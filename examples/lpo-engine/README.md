# Un juego de LPO Engine

Este juego tiene la misma estructura que uno de LPO Engine: cada carpeta es un servicio del motor y cada archivo, un script. Funciona en el motor y también con `hyper`, que simula el juego sin gráficos.

| Archivo | Tipo | Qué hace |
|---|---|---|
| [`ReplicatedStorage/Config.module.hz`](ReplicatedStorage/Config.module.hz) | `ModuleScript` | constantes y reglas compartidas |
| [`ServerScriptService/Lava.server.hz`](ServerScriptService/Lava.server.hz) | `Script` | la lava quita vida al tocarla (`touched`, `Humanoid`) |
| [`ServerScriptService/Marcador.server.hz`](ServerScriptService/Marcador.server.hz) | `Script` | marcador de monedas por jugador guardado en `DataStore` |
| [`ServerScriptService/Puerta.server.hz`](ServerScriptService/Puerta.server.hz) | `Script` | una puerta que se abre con un clic y una animación `Tween` |
| [`StarterPlayerScripts/Controles.client.hz`](StarterPlayerScripts/Controles.client.hz) | `LocalScript` | teclado, bucle `Game.update` y un `RemoteEvent` hacia el servidor |
| [`Workspace2D/Monedas.server.hz`](Workspace2D/Monedas.server.hz) | `Script` | monedas 2D con `World2D` y `Timer` |

```text
hyper run ServerScriptService/Lava.server.hz
hyper test .
```

Los scripts no importan nada: los archivos `.server.hz`, `.client.hz` y `.module.hz` reciben automáticamente todo LPO Engine. Más en la [guía de LPO Engine](../../docs/biblioteca/lpo-engine.md).
