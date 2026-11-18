# LPO Engine

**LPO Engine** es el motor de juegos 2D y 3D de LPO Studios, y su lenguaje de lógica es **HyperEZ completo**: todo lo que explica esta documentación funciona en los scripts del motor. Además, HyperEZ trae de serie la biblioteca **`lpo`**, con todas las clases, servicios y objetos globales del motor, para escribir, comprobar y probar los scripts de un juego fuera de él.

## Scripts del motor

Un juego de LPO Engine se organiza como un árbol de servicios. Cada script es un archivo HyperEZ y su nombre dice dónde se ejecuta:

| Archivo | Clase en el motor | Se ejecuta en | Dónde va |
|---|---|---|---|
| `Nombre.server.hz` | `Script` | el servidor | `ServerScriptService`, `Workspace`, `Workspace2D` |
| `Nombre.client.hz` | `LocalScript` | el jugador | `StarterPlayerScripts`, `StarterGui`, `StarterCharacterScripts` |
| `Nombre.module.hz` | `ModuleScript` | donde se importe | `ReplicatedStorage` |

En estos archivos **no hace falta importar nada**: `hyper`, el servidor de lenguaje y VS Code les dan automáticamente todo lo de `lpo` (`game`, `workspace`, `workspace2D`, `script`, `Game`, `Input`, `Tween`, `Debris`, `DataStore`, `Assets`, `World2D`, `Timer`, las 78 clases y las enumeraciones). Un módulo se importa por su ruta en el juego:

```text
import ReplicatedStorage.Config
```

En cualquier otro archivo se usa como cualquier biblioteca: `from lpo import *` o `import lpo`.

## Lo esencial

Los objetos se crean con el nombre de su clase y su padre, y se buscan por nombre:

```hz
from lpo import *

var puerta = Part(workspace)
puerta.name = "Puerta"
puerta.size = Vec3(4, 10, 1)
puerta.color = Color(120, 80, 40)
puerta.material = Material.Wood

var luz = PointLight(puerta)
luz.range = 20

print(workspace.find("Puerta").getFullName())
print(puerta.isA("BasePart"), len(puerta.children()))
```

Cada objeto tiene sus **eventos**, que se escuchan con `on objeto.evento as e { }`:

```hz
from lpo import *

var lava = Part(workspace)
var personaje = Model(workspace)
var humanoid = Humanoid(personaje)
var pie = Part(personaje)

on lava.touched as e {
    e.other.parent?.findChildOfClass("Humanoid")?.takeDamage(25)
}
on humanoid.died as e { print("¡Fuera!") }

repeat 4 { lava.simulateTouch(pie) }
print(humanoid.health)
```

Animaciones con `Tween` (curvas `linear`, `quadIn`, `quadOut`, `quadInOut`, `cubicOut`, `sineInOut`, `backOut`, `bounceOut`, `elasticOut`), temporizadores con `Timer` y datos que se guardan entre partidas con `DataStore`:

```hz
from lpo import *

var ascensor = Part(workspace)
await Tween.to(ascensor, {position: Vec3(0, 15, 0)}, 0.2, "sineInOut")
print(ascensor.position)

DataStore.set("record", 120)
print(DataStore.get("record", 0))
```

## Probar un juego sin abrir el motor

Fuera de LPO Engine, `lpo` es una **simulación sin gráficos**: la jerarquía, los eventos, `Tween`, `Timer`, `DataStore`, `Input` y los jugadores funcionan de verdad, y la física y el dibujo no. Para provocar lo que en el motor hace el jugador hay funciones de simulación:

| Simulación | Qué hace |
|---|---|
| `game.players.join(nombre)` / `leave(jugador)` | entra o sale un jugador (`playerAdded`, `playerRemoving`); el primero es `localPlayer` |
| `pieza.simulateTouch(otra)` | `touched` en una `BasePart` o un `Sprite2D` |
| `detector.simulateClick(jugador)` | `mouseClick` de un `ClickDetector` |
| `boton.simulateActivate()` | `activated` de un `TextButton` o `ImageButton` |
| `Input.press(tecla)`, `Input.release(tecla)`, `Input.click()` | teclado y ratón |
| `await Game.run(segundos, fps)` | el bucle del juego: lanza `Game.update` en cada fotograma |
| `Assets.folder` | carpeta donde `Assets` busca los recursos (`assets` por defecto) |

Así se prueba la lógica de un juego con `hyper test`:

```hz
from lpo import *

test("la lava quita 25 de vida", () => {
    var lava = Part(workspace)
    on lava.touched as e { e.other.parent?.findChildOfClass("Humanoid")?.takeDamage(25) }
    var personaje = Model(workspace)
    var humanoid = Humanoid(personaje)
    lava.simulateTouch(Part(personaje))
    assertEqual(humanoid.health, 75)
})
```

## Ejemplos

En [`examples/lpo-engine`](../../examples/lpo-engine) hay un juego completo con la estructura del motor: lava que quita vida, un marcador con monedas guardadas en `DataStore`, una puerta que se abre al hacer clic, controles de un `LocalScript` que hablan con el servidor por un `RemoteEvent` y monedas 2D con `World2D` y `Timer`.

## Referencia

Todas las clases, propiedades, métodos y eventos están en la [referencia de LPO Engine](lpo-engine-api.md) y aparecen al pasar el ratón y en el autocompletado de VS Code. La biblioteca se genera a partir de la API del motor con `python tools/gen_lpo.py` (`tools/lpo/api.md`).
