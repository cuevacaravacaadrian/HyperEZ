import os
import re
import sys

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC = os.path.join(ROOT, "tools", "lpo", "api.md")
OUT_LIB = os.path.join(ROOT, "src", "lib", "lpo.hz")

RESERVED = {"var", "let", "const", "function", "return", "if", "else", "for", "foreach", "in", "while", "repeat", "break",
            "continue", "class", "struct", "constructor", "this", "super", "extends", "implements", "interface", "enum",
            "import", "public", "private", "protected", "static", "true", "false", "null", "and", "or", "not", "is", "new",
            "try", "catch", "finally", "throw", "async", "await", "match"}
SIMPLE_TYPES = {"number", "text", "bool", "any", "list", "map", "Vec2", "Vec3", "Color", "function", "Task"}

MEMBER = re.compile(r"^- \*\*(\w+)\*\*(?:\((.*?)\))?: (.+?) \*\((property|method|event|function)(, read-only)?\)\* — (.*)$")
GLOBAL_OBJ = re.compile(r"^- `(\w+)` — (.*)$")
GLOBAL_VAR = re.compile(r"^- `(\w+)`: (\w+) — (.*)$")
ENUM = re.compile(r"^- \*\*(\w+)\*\*: (.*?) — (.*)$")


class Member:
    def __init__(self, name, params, type_, kind, readonly, desc):
        self.name, self.params, self.type, self.kind, self.readonly, self.desc = name, params, type_, kind, readonly, desc


class Section:
    def __init__(self, name):
        self.name = name
        self.desc = ""
        self.parent = None
        self.area = ""
        self.members = []


def parse():
    text = open(SPEC, encoding="utf-8").read().replace("\r\n", "\n")
    singletons, classes, enums, globals_obj, globals_var = [], [], [], [], []
    part = None
    cur = None
    for line in text.split("\n"):
        if line.startswith("## "):
            title = line[3:].strip()
            if title == "Globals":
                part = "globals"
            elif title == "Classes":
                part = "classes"
            elif title.startswith("Enumerations"):
                part = "enums"
            else:
                part = "singleton"
                cur = Section(title)
                singletons.append(cur)
            continue
        if line.startswith("### ") and part == "classes":
            cur = Section(line[4:].strip())
            classes.append(cur)
            continue
        if part == "globals":
            m = GLOBAL_VAR.match(line)
            if m:
                globals_var.append(m.groups())
                continue
            m = GLOBAL_OBJ.match(line)
            if m:
                globals_obj.append(m.groups())
            continue
        if part == "enums":
            m = ENUM.match(line)
            if m:
                enums.append((m.group(1), re.findall(r"`(\w+)`", m.group(2)), m.group(3)))
            continue
        if cur is None:
            continue
        m = MEMBER.match(line)
        if m:
            name, params, type_, kind, ro, desc = m.groups()
            cur.members.append(Member(name, params, type_.strip(), kind, bool(ro), desc.strip()))
            continue
        m = re.match(r"^Inherits from \*\*(\w+)\*\*\. Area: ([^.]*)\.", line)
        if m:
            cur.parent, cur.area = m.group(1), m.group(2)
            continue
        m = re.match(r"^Area: ([^.]*)\.", line)
        if m:
            cur.area = m.group(1)
            continue
        if line.strip() and not line.startswith("-") and not cur.desc and not line.startswith("Generated"):
            cur.desc = line.strip()
    return singletons, classes, enums, globals_obj, globals_var


def hz_type(t):
    t = t.strip()
    nullable = t.endswith("?")
    base = t.rstrip("?")
    if base in SIMPLE_TYPES:
        return base + ("?" if nullable and base != "any" else "")
    return "any"


def default_for(t, desc=""):
    base = t.strip().rstrip("?")
    if t.strip().endswith("?"):
        return "null"
    if base == "number":
        m = re.search(r"\(([-\d.]+) by default\)", desc)
        return m.group(1) if m else "0"
    return {"text": '""', "bool": "false", "Vec2": "Vec2(0, 0)", "Vec3": "Vec3(0, 0, 0)", "Color": "Color(255, 255, 255)",
            "list": "[]", "map": "{}"}.get(base, "null")


