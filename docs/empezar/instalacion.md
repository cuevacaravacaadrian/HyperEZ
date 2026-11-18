# Instalación

Instalar HyperEZ no instala una aplicación: **registra el lenguaje en tu sistema**, igual que Python o Node. Después, tu sistema operativo sabe qué es un archivo `.hez`, la orden `hyper` funciona en cualquier terminal y tus editores de código colorean HyperEZ sin instalar extensiones.

## Windows

1. Descarga `HyperEZ-Setup-<versión>.exe` de la [página de versiones](https://github.com/cuevacaravacaadrian/HyperEZ/releases/latest).
2. Ejecútalo y pulsa **Instalar**. No necesita permisos de administrador. Si aparece "Windows protegió su PC" (el instalador no está firmado), pulsa *Más información → Ejecutar de todas formas*.
3. Abre una terminal **nueva** y escribe `hyper`.

Por defecto el instalador:

- copia el lenguaje en `%LOCALAPPDATA%\Programs\HyperEZ` (compilador, biblioteca estándar, servidor de lenguaje, ejemplos y documentación);
- registra el lenguaje en Windows (`HKCU\Software\HyperEZ\Language`): nombre, versión, extensiones, tipo MIME y las órdenes para ejecutar, comprobar, dar formato y el servidor de lenguaje, para que cualquier herramienta pueda encontrarlas;
- registra los archivos **`.hez` y `.hz`** como *Programa HyperEZ*: icono propio, tipo `text/x-hyperez`, se abren como texto en cualquier editor, Windows Search indexa su contenido y el menú contextual tiene *Ejecutar con HyperEZ* (doble clic), *Editar*, *Comprobar errores* y *Ejecutar y repetir al guardar*; en cualquier carpeta, *Nuevo → Programa HyperEZ* y *Abrir HyperEZ aquí*;
- enseña HyperEZ a los editores que tengas (**Notepad++, Sublime Text, Vim y Neovim**): reconocen los `.hez` y los colorean sin extensiones ni pasos manuales;
- si tienes **Visual Studio Code**, le añade el soporte completo (errores en vivo, autocompletado, F5);
- añade `hyper` al `PATH`.

**HyperEZ Editor**, un editor sencillo para empezar, es un complemento opcional que viene desmarcado.

Se desinstala desde *Configuración → Aplicaciones → HyperEZ*. La desinstalación quita también el registro del lenguaje y lo que se añadió a tus editores.

### Instalación silenciosa

```text
HyperEZ-Setup-1.0.0.exe /S                  sin preguntas
HyperEZ-Setup-1.0.0.exe /S /D=C:\HyperEZ    en otra carpeta
HyperEZ-Setup-1.0.0.exe /S /EDITOR          incluye HyperEZ Editor
```

Opciones: `/NOASSOC` (no registrar los archivos), `/NOPATH`, `/NOEDITORS` (no tocar Notepad++, Sublime Text ni Vim), `/NOVSCODE`, `/EDITOR`.

## Linux y macOS

1. Descarga `HyperEZ-<versión>-linux-x64.tar.gz` (o `-macos-arm64`) de la página de versiones.
2. Descomprímelo e instala para tu usuario (sin `sudo`):

```text
tar xzf HyperEZ-1.0.0-linux-x64.tar.gz
cd HyperEZ-1.0.0-linux-x64
sh install.sh
```

Queda en `~/.local/bin/hyper`. `install.sh` ejecuta `hyper register`, que en Linux registra el tipo MIME `text/x-hyperez` para `*.hez` y `*.hz` y, en Linux y macOS, enseña HyperEZ a **gedit, GNOME Text Editor, Kate, Vim, Neovim, nano y Sublime Text**. Para desinstalar: `sh install.sh --uninstall`.

## Registrar el lenguaje a mano

En cualquier sistema, `hyper register` registra el lenguaje con el `hyper` que lo ejecuta y configura los editores que encuentre; `hyper unregister` lo deshace. Si instalas un editor nuevo después de HyperEZ, vuelve a ejecutar `hyper register`.

## Visual Studio Code

El instalador de Windows lo configura solo si VS Code ya está instalado. Si instalas VS Code después, añade el soporte desde *Extensiones → ⋯ → Instalar desde VSIX…* con `hyperez-<versión>.vsix`, o desde la terminal:

```text
code --install-extension hyperez-1.0.0.vsix
```

## Desde el código fuente

Mira [CONTRIBUTING.md](../../CONTRIBUTING.md): en Windows basta con `./build.ps1`; en Linux y macOS, CMake y un compilador de C++20:

```text
cmake -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=Release
cmake --build build
ctest --test-dir build
```
