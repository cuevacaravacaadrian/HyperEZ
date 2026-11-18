# Instaladores y registro del lenguaje

Los instaladores no instalan una aplicación: registran el **lenguaje** HyperEZ en el sistema operativo y en los editores de código. El trabajo lo hace `hyper register` (y su inverso, `hyper unregister`), que el instalador de Windows y `install.sh` usan por dentro.

## Windows: `HyperEZ-Setup.exe`

Programa propio (`packaging/windows/setup.cpp`) con los archivos dentro: no necesita nada externo ni permisos de administrador. Instala por usuario en `%LOCALAPPDATA%\Programs\HyperEZ`:

```text
bin\hyper.exe          el lenguaje y todas sus herramientas
bin\hyperez-editor.exe HyperEZ Editor (complemento opcional)
docs\                  documentación en Markdown (incluida la referencia de la API)
docs-html\             la misma documentación en HTML, sin conexión
editors\               sintaxis de HyperEZ para Notepad++, Sublime Text, Vim, nano, gedit, Kate y highlight.js
examples\              ejemplos
icons\                 iconos de los archivos .hez
vscode\*.vsix          el soporte para VS Code
uninstall.exe          desinstalador (y uninstall.lst con lo instalado)
```

### Qué toca en el registro

Todo en `HKEY_CURRENT_USER` (solo afecta a tu usuario):

| Clave | Para qué |
|---|---|
| `Software\HyperEZ\Language` | el registro del lenguaje: `Name`, `Version`, `Extensions`, `ContentType`, `ProgID`, `Executable`, `Run`, `Check`, `Format`, `LanguageServer`, `LineComment`, `BlockComment` |
| `Software\Classes\.hez`, `.hz` | extensiones → tipo `HyperEZ.Source`, `text/x-hyperez`, `PerceivedType=text`, filtro de texto para Windows Search; *Nuevo → Programa HyperEZ* (solo `.hez`) |
| `Software\Classes\HyperEZ.Source` | icono y acciones: *Ejecutar con HyperEZ* (doble clic), *Editar*, *Comprobar errores*, *Ejecutar y repetir al guardar* |
| `Software\Classes\Directory\Background\shell\HyperEZ` | *Abrir HyperEZ aquí* |
| `Software\Classes\Applications\hyper.exe` | HyperEZ en *Abrir con...* |
| `...\Explorer\FileExts\.hez\UserChoice` | se borra: si antes elegiste otro programa para `.hez`, HyperEZ vuelve a ser el predeterminado |
| `Environment\Path` | la carpeta `bin` de HyperEZ |
| `Software\Microsoft\Windows\CurrentVersion\App Paths\hyper.exe` | *Win+R → hyper* funciona al momento |
| `Software\Microsoft\Windows\CurrentVersion\Uninstall\HyperEZ` | aparece en *Aplicaciones* |

El doble clic ejecuta `hyper.exe run --pause "archivo"`: la ventana espera una tecla al terminar para que se pueda leer el resultado. *Editar* abre VS Code si está instalado y, si no, el Bloc de notas (o HyperEZ Editor si se instaló).

### Editores de código

Sin extensiones: el instalador copia la sintaxis de HyperEZ en la configuración de cada editor que encuentra.

| Editor | Dónde |
|---|---|
| Notepad++ | `%APPDATA%\Notepad++\userDefineLangs\HyperEZ.xml` |
| Sublime Text | `%APPDATA%\Sublime Text\Packages\User\HyperEZ.tmLanguage` |
| Vim | `%USERPROFILE%\vimfiles\{syntax,ftdetect,ftplugin}\hyperez.vim` |
| Neovim | `%LOCALAPPDATA%\nvim\{syntax,ftdetect,ftplugin}\hyperez.vim` |
| Visual Studio Code | el `.vsix` incluido (errores en vivo, autocompletado, F5) |

### Opciones

```text
/S                 silencioso
/D=carpeta         carpeta de instalación
/NOASSOC           no registrar .hez/.hz
/NOPATH            no tocar el PATH
/NOEDITORS         no tocar Notepad++, Sublime Text, Vim ni Neovim
/NOVSCODE          no instalar el soporte de VS Code
/EDITOR            instalar también HyperEZ Editor
```

Para pruebas automáticas, `/REGROOT=Software\Prueba` escribe el registro en otra clave y `HYPEREZ_EDITORS_HOME` cambia la carpeta de usuario donde se buscan los editores.

### Crear el instalador

`./build.ps1` lo compila todo y deja en `dist/` el instalador, el `.vsix` y `hyper.exe`. El instalador empaqueta lo que hay en `build/stage` (ver `packaging/windows/stage.cmake`).

## Linux y macOS: `install.sh`

El paquete `HyperEZ-<versión>-<sistema>-<arquitectura>.tar.gz` (lo crea `packaging/unix/package.sh`, y GitHub Actions en cada versión) contiene `bin/hyper`, `share/hyperez/` (ejemplos, documentación, icono y sintaxis para editores) e `install.sh`.

`sh install.sh` instala en `~/.local` y ejecuta `hyper register`, que:

- en Linux registra el tipo MIME `text/x-hyperez` para `*.hez` y `*.hz` (`~/.local/share/mime/packages/hyperez.xml`), crea `~/.local/share/applications/hyperez.desktop` y lo marca como predeterminado con `xdg-mime`;
- en Linux instala la sintaxis para gedit / GNOME Text Editor (`~/.local/share/gtksourceview-{3.0,4,5}/language-specs/hyperez.lang`) y Kate (`~/.local/share/org.kde.syntax-highlighting/syntax/hyperez.xml`);
- en Linux y macOS, si los usas, configura Vim (`~/.vim`), Neovim (`~/.config/nvim`), nano (una línea `include` en `~/.nanorc`) y Sublime Text.

`sh install.sh --uninstall` lo deshace todo.