def split_params(p):
    out, depth, cur = [], 0, ""
    for c in p:
        if c in "([{":
            depth += 1
        elif c in ")]}":
            depth -= 1
        if c == "," and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += c
    if cur.strip():
        out.append(cur.strip())
    return out


def hz_params(p):
    res = []
    for item in split_params(p or ""):
        m = re.match(r"^(\.\.\.)?(\w+)(\?)?\s*:\s*([\w?]+)(?:\s*=\s*(.+))?$", item)
        if not m:
            continue
        rest, name, opt, t, default = m.groups()
        if name in RESERVED:
            name += "_"
        if rest:
            res.append(f"...{name}: any")
        elif default is not None:
            res.append(f"{name}: {hz_type(t)} = {default.strip()}")
        elif opt:
            res.append(f"{name}: any = null")
        else:
            res.append(f"{name}: {hz_type(t)}")
    return ", ".join(res)


def event_fields(m):
    if m.params is not None:
        return [f for f in split_params(m.params) if f]
    d = re.search(r"Data: (.*?)\.?$", m.desc)
    if not d:
        return []
    return [f.strip() for f in split_params(d.group(1))]


def event_decl(m, static=False):
    fields = []
    for f in event_fields(m):
        mm = re.match(r"^(\w+)\s*:\s*([\w?]+)", f)
        if mm:
            fields.append(f"{mm.group(1)}: {hz_type(mm.group(2))}")
    return f"{'static ' if static else ''}event {m.name}({', '.join(fields)})"


def doc(desc, indent):
    desc = re.sub(r"\s*Data: .*$", "", desc).strip()
    return f"{indent}/// {desc}\n" if desc else ""


def return_stmt(t):
    base = t.strip().rstrip("?")
    if base == "void":
        return ""
    if base == "Task":
        return "return wait(0)"
    return "return " + default_for(t)


