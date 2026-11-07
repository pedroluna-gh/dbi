# DBI 912 — paquete comunitario de traducción v1.1

**Español latinoamericano probado en Switch. Inglés experimental: comprobaciones automáticas, sin prueba en consola.**

Este paquete de `pedroluna-gh/dbi` usa DBI 912 y el motor/diccionarios existentes de
[DBIPatcher](https://github.com/rashevskyv/DBIPatcher). No es una versión oficial
nueva de DBI ni DBI 913. La contribución propia agrega documentación y las siete
categorías de un servidor como complemento opcional.

## Instalación

1. Descarga el ZIP del idioma deseado. Cierra DBI por completo.
2. Copia el contenido de `switch/DBI/` del ZIP a `sdmc:/switch/DBI/`.
   Incluye el ejecutable DBI 912 adaptado y el diccionario completo `translation.bin`.
3. Conserva tu `dbi.config`. Si ya tienes `DBI.nro` en otra ubicación de `/switch/`,
   conserva una sola entrada de lanzamiento para evitar abrir la copia anterior.
4. Expulsa la microSD de forma segura y abre DBI desde tu menú de homebrew.

El DBI ruso original no carga `translation.bin`. Se necesita el ejecutable adaptado
incluido. El diccionario debe estar exactamente en `sdmc:/switch/DBI/translation.bin`.
Para cambiar entre inglés y español, cierra DBI y reemplaza solo ese archivo por
el del otro ZIP. Para volver a la versión rusa original, restaura tu ejecutable original.

## Categorías remotas: opción separada

El diccionario instalado por defecto es el de DBIPatcher sin nuestras categorías
de servidor. Si usas las categorías de UltraNX observadas en `/ru/`, reemplázalo
por `opcional-ultranx/translation.bin`, incluido en el mismo ZIP. Es una tabla
completa que añade siete categorías, con y sin numeración: 14 entradas.
No mezcles ambos binarios ni copies únicamente el CSV complementario como tabla.

Este complemento traduce etiquetas del listado remoto. No son textos internos
de DBI, no configura ningún servidor ni incluye contenido del catálogo.
Las imágenes y las etiquetas remotas nuevas no se traducen automáticamente.

## Pruebas y límites

En español se comprobó el inicio y cierre de DBI. Con el complemento opcional se
confirmaron las categorías traducidas, el listado esperado de «Todos los juegos»,
la descarga de un elemento y su instalación completa. Se probó en firmware
19.0.1 / Atmosphere 1.12.1, emuMMC, abriendo DBI desde Sphaira.

El inglés no se probó en una Switch. Ambos idiomas pasaron 84 comprobaciones
de las nuevas etiquetas/rutas y 452 casos de regresión por idioma en emulación
ARM64. La suite original pasó 159 pruebas; 9 se omitieron. Las pruebas no cubren
todas las funciones, todos los servidores ni otras versiones de DBI o firmware.
El inglés conserva cinco advertencias de puntuación del relato Shadok presentes
en el diccionario original; los marcadores de formato se conservaron.

`manifest.json` contiene los hashes de los archivos y su procedencia. El NRO es
idéntico en ambos paquetes; la tabla española opcional es exactamente la probada
en la consola. No se incluyen configuraciones, identificadores de dispositivo,
credenciales ni datos del usuario.

## Procedencia y reproducción

- DBI: duckbill; repositorio mantenido por rashevskyv.
- Diccionarios y adaptación: DBIPatcher, commit `65cc1ccdf8bc2552090e69df9c3d06543e740178`.
- Motor incorporado: `0xroast/dbi-translate`, con su licencia MIT y avisos conservados.
- Categorías adicionales y documentación: contribución de Pedro Luna, PR #408.

La licencia del motor no atribuye esa licencia a todo el ejecutable DBI.

Para reproducir los ZIP, usa un checkout de DBIPatcher en el commit indicado y
sus dependencias. Genera el NRO adaptado con `scripts/patch_dbi.py` usando tu copia
del DBI 912 ruso original; luego ejecuta:

```text
python -I community-release/build.py --patcher /ruta/DBIPatcher --nro /ruta/DBI-912-adaptado.nro --out /ruta/paquetes
```

El generador comprueba los hashes del NRO y de las cuatro tablas antes de crear
los ZIP; rechaza archivos distintos de los verificados.

## English

This is an unofficial community translation package for DBI 912, not a new
official DBI version. **Latin American Spanish was tested on a Switch**, including
a download and completed installation with the optional server-category table.
**English is experimental and has only passed automated checks.**

Copy the ZIP's `switch/DBI/` contents to your SD card, preserve your own configuration,
and avoid duplicate DBI launch entries. The included patched NRO is required:
the original Russian executable cannot load an external translation table.
The table must be at `sdmc:/switch/DBI/translation.bin`.

The default table is the upstream dictionary. To opt into the additional remote
category labels, replace it with `opcional-ultranx/translation.bin` from the same
ZIP. That optional file is also a complete table, not a delta. It does not add
server configuration or catalog content. Close DBI before replacing a table.
Hardware validation applies only to the Spanish flow described above.
