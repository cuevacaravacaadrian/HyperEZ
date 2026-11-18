#!/usr/bin/env python3
import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KIT = os.path.join(RAIZ, "editors", "linguist")
UPSTREAM = "https://github.com/github-linguist/linguist.git"
NOMBRE = "HyperEZ"
RAMA = "hyperez"


def usuario_por_defecto():
    with open(os.path.join(RAIZ, "src", "core", "version.h"), encoding="utf-8") as f:
        m = re.search(r'HYPEREZ_REPO_URL "https://github\.com/([^/"]+)/', f.read())
    return m.group(1) if m else "cuevacaravacaadrian"


def git(*args, cwd=None, check=True, capture=False):
    r = subprocess.run(["git", *args], cwd=cwd, text=True, encoding="utf-8",
                       stdout=subprocess.PIPE if capture else None, stderr=subprocess.PIPE if capture else None)
    if check and r.returncode != 0:
        sys.exit("✗ git %s falló%s" % (" ".join(args), (":\n" + (r.stderr or "")) if capture else ""))
    return (r.stdout or "").strip() if capture else r.returncode


def existe_repo(url):
    r = subprocess.run(["git", "ls-remote", "--heads", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                       env=dict(os.environ, GIT_TERMINAL_PROMPT="0"))
    return r.returncode == 0


def leer(p):
    with open(p, encoding="utf-8", newline="") as f:
        return f.read()


def escribir(p, texto):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(texto)


def language_id(nombre):
    return int(hashlib.sha256(nombre.encode()).hexdigest(), 16) % (2 ** 30 - 1)


def clave(s):
    return s.encode("utf-8")


def anadir_lenguaje(lin):
    ruta = os.path.join(lin, "lib", "linguist", "languages.yml")
    texto = leer(ruta)
    if re.search(r"^%s:\s*$" % re.escape(NOMBRE), texto, re.M):
        print("  · languages.yml ya tiene %s" % NOMBRE)
        return
    entrada = [l for l in leer(os.path.join(KIT, "languages.yml")).splitlines() if l and not l.startswith("#")]
    entrada.append("  language_id: %d" % language_id(NOMBRE))
    lineas = texto.split("\n")
    pos = None
    for i, l in enumerate(lineas):
        m = re.match(r"^([^\s#][^:]*):\s*$", l)
        if m and i > 0 and clave(m.group(1).strip('"')) > clave(NOMBRE):
            pos = i
            break
    if pos is None:
        sys.exit("✗ no encuentro dónde va %s en languages.yml" % NOMBRE)
    lineas[pos:pos] = entrada
    escribir(ruta, "\n".join(lineas))
    print("  ✓ lib/linguist/languages.yml: %s (language_id %d), antes de %s" % (NOMBRE, language_id(NOMBRE), lineas[pos + len(entrada)].rstrip(":")))


def copiar_muestras(lin):
    destino = os.path.join(lin, "samples", NOMBRE)
    os.makedirs(destino, exist_ok=True)
    nombres = sorted(f for f in os.listdir(os.path.join(KIT, "samples")) if f.endswith(".hez"))
    for f in nombres:
        shutil.copyfile(os.path.join(KIT, "samples", f), os.path.join(destino, f))
    print("  ✓ samples/%s: %s" % (NOMBRE, ", ".join(nombres)))


def insertar_bloque(texto, cabecera_re, nuevo_nombre, bloque):
    for m in re.finditer(cabecera_re, texto, re.M):
        if clave(m.group(1)) > clave(nuevo_nombre):
            return texto[:m.start()] + bloque + texto[m.start():]
    return texto.rstrip("\n") + "\n" + bloque


def anadir_gramatica(lin, usuario):
    url = "https://github.com/%s/hyperez-grammar" % usuario
    sub = "vendor/grammars/hyperez-grammar"
    if not existe_repo(url):
        print("  ⚠ no existe %s: créalo (público, con lo que hay en editors/linguist/grammar) y vuelve a ejecutar" % url)
        return False
    if not os.path.isdir(os.path.join(lin, sub)):
        git("submodule", "add", "-f", url + ".git", sub, cwd=lin)
    gm = os.path.join(lin, ".gitmodules")
    texto = leer(gm)
    bloques = re.findall(r'\[submodule "[^"]+"\]\n(?:\t[^\n]*\n)*', texto)
    if "".join(bloques) == texto:
        bloques.sort(key=lambda b: clave(re.match(r'\[submodule "([^"]+)"\]', b).group(1)))
        escribir(gm, "".join(bloques))
    gy = os.path.join(lin, "grammars.yml")
    texto = leer(gy)
    if sub + ":" not in texto:
        texto = insertar_bloque(texto, r"^vendor/grammars/([^:\n]+):$", "hyperez-grammar", sub + ":\n- source.hyperez\n")
        escribir(gy, texto)
    rd = os.path.join(lin, "vendor", "README.md")
    texto = leer(rd)
    linea = "- **%s:** [%s/hyperez-grammar](%s)\n" % (NOMBRE, usuario, url)
    if linea not in texto:
        texto = insertar_bloque(texto, r"^- \*\*([^*]+):\*\* ", NOMBRE, linea)
        escribir(rd, texto)
    version = git("rev-parse", "HEAD", cwd=os.path.join(lin, sub), capture=True)
    licencia = leer(os.path.join(lin, sub, "LICENSE")).replace("\r\n", "\n").rstrip("\n")
    dep = ("---\nname: hyperez-grammar\nversion: %s\ntype: git_submodule\nhomepage: %s\nlicense: mit\nlicenses:\n"
           "- sources: LICENSE\n  text: |\n%s\nnotices: []\n") % (version, url, "\n".join(("    " + l) if l else "" for l in licencia.split("\n")))
    escribir(os.path.join(lin, "vendor", "licenses", "git_submodule", "hyperez-grammar.dep.yml"), dep)
    print("  ✓ gramática: %s (%s), grammars.yml, vendor/README.md y su licencia" % (sub, version[:10]))
    return True


def main():
    ap = argparse.ArgumentParser(description="Prepara la propuesta de HyperEZ para GitHub Linguist")
    ap.add_argument("--dir", default=os.path.join(RAIZ, "build-linguist"), help="carpeta de la copia de Linguist")
    ap.add_argument("--usuario", default=usuario_por_defecto(), help="tu usuario de GitHub (fork y hyperez-grammar)")
    ap.add_argument("--push", action="store_true", help="subir la rama a tu fork")
    a = ap.parse_args()
    fork = "https://github.com/%s/linguist.git" % a.usuario

    subprocess.run([sys.executable, os.path.join(RAIZ, "tools", "linguist_kit.py")], check=True, stdout=subprocess.DEVNULL)

    print("Linguist en %s" % a.dir)
    if not os.path.isdir(os.path.join(a.dir, ".git")):
        tiene_fork = existe_repo(fork)
        origen = fork if tiene_fork else UPSTREAM
        print("  · clonando %s (sin el contenido de los commits antiguos)" % origen)
        git("clone", "--filter=blob:none", origen, a.dir)
        if not tiene_fork:
            git("remote", "rename", "origin", "upstream", cwd=a.dir)
    remotos = git("remote", cwd=a.dir, capture=True).split()
    if "upstream" not in remotos:
        git("remote", "add", "upstream", UPSTREAM, cwd=a.dir)
    if "origin" not in remotos and existe_repo(fork):
        git("remote", "add", "origin", fork, cwd=a.dir)
    git("fetch", "upstream", "main", cwd=a.dir)
    if git("status", "--porcelain", cwd=a.dir, capture=True):
        sys.exit("✗ %s tiene cambios sin guardar: guárdalos o bórralos antes" % a.dir)
    git("checkout", "-B", RAMA, "upstream/main", cwd=a.dir)

    anadir_lenguaje(a.dir)
    copiar_muestras(a.dir)
    con_gramatica = anadir_gramatica(a.dir, a.usuario)

    git("add", "-A", cwd=a.dir)
    git("commit", "-q", "-m", "Add HyperEZ language", cwd=a.dir)
    print("  ✓ commit en la rama %s: %s" % (RAMA, git("log", "-1", "--format=%h %s", cwd=a.dir, capture=True)))

    if not con_gramatica:
        print("\nFalta la gramática: crea el repositorio y vuelve a ejecutar esto antes de subir nada.")
        return 1
    if a.push:
        if "origin" not in git("remote", cwd=a.dir, capture=True).split():
            sys.exit("✗ no existe %s: haz el fork de github-linguist/linguist en GitHub y vuelve a ejecutar" % fork)
        git("push", "-f", "-u", "origin", RAMA, cwd=a.dir)
        print("\n✓ Subido. Abre la pull request (con el texto de editors/linguist/PULL_REQUEST.md y las cifras del día):")
        print("  https://github.com/github-linguist/linguist/compare/main...%s:linguist:%s?expand=1" % (a.usuario, RAMA))
    else:
        print("\nListo en local. Para subirlo a tu fork: python tools/linguist_pr.py --push")
    print("Las pruebas de Linguist (bundle exec rake test) se ejecutan solas en la pull request; las que dependen de\n"
          "HyperEZ ya las comprueba aquí ctest -R linguist.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