INSTANCE = '''/// Objeto base de la jerarquía de LPO Engine: todo lo que hay en un juego es una instancia.
class Instance {
    /// Nombre de la instancia.
    var name: text = ""
    private var _parent: any = null
    private var _children: list = []
    private var _attributes: map = {}
    private var _destroyed: bool = false
    /// Se añadió un hijo directo.
    event childAdded(child: any)
    /// Se quitó un hijo directo.
    event childRemoved(child: any)
    /// Cambió una propiedad (recibe su nombre).
    event changed(property: text)
    /// La instancia va a destruirse.
    event destroying()

    constructor(parent: any = null) {
        name = typeof(this)
        if parent != null { this.parent = parent }
    }

    /// Nombre de la clase.
    get className(): text { return typeof(this) }

    /// Padre (asigna otra instancia para moverla; null para sacarla del juego).
    get parent(): any { return _parent }
    set parent(nuevo: any) {
        if nuevo == _parent { return }
        if _destroyed { throw Error("${name}: la instancia está destruida") }
        if nuevo != null and (nuevo == this or nuevo.isDescendantOf(this)) { throw Error("${name}: no puede ser hija de sí misma") }
        var anterior = _parent
        _parent = nuevo
        if anterior != null { anterior._quitarHijo(this) }
        if nuevo != null { nuevo._ponerHijo(this) }
        emit changed("parent")
    }

    fn _ponerHijo(hijo: any) {
        _children.add(hijo)
        emit childAdded(hijo)
    }

    fn _quitarHijo(hijo: any) {
        _children.remove(hijo)
        emit childRemoved(hijo)
    }

    /// Hijo directo con ese nombre (o null).
    fn find(name: text): any { return _children.find(c => c.name == name) }

    /// Primer descendiente con ese nombre (o null).
    fn findDescendant(name: text): any {
        foreach c in _children {
            if c.name == name { return c }
            var d = c.findDescendant(name)
            if d != null { return d }
        }
        return null
    }

    /// Primer hijo de esa clase (o null).
    fn findChildOfClass(className: text): any { return _children.find(c => c.isA(className)) }

    /// Primer antepasado de esa clase (o null).
    fn findAncestorOfClass(className: text): any {
        var p = _parent
        while p != null {
            if p.isA(className) { return p }
            p = p.parent
        }
        return null
    }

    /// Tarea que termina cuando existe el hijo (úsala con await). Devuelve null si se acaba el tiempo.
    async fn waitForChild(name: text, timeout: number = 10): any {
        var inicio = time()
        loop {
            var c = find(name)
            if c != null { return c }
            if time() - inicio >= timeout { return null }
            await nextFrame()
        }
    }

    /// Lista de los hijos directos.
    fn children(): list { return _children.copy() }

    /// Lista de todos los descendientes.
    fn descendants(): list {
        var todos = []
        foreach c in _children {
            todos.add(c)
            todos.add(...c.descendants())
        }
        return todos
    }

    /// ¿Es de esa clase o de una derivada?
    fn isA(className: text): bool { return _lpoIsA(this, className) }

    /// ¿Está dentro de 'other'?
    fn isDescendantOf(other: any): bool {
        var p = _parent
        while p != null {
            if p == other { return true }
            p = p.parent
        }
        return false
    }

    /// Copia (sin padre), con sus hijos y atributos.
    fn clone(): any {
        var copia = _lpoCreate(className)
        copia.name = name
        foreach k in _attributes.keys() { copia.setAttribute(k, _attributes[k]) }
        foreach c in _children { c.clone().parent = copia }
        return copia
    }

    /// Destruye la instancia y sus hijos.
    fn destroy() {
        if _destroyed { return }
        emit destroying()
        clearChildren()
        parent = null
        _destroyed = true
    }

    /// Destruye todos los hijos.
    fn clearChildren() {
        foreach c in _children.copy() { c.destroy() }
    }

    /// Atributo personalizado (o null).
    fn getAttribute(name: text): any { return _attributes.get(name) }

    /// Guarda un atributo personalizado.
    fn setAttribute(name: text, value: any) {
        _attributes[name] = value
        emit changed(name)
    }

    /// Ruta completa: Workspace.Model.Part.
    fn getFullName(): text {
        var partes = [name]
        var p = _parent
        while p != null and p.className != "DataModel" {
            partes.insert(0, p.name)
            p = p.parent
        }
        return partes.join(".")
    }

    /// Crea una instancia a partir del nombre de su clase.
    fn create(className: text, parent: any = null): any {
        var nueva = _lpoCreate(className)
        if parent != null { nueva.parent = parent }
        return nueva
    }

    fn toString(): text { return name }
}
'''

DEFAULTS = {
    ("Humanoid", "health"): "100", ("Humanoid", "maxHealth"): "100", ("Humanoid", "walkSpeed"): "16",
    ("Humanoid", "jumpPower"): "50", ("Players", "maxPlayers"): "12", ("Players", "respawnTime"): "5",
    ("Players", "characterAutoLoads"): "true", ("Sound", "volume"): "0.5", ("Sound", "playbackSpeed"): "1",
    ("ScreenGui", "enabled"): "true", ("Script", "enabled"): "true", ("LocalScript", "enabled"): "true",
    ("ClickDetector", "maxActivationDistance"): "32",
}

OVERRIDES = {
    ("DataModel", "getService"): "    fn getService(name: text): any { return find(name) }",
    ("Players", "getPlayers"): "    fn getPlayers(): list { return children().filter(c => c.isA(\"Player\")) }",
    ("Players", "playerFromCharacter"): "    fn playerFromCharacter(character: any): any { return getPlayers().find(p => p.character == character) }",
    ("Humanoid", "takeDamage"): """    fn takeDamage(amount: number) {
        if health <= 0 { return }
        health = max(0, health - amount)
        emit healthChanged(health)
        if health == 0 { emit died() }
    }""",
    ("Humanoid", "moveTo"): "    fn moveTo(position: Vec3) { parent?.setAttribute(\"moveTarget\", position) }",
    ("RemoteEvent", "fireServer"): "    fn fireServer(value: any = null) { emit onServerEvent(Players.current?.localPlayer, value) }",
    ("RemoteEvent", "fireClient"): "    fn fireClient(player: any, value: any = null) { emit onClientEvent(value) }",
    ("RemoteEvent", "fireAllClients"): "    fn fireAllClients(value: any = null) { emit onClientEvent(value) }",
    ("Sound", "play"): "    fn play() { playing = true }",
    ("Sound", "stop"): "    fn stop() { playing = false }",
    ("Sound", "pause"): "    fn pause() { playing = false }",
}

