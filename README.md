# DBI 912 — traducciones comunitarias

**Español latinoamericano probado en Nintendo Switch · English experimental**

Este fork de **Pedro Luna** distribuye un paquete comunitario para usar **DBI 912**
en español latinoamericano o inglés mediante `translation.bin`. Se apoya en DBI,
creado por **duckbill** y alojado por **rashevskyv**, y en el motor y los diccionarios
existentes de **DBIPatcher** y sus colaboradores.

El programa original y las traducciones existentes son trabajo de sus respectivos
autores. Nuestro aporte incluye la preparación del paquete, documentación, pruebas
en español y traducciones de siete categorías de un servidor como complemento opcional.

**Es un paquete comunitario, no un release oficial de DBI.** La versión `v1.1`
identifica el paquete de traducción; la aplicación sigue siendo **DBI 912**.

[Proyecto original](https://github.com/rashevskyv/dbi) ·
[DBIPatcher](https://github.com/rashevskyv/DBIPatcher) ·
[Manual original conservado](README_UPSTREAM.md) ·
[Guía rusa original](README_RU.md)

## Descargar

[Release comunitario v1.1 para DBI 912](https://github.com/pedroluna-gh/dbi/releases/tag/community-translations-v1.1-dbi912)

| Paquete | Estado de las pruebas |
| --- | --- |
| [Español latinoamericano — es419](https://github.com/pedroluna-gh/dbi/releases/download/community-translations-v1.1-dbi912/DBI-912-community-v1.1-es419-probado.zip) | Probado en Switch: inicio y cierre; con el complemento opcional, categorías traducidas, listado esperado, descarga e instalación completa de un elemento. |
| [English — experimental](https://github.com/pedroluna-gh/dbi/releases/download/community-translations-v1.1-dbi912/DBI-912-community-v1.1-en-experimental.zip) | Comprobaciones automáticas aprobadas. **Todavía no probado en consola.** |
| [SHA256SUMS.txt](https://github.com/pedroluna-gh/dbi/releases/download/community-translations-v1.1-dbi912/SHA256SUMS.txt) | Hashes para comprobar los dos ZIP. |

Cada ZIP incluye el **DBI 912 adaptado**, un diccionario completo `translation.bin`,
los CSV de origen, instrucciones, créditos y un manifiesto con hashes.
El idioma disponible en este fork no cambia el estado de los releases del proyecto original.

## Instalar en la Switch

1. Descarga el ZIP del idioma deseado y cierra DBI por completo.
2. Conecta la microSD a la computadora. Si usas Hekate por USB, entra a
   **Tools → USB Tools → SD Card**.
3. Copia el contenido de `switch/DBI/` del ZIP a la misma carpeta de la microSD:

   ```text
   sdmc:/switch/DBI/DBI.nro
   sdmc:/switch/DBI/translation.bin
   ```

4. Conserva tu `dbi.config` y colócalo junto al nuevo `DBI.nro`. Si ya tienes otra copia de `DBI.nro`, por ejemplo
   en `/switch/DBI.nro`, guarda la anterior fuera de `/switch/` para evitar
   accesos duplicados y abrir por error el ejecutable ruso original.
5. Expulsa la microSD de forma segura, vuelve a Atmosphere y abre DBI desde
   Sphaira o tu menú de homebrew.

**No basta con poner `translation.bin` junto al DBI ruso original:** necesitas
el ejecutable adaptado incluido en el paquete. El diccionario debe estar
exactamente en `sdmc:/switch/DBI/translation.bin`.

Para cambiar entre español e inglés, cierra DBI y reemplaza únicamente
`translation.bin` por el del otro paquete. No hace falta un selector ni otro lanzador.
Para volver a la versión rusa original, restaura tu `DBI.nro` original.

## Categorías de servidor: complemento opcional

La tabla instalada por defecto contiene el diccionario de DBIPatcher sin nuestras
categorías adicionales. Si quieres traducir las siete categorías observadas en
el listado remoto de UltraNX, copia **`opcional-ultranx/translation.bin`** del ZIP
del idioma elegido a **`sdmc:/switch/DBI/translation.bin`**, reemplazando la tabla
activa con DBI cerrado.

Ese archivo también es un diccionario completo. Añade las siete categorías con
y sin numeración: 14 entradas. **La prueba completa de descarga e instalación en
español se hizo con esta variante opcional.**

Estas etiquetas proceden del listado del servidor, no del programa DBI. El
complemento no configura servidores ni incluye contenido del catálogo. Los
textos remotos nuevos y las imágenes no se traducen automáticamente.

## Qué se probó

La prueba en español se realizó con **DBI 912, firmware 19.0.1, Atmosphere 1.12.1,
emuMMC y Sphaira**. El paquete conserva los mismos hashes del ejecutable y de la
tabla opcional española que se usaron en esa prueba.

Ambos idiomas pasaron 84 comprobaciones de las nuevas etiquetas/rutas y 452 casos
de regresión por idioma en emulación ARM64. La suite de DBIPatcher pasó 159 pruebas
y omitió 9. Esto no equivale a probar todas las funciones, todos los servidores
ni otras versiones de DBI o firmware. El inglés sigue pendiente de prueba en consola.

## Documentación y créditos

- [Instrucciones completas y reproducción de los paquetes](community-release/README.md).
- [Guía de traducciones y formato de las categorías adicionales](TRANSLATIONS.md).
- [Manual original completo](README_UPSTREAM.md), conservado sin modificar como
  referencia del proyecto original. Para instalar este paquete, usa las instrucciones de arriba.
- [Contribución integrada en el proyecto original: PR #408](https://github.com/rashevskyv/dbi/pull/408).

Gracias a **duckbill**, **rashevskyv**, los colaboradores de **DBIPatcher**,
**0xroast/dbi-translate** y los autores de las guías originales. El paquete usa
DBIPatcher en el commit `65cc1ccdf8bc2552090e69df9c3d06543e740178` y conserva los
avisos del motor de traducción. La licencia de ese motor no se atribuye a todo DBI.

## English quick start

This fork provides **unofficial community translation packages for DBI 912**.
Latin American Spanish was tested on a Switch, including a completed download
and installation with the optional remote-category table. **English is experimental
and has only passed automated checks.** Existing DBI and DBIPatcher work remains
credited to its original authors.

Download a ZIP above, close DBI, and copy its `switch/DBI/` contents to your SD card.
Keep your existing configuration and avoid duplicate DBI launch entries. The
included patched NRO is required; the original Russian executable does not load
external translations. The active table must be at `sdmc:/switch/DBI/translation.bin`.

The default table contains the upstream dictionary. To opt into the additional
server category labels, replace the active table with `opcional-ultranx/translation.bin`
from the same language ZIP. Close DBI before changing tables. For detailed usage,
see the [package guide](community-release/README.md) and the
[preserved original manual](README_UPSTREAM.md).
