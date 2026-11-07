"""Package the exact verified DBI 912 translation artifacts; no network operations."""
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

PIN = '65cc1ccdf8bc2552090e69df9c3d06543e740178'
NRO_SHA = 'ebbf1422c07daa77d70ca6396b872fcdabf6db84b6c780d1072bdee6b4576100'
HASHES = {
    'es419': ('567c6ba222b392a48d23ea801d81a02c1f3db02eb04626552fc9596ee84f9749', 'cf0f1da32ba8b4518a2c341d9993300bf7650cdbff3707ea0507b048966d5be8'),
    'en': ('fc449d83a027a9b496320d5420c8b459daa4f47508412256c0df9a90047adb93', '155df9dadb0af4557c56c21eb2db27514019ce7964ec7410dd59cccb33ef371f'),
}

def sha(data):
    return hashlib.sha256(data).hexdigest()

def csv_bytes(rows):
    out = io.StringIO(newline='')
    writer = csv.DictWriter(out, fieldnames=['original', 'translation'], lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue().encode('utf-8')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--patcher', type=Path, required=True)
    parser.add_argument('--nro', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    patcher = args.patcher.resolve()
    repo = Path(__file__).resolve().parents[1]
    head = subprocess.run(['git', '-C', str(patcher), 'rev-parse', 'HEAD'], check=True, capture_output=True, text=True).stdout.strip()
    if head != PIN:
        raise ValueError('DBIPatcher checkout does not match the verified commit')
    nro = args.nro.read_bytes()
    if sha(nro) != NRO_SHA:
        raise ValueError('Patched NRO does not match the verified DBI 912 build')
    sys.path.insert(0, str(patcher))
    from scripts.build_translation_bin import build_table, _unescape
    args.out.mkdir(parents=True, exist_ok=True)
    artifact_hashes = []
    for lang in ('es419', 'en'):
        with (patcher / f'translations/{lang}.csv').open(encoding='utf-8', newline='') as f:
            baseline = list(csv.DictReader(f))
        with (repo / f'translations/server-categories/{lang}.csv').open(encoding='utf-8', newline='') as f:
            extra = list(csv.DictReader(f))
        if len(extra) != 14:
            raise ValueError('Expected exactly 14 optional category mappings')
        tables = []
        for index, rows in enumerate((baseline, baseline + extra)):
            seen, pairs = set(), []
            for row in rows:
                key, val = (_unescape(row[k]).encode('utf-8') for k in ('original', 'translation'))
                if not key or not val or key in seen:
                    raise ValueError('Empty or duplicate source string')
                seen.add(key)
                if key != val:
                    pairs.append((key, val))
            table, _, _ = build_table(pairs)
            if sha(table) != HASHES[lang][index]:
                raise ValueError(f'Unexpected table hash: {lang}, optional={bool(index)}')
            tables.append(table)
        manifest = {
            'package_version': '1.1', 'dbi_version': '912', 'language': lang,
            'community_release': True, 'patcher_commit': PIN,
            'nro_sha256': NRO_SHA, 'baseline_translation_sha256': HASHES[lang][0],
            'optional_ultranx_translation_sha256': HASHES[lang][1],
            'hardware_test': 'Spanish launch/exit; optional table: category labels, listing, one download and completed installation' if lang == 'es419' else 'NOT TESTED ON HARDWARE; automated checks only',
            'tested_firmware': '19.0.1 / AMS 1.12.1 / emuMMC' if lang == 'es419' else None,
        }
        files = {
            'switch/DBI/DBI.nro': nro,
            'switch/DBI/translation.bin': tables[0],
            'opcional-ultranx/translation.bin': tables[1],
            'source/translation.csv': csv_bytes(baseline),
            'source/translation-ultranx.csv': csv_bytes(baseline + extra),
            'LEEME-README.md': (repo / 'community-release/README.md').read_bytes(),
            'manifest.json': (json.dumps(manifest, indent=2) + '\n').encode(),
            'licenses/runtime-MIT.txt': (patcher / 'vendor/dbi_translate/LICENSE').read_bytes(),
            'licenses/runtime-NOTICE.txt': (patcher / 'vendor/dbi_translate/NOTICE').read_bytes(),
            'licenses/DBIPatcher-UPSTREAM.md': (patcher / 'UPSTREAM.md').read_bytes(),
        }
        suffix = 'es419-probado' if lang == 'es419' else 'en-experimental'
        archive = args.out / f'DBI-912-community-v1.1-{suffix}.zip'
        with ZipFile(archive, 'w') as z:
            for name, data in sorted(files.items()):
                info = ZipInfo(name, date_time=(2026, 11, 6, 0, 0, 0))
                info.compress_type = ZIP_DEFLATED
                z.writestr(info, data)
        with ZipFile(archive) as z:
            if z.testzip() is not None or set(z.namelist()) != set(files):
                raise ValueError('Archive integrity or content failure')
            for name, data in files.items():
                if z.read(name) != data:
                    raise ValueError(f'Archive content mismatch: {name}')
        artifact_hashes.append(f'{sha(archive.read_bytes())}  {archive.name}')
        print(f'Verified: {archive.name}, {archive.stat().st_size} bytes')
    (args.out / 'SHA256SUMS.txt').write_text('\n'.join(artifact_hashes) + '\n', encoding='utf-8')

if __name__ == '__main__':
    main()