EXTRA = {
    "Players": '''
    static var current: any = null

    /// Simulación: entra un jugador nuevo (lanza playerAdded) y lo devuelve. El primero es el jugador local.
    fn join(name: text): any {
        var p = Player(this)
        p.name = name
        p.displayName = name
        p.userId = len(getPlayers())
        if localPlayer == null { localPlayer = p }
        emit playerAdded(p)
        return p
    }

    /// Simulación: un jugador se va (lanza playerRemoving).
    fn leave(player: any) {
        emit playerRemoving(player)
        player.destroy()
    }
''',
    "BasePart": '''
    /// Simulación: otra pieza empieza a tocar esta (lanza touched).
    fn simulateTouch(other: any) { emit touched(other) }
''',
    "Sprite2D": '''
    /// Simulación: otro objeto 2D empieza a tocar este (lanza touched).
    fn simulateTouch(other: any) { emit touched(other) }
''',
    "ClickDetector": '''
    /// Simulación: un jugador hace clic en la pieza (lanza mouseClick).
    fn simulateClick(player: any = null) { emit mouseClick(player) }
''',
    "TextButton": '''
    /// Simulación: se pulsa el botón (lanza activated).
    fn simulateActivate() { emit activated() }
''',
    "ImageButton": '''
    /// Simulación: se pulsa el botón (lanza activated).
    fn simulateActivate() { emit activated() }
''',
}

SINGLETON_CODE = {
    "Game": '''    /// Simulación fuera del motor: ejecuta el bucle del juego durante unos segundos, lanzando update en cada fotograma.
    static async fn run(seconds: number = 1, fps: number = 60) {
        var dt = 1 / fps
        var fin = time + seconds
        while time < fin {
            await wait(dt)
            time += dt
            emit update(dt)
        }
    }
''',
    "Input": '''    private static var _keys: set = set()
    private static var _buttons: set = set()

    /// Simulación: pulsa una tecla (lanza keyDown).
    static fn press(key: text) {
        _keys.add(key)
        emit keyDown(key)
    }

    /// Simulación: suelta una tecla (lanza keyUp).
    static fn release(key: text) {
        _keys.remove(key)
        emit keyUp(key)
    }

    /// Simulación: hace clic con un botón del ratón (lanza mouseDown y mouseUp).
    static fn click(button: number = 1, position: Vec2 = Vec2(0, 0)) {
        mousePosition = position
        emit mouseDown(button, position)
        emit mouseUp(button, position)
    }
''',
}

