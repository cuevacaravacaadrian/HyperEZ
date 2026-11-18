#!/bin/sh
set -e
DEST="${HYPEREZ_HOME:-$HOME/.local}"
HERE=$(cd "$(dirname "$0")" && pwd)

if [ "$1" = "--uninstall" ]; then
    if [ -x "$DEST/bin/hyper" ]; then "$DEST/bin/hyper" unregister || true; fi
    rm -f "$DEST/bin/hyper"
    rm -rf "$DEST/share/hyperez"
    echo "HyperEZ desinstalado."
    exit 0
fi

mkdir -p "$DEST/bin" "$DEST/share/hyperez"
cp "$HERE/bin/hyper" "$DEST/bin/hyper"
chmod +x "$DEST/bin/hyper"
cp -R "$HERE/share/hyperez/." "$DEST/share/hyperez/"
echo "✓ HyperEZ $("$DEST/bin/hyper" version | head -n 1 | sed 's/HyperEZ //') instalado en $DEST/bin/hyper"

"$DEST/bin/hyper" register || echo "(no se pudo registrar el lenguaje en el escritorio; hyper funciona igual)"

VSIX=$(ls "$HERE"/*.vsix 2>/dev/null | head -n 1 || true)
if [ -n "$VSIX" ] && command -v code >/dev/null 2>&1; then
    code --install-extension "$VSIX" --force >/dev/null 2>&1 && echo "✓ Extensión de VS Code instalada" || true
fi

case ":$PATH:" in
    *":$DEST/bin:"*) echo "Escribe 'hyper' para abrir la consola interactiva." ;;
    *)
        echo
        echo "Falta añadir $DEST/bin al PATH. Ejecuta esto y abre una terminal nueva:"
        echo "  echo 'export PATH=\"$DEST/bin:\$PATH\"' >> ~/.profile"
        ;;
esac
