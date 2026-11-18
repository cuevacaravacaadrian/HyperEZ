# HyperEZ en tu editor

Al instalar HyperEZ (o con `hyper register`), los editores que tengas aprenden HyperEZ solos, sin extensiones ni pasos manuales.

| Editor | Qué tiene | Cómo se configura |
|---|---|---|
| **Visual Studio Code** | todo: colores, errores en vivo, autocompletado, F12, F2, formato, botones ▶ | el instalador de Windows lo hace si tienes VS Code; también con el `.vsix` · [guía](../docs/herramientas/vscode.md) |
| **Notepad++** | colores, plegado de llaves | solo, con el instalador o `hyper register` ([`notepad++/HyperEZ.xml`](notepad++/HyperEZ.xml)) |
| **Sublime Text / TextMate** | colores | solo ([`sublime/HyperEZ.tmLanguage`](sublime/HyperEZ.tmLanguage)) |
| **Vim / Neovim** | colores, comentarios, sangría, `:make` con `hyper check` | solo ([`vim/`](vim)) |
| **gedit, GNOME Text Editor** (Linux) | colores | solo ([`gtksourceview/hyperez.lang`](gtksourceview/hyperez.lang)) |
| **Kate, KWrite** (Linux) | colores, plegado | solo ([`kate/hyperez.xml`](kate/hyperez.xml)) |
| **nano** (Linux, macOS) | colores | solo ([`nano/hyperez.nanorc`](nano/hyperez.nanorc)) |
| **Cualquier editor con LSP** (Helix, Zed, Emacs, Sublime con LSP…) | errores, autocompletado, hover, ir a la definición, renombrar, formato | configura el servidor de lenguaje `hyper lsp` para los archivos `.hez` y `.hz` |
| **Bloc de notas y cualquier editor de texto** | los `.hez` son texto UTF-8 | se editan tal cual y se ejecutan con doble clic o `hyper archivo.hez` |
| **HyperEZ Editor** (Windows, opcional) | colores, errores en vivo, F5, pestañas, panel de salida | complemento del instalador · [guía](../docs/herramientas/editor.md) |
| **Páginas web** (highlight.js) | colores en blogs y documentación | [`highlightjs/hyperez.js`](highlightjs/hyperez.js) junto a highlight.js: `<code class="language-hz">` |
| **GitHub** | reconocimiento oficial del lenguaje | [`linguist/`](linguist): el kit para proponerlo a GitHub Linguist |

Todas las sintaxis se generan a partir de la gramática de VS Code con `python tools/gen_editors.py`.

## Servidor de lenguaje en otros editores

`hyper lsp` habla el protocolo LSP 3.17 por la entrada y la salida estándar. Por ejemplo, en Neovim (con `nvim-lspconfig` o a mano):

```text
vim.filetype.add({ extension = { hez = "hyperez", hz = "hyperez" } })
vim.lsp.start({ name = "hyperez", cmd = { "hyper", "lsp" }, root_dir = vim.fn.getcwd() })
```

y en Helix (`languages.toml`):

```text
[[language]]
name = "hyperez"
scope = "source.hyperez"
file-types = ["hez", "hz"]
language-servers = ["hyper"]
comment-token = "//"
indent = { tab-width = 4, unit = "    " }

[language-server.hyper]
command = "hyper"
args = ["lsp"]
```