SINGLETON_OVERRIDES = {
    ("Input", "isKeyDown"): "    static fn isKeyDown(key: text): bool { return _keys.contains(key) }",
    ("Input", "isMouseDown"): "    static fn isMouseDown(button: number = 1): bool { return _buttons.contains(button) }",
    ("Tween", "to"): '''    static async fn to(target: any, props: map, duration: number, easing: text = "quadOut", delay: number = 0): any {
        if delay > 0 { await wait(delay) }
        var desde = {}
        foreach k in props.keys() { desde[k] = target[k] }
        var t = 0
        while t < duration {
            await wait(1 / 60)
            t = min(duration, t + 1 / 60)
            var f = _lpoEase(easing, duration <= 0 ? 1 : t / duration)
            foreach k in props.keys() { target[k] = _lpoLerp(desde[k], props[k], f) }
        }
        foreach k in props.keys() { target[k] = props[k] }
        return target
    }''',
    ("Debris", "add"): "    static fn add(instance: any, seconds: number = 5) { delay(seconds, () => instance.destroy()) }",
    ("DataStore", "get"): "    static fn get(key: text, default_: any = null): any { return _data.get(key, default_) }",
    ("DataStore", "set"): "    static fn set(key: text, value: any) { _data[key] = value }",
    ("DataStore", "remove"): "    static fn remove(key: text) { _data.remove(key) }",
    ("DataStore", "keys"): "    static fn keys(): list { return _data.keys() }",
    ("Assets", "readText"): "    static fn readText(name: text): text { return File.read(Path.join(folder, name)) }",
    ("Assets", "readJson"): "    static fn readJson(name: text): any { return JSON.parse(readText(name)) }",
    ("Assets", "readCsv"): "    static fn readCsv(name: text): list { return readText(name).lines().filter(l => l.trim() != \"\").map(l => l.split(\",\")) }",
    ("Assets", "exists"): "    static fn exists(name: text): bool { return File.exists(Path.join(folder, name)) }",
    ("World2D", "find"): "    static fn find(name: text): any { return workspace2D.findDescendant(name) }",
    ("World2D", "findAll"): "    static fn findAll(nameOrClass: text): list { return workspace2D.descendants().filter(d => d.name == nameOrClass or d.isA(nameOrClass)) }",
    ("World2D", "spawn"): '''    static fn spawn(template: any, position: any = null, parent: any = null): any {
        var copia = template.clone()
        copia.parent = parent ?? workspace2D
        if position != null { copia.position = position }
        return copia
    }''',
    ("World2D", "distance"): "    static fn distance(a: any, b: any): number { return (_lpoPoint(a) - _lpoPoint(b)).length() }",
    ("World2D", "direction"): "    static fn direction(from_: any, to: any): Vec2 { return (_lpoPoint(to) - _lpoPoint(from_)).normalized() }",
    ("Timer", "after"): '''    static fn after(seconds: number, fn_: function): number {
        var id = _next++
        _tasks[id] = delay(seconds, fn_)
        return id
    }''',
    ("Timer", "every"): '''    static fn every(seconds: number, fn_: function, times: any = null): number {
        var id = _next++
        _tasks[id] = spawn(async () => {
            var n = 0
            while times == null or n < times {
                await wait(seconds)
                fn_()
                n++
            }
        })
        return id
    }''',
    ("Timer", "cancel"): '''    static fn cancel(id: number) {
        var t = _tasks.get(id)
        if t != null { t.cancel() }
        _tasks.remove(id)
    }''',
}

SINGLETON_FIELDS = {
    "DataStore": "    private static var _data: map = {}\n",
    "Assets": "    /// Simulación: carpeta donde se buscan los recursos.\n    static var folder: text = \"assets\"\n",
    "Timer": "    private static var _next: number = 1\n    private static var _tasks: map = {}\n",
}

HELPERS = '''fn _lpoIsA(obj: any, className: text): bool {
    var c = obj.className
    while c != null {
        if c == className { return true }
        c = _LPO_PARENTS.get(c)
    }
    return false
}

fn _lpoEase(name: text, t: number): number {
    return match name {
        "linear" => t
        "quadIn" => t * t
        "quadOut" => 1 - (1 - t) * (1 - t)
        "quadInOut" => t < 0.5 ? 2 * t * t : 1 - (-2 * t + 2) ** 2 / 2
        "cubicOut" => 1 - (1 - t) ** 3
        "sineInOut" => -(cos(PI * t) - 1) / 2
        "backOut" => 1 + 2.70158 * (t - 1) ** 3 + 1.70158 * (t - 1) ** 2
        "bounceOut" => _lpoBounce(t)
        "elasticOut" => t == 0 or t == 1 ? t : 2 ** (-10 * t) * sin((t * 10 - 0.75) * (2 * PI / 3)) + 1
        else => t
    }
}

fn _lpoBounce(t: number): number {
    if t < 1 / 2.75 { return 7.5625 * t * t }
    if t < 2 / 2.75 { var u = t - 1.5 / 2.75; return 7.5625 * u * u + 0.75 }
    if t < 2.5 / 2.75 { var u = t - 2.25 / 2.75; return 7.5625 * u * u + 0.9375 }
    var u = t - 2.625 / 2.75
    return 7.5625 * u * u + 0.984375
}

fn _lpoLerp(a: any, b: any, f: number): any {
    if a is number and b is number { return a + (b - a) * f }
    if a is Color and b is Color {
        return Color(round(a.r + (b.r - a.r) * f), round(a.g + (b.g - a.g) * f), round(a.b + (b.b - a.b) * f), round(a.a + (b.a - a.a) * f))
    }
    if (a is Vec2 and b is Vec2) or (a is Vec3 and b is Vec3) { return a + (b - a) * f }
    return f < 1 ? a : b
}

fn _lpoPoint(p: any): any { return p is Vec2 or p is Vec3 ? p : p.position }
'''


def method_line(m, static=False):
    ps = hz_params(m.params)
    ret = hz_type(m.type) if m.type.strip() != "void" else "void"
    r = return_stmt(m.type)
    head = f"    {'static ' if static else ''}fn {m.name}({ps}): {ret}"
    return head + (f" {{ {r} }}" if r else " {}")


def main():
    singletons, classes, enums, globals_obj, globals_var = parse()
    by_name = {c.name: c for c in classes}
    full = {c.name: {m.name for m in c.members} for c in classes}

    order, seen = [], set()

    def visit(c):
        if c.name in seen:
            return
        seen.add(c.name)
        if c.parent and c.parent in by_name:
            visit(by_name[c.parent])
        order.append(c)

    for c in classes:
        visit(c)

    out = ["/// LPO Engine para HyperEZ: todas las clases, servicios y objetos globales del motor.",
           "/// Fuera del motor funciona como simulación sin gráficos: sirve para probar la lógica de un juego con hyper test.",
           "", HELPERS, INSTANCE]
    parents = {}
    for c in order:
        if c.name == "Instance":
            continue
        parents[c.name] = c.parent or "Instance"
        inherited = full.get(c.parent or "Instance", set())
        lines = [doc(c.desc, "").rstrip("\n"), f"class {c.name} extends {c.parent or 'Instance'} {{"]
        body = []
        for m in c.members:
            if m.name in inherited or m.name in RESERVED:
                continue
            if c.name == "DataModel" and m.kind == "property":
                continue
            if (c.name, m.name) in OVERRIDES:
                body.append(doc(m.desc, "    ") + OVERRIDES[(c.name, m.name)])
            elif m.kind == "property":
                value = DEFAULTS.get((c.name, m.name), default_for(m.type, m.desc))
                body.append(doc(m.desc, "    ") + f"    var {m.name}: {hz_type(m.type)} = {value}")
            elif m.kind == "event":
                body.append(doc(m.desc, "    ") + "    " + event_decl(m))
            else:
                body.append(doc(m.desc, "    ") + method_line(m))
        if c.name == "DataModel":
            services = [m for m in c.members if m.kind == "property" and m.readonly and m.name not in full["Instance"]]
            for m in services:
                body.append(doc(m.desc, "    ") + f"    var {m.name}: any = null")
            ctor = ["    constructor() {", "        super(null)", '        name = "Game"']
            for m in services:
                ctor.append(f"        {m.name} = {m.type}(this)")
            ctor.append("        Players.current = players")
            ctor.append("    }")
            body.append("\n".join(ctor))
        if c.name in EXTRA:
            body.append(EXTRA[c.name].strip("\n"))
        lines.append("\n\n".join(b.rstrip("\n") for b in body))
        lines.append("}")
        out.append("\n".join(l for l in lines if l != "") + "\n")

    for s in singletons:
        sdesc = next((d for n, d in globals_obj if n == s.name), "")
        lines = [doc(sdesc, "").rstrip("\n"), f"class {s.name} {{"]
        body = []
        if s.name in SINGLETON_FIELDS:
            body.append(SINGLETON_FIELDS[s.name].rstrip("\n"))
        for m in s.members:
            if (s.name, m.name) in SINGLETON_OVERRIDES:
                body.append(doc(m.desc, "    ") + SINGLETON_OVERRIDES[(s.name, m.name)])
            elif m.name in RESERVED:
                continue
            elif m.kind == "property":
                body.append(doc(m.desc, "    ") + f"    static var {m.name}: {hz_type(m.type)} = {default_for(m.type, m.desc)}")
            elif m.kind == "event":
                body.append(doc(m.desc, "    ") + "    " + event_decl(m, static=True))
            else:
                body.append(doc(m.desc, "    ") + method_line(m, static=True))
        if s.name in SINGLETON_CODE:
            body.append(SINGLETON_CODE[s.name].rstrip("\n"))
        lines.append("\n\n".join(b.rstrip("\n") for b in body))
        lines.append("}")
        out.append("\n".join(l for l in lines if l != "") + "\n")

    for name, values, desc in enums:
        items = ", ".join(f"{v}: \"{v}\"" for v in values)
        out.append(doc(desc, "") + f"const {name} = {{ {items} }}\n")

    out.append("const _LPO_PARENTS = {\n" + ",\n".join(f'    {k}: "{v}"' for k, v in parents.items()) + "\n}\n")
    creators = ",\n".join(f"        \"{c.name}\" => {c.name}()" for c in order if c.name not in ("Instance", "DataModel"))
    out.append("fn _lpoCreate(className: text): any {\n    return match className {\n" + creators +
               ",\n        else => { throw Error(\"LPO Engine no tiene la clase '${className}'\") }\n    }\n}\n")
    gdesc = {n: d for n, t, d in globals_var}
    out.append(doc(gdesc.get("game", "El juego."), "") + "var game = DataModel()")
    out.append(doc(gdesc.get("workspace", "El mundo 3D."), "") + "var workspace = game.workspace")
    out.append(doc(gdesc.get("workspace2D", "El mundo 2D."), "") + "var workspace2D = game.workspace2D")
    out.append("/// El script que se está ejecutando.\nvar script = Script(game.serverScriptService)\n")
    text = "\n".join(out).replace("\n\n\n", "\n\n")
    with open(OUT_LIB, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("  " + os.path.relpath(OUT_LIB, ROOT) + f" ({len(order)} clases, {len(singletons)} servicios globales, {len(enums)} enumeraciones)")
    write_reference(singletons, order, enums, globals_obj, globals_var, full)


KINDS = {"property": "propiedad", "method": "método", "event": "evento", "function": "función"}


def ref_rows(members, skip=()):
    rows = ["| Miembro | Tipo | Descripción |", "|---|---|---|"]
    for m in members:
        if m.name in skip:
            continue
        sig = f"`{m.name}({m.params})`" if m.params is not None else f"`{m.name}`"
        kind = KINDS.get(m.kind, m.kind) + (", solo lectura" if m.readonly else "")
        desc = m.desc.replace("|", "\\|")
        rows.append(f"| {sig} | {kind}: `{m.type}` | {desc} |")
    return rows


def write_reference(singletons, order, enums, globals_obj, globals_var, full):
    out = ["# Referencia de LPO Engine", "",
           "Todas las clases, servicios y enumeraciones de la biblioteca `lpo` ([guía](lpo-engine.md)). "
           "Se genera con `python tools/gen_lpo.py` a partir de la API del motor; las descripciones vienen del propio motor.", "",
           "## Objetos globales", "", "| Nombre | Descripción |", "|---|---|"]
    for n, d in globals_obj:
        out.append(f"| [`{n}`](#{n.lower()}) | {d} |")
    for n, t, d in globals_var:
        out.append(f"| `{n}` | {t}: {d} |")
    for s in singletons:
        out += ["", f"## {s.name}", ""] + ref_rows(s.members)
    out += ["", "## Clases", ""]
    out.append(", ".join(f"[{c.name}](#{c.name.lower()})" for c in order))
    for c in order:
        inherited = full.get(c.parent, set()) if c.parent else set()
        head = c.desc + (f" Hereda de [{c.parent}](#{c.parent.lower()})." if c.parent else "")
        out += ["", f"### {c.name}", "", head.strip(), ""] + ref_rows(c.members, inherited)
    out += ["", "## Enumeraciones", "", "| Nombre | Valores | Descripción |", "|---|---|---|"]
    for n, vals, d in enums:
        out.append(f"| `{n}` | {', '.join('`' + v + '`' for v in vals)} | {d} |")
    path = os.path.join(ROOT, "docs", "biblioteca", "lpo-engine-api.md")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out) + "\n")
    print("  " + os.path.relpath(path, ROOT))


if __name__ == "__main__":
    main()
