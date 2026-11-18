# Referencia de LPO Engine

Todas las clases, servicios y enumeraciones de la biblioteca `lpo` ([guía](lpo-engine.md)). Se genera con `python tools/gen_lpo.py` a partir de la API del motor; las descripciones vienen del propio motor.

## Objetos globales

| Nombre | Descripción |
|---|---|
| [`Game`](#game) | The running game: time, side (server/client) and the update event of every frame. |
| [`Input`](#input) | (Client) The player's keyboard, mouse and gamepad. |
| [`Tween`](#tween) | Tweens: animate number, Vec2, Vec3 and Color properties. |
| [`Debris`](#debris) | Destroys objects after a while. |
| [`DataStore`](#datastore) | (Server) Data kept between sessions (scores, inventories...). |
| [`Assets`](#assets) | Game assets: reads imported text and data (JSON, CSV, dialogues, levels). |
| [`World2D`](#world2d) | Helpers for 2D games: find and create objects, floating text, particles, shake, slow motion, hit freeze, flashes, fades and zone queries. |
| [`Timer`](#timer) | Timers: call a function after a while or every so often (game time). |
| `game` | DataModel: The game (root of everything). |
| `workspace` | Workspace: The 3D world. |
| `workspace2D` | Workspace2D: The 2D world. |

## Game

| Miembro | Tipo | Descripción |
|---|---|---|
| `time` | propiedad: `number` | Game seconds since it started. |
| `isServer` | propiedad: `bool` | Does this script run on the server? |
| `isClient` | propiedad: `bool` | Does this script run on a client? |
| `isStudio` | propiedad: `bool` | Is it being tested in LPO Engine? |
| `update(dt: number)` | evento: `void` | Every frame (dt = seconds since the previous one). |

## Input

| Miembro | Tipo | Descripción |
|---|---|---|
| `isKeyDown(key: text)` | función: `bool` | Is the key pressed? ("W", "Space", "Left", "LeftShift"...) |
| `isMouseDown(button: number = 1)` | función: `bool` | Is the mouse button pressed? (1 left, 2 middle, 3 right) |
| `mousePosition` | propiedad: `Vec2` | Mouse position in the game view (pixels). |
| `mouseDelta` | propiedad: `Vec2` | Mouse movement in this frame. |
| `viewSize` | propiedad: `Vec2` | Game view size (pixels). |
| `mouseHit` | propiedad: `Vec3` | 3D world point under the mouse. |
| `mouseTarget` | propiedad: `any` | Part under the mouse (or null). |
| `gamepadStick` | propiedad: `Vec2` | Left stick of the gamepad (-1..1). |
| `mouseWorld2D` | propiedad: `Vec2` | Mouse position in the 2D world (with the 2D camera). |
| `keyDown(key: text)` | evento: `void` | A key was pressed. |
| `keyUp(key: text)` | evento: `void` | A key was released. |
| `mouseDown(button: number, position: Vec2)` | evento: `void` | A mouse button was pressed. |
| `mouseUp(button: number, position: Vec2)` | evento: `void` | A mouse button was released. |
| `mouseWheel(delta: number)` | evento: `void` | The mouse wheel moved. |

## Tween

| Miembro | Tipo | Descripción |
|---|---|---|
| `to(target: any, props: map, duration: number, easing: text = "quadOut", delay: number = 0)` | función: `Task` | Animates the properties to the given values. Curves: linear, quadIn, quadOut, quadInOut, cubicOut, sineInOut, backOut, bounceOut, elasticOut. |

## Debris

| Miembro | Tipo | Descripción |
|---|---|---|
| `add(instance: any, seconds: number = 5)` | función: `void` | Destroys the instance after the given seconds. |

## DataStore

| Miembro | Tipo | Descripción |
|---|---|---|
| `get(key: text, default?: any)` | función: `any` | Stored value (or 'default'). |
| `set(key: text, value: any)` | función: `void` | Stores a value (numbers, text, lists, maps...). |
| `remove(key: text)` | función: `void` | Deletes a value. |
| `keys()` | función: `list` | Claves guardadas. |

## Assets

| Miembro | Tipo | Descripción |
|---|---|---|
| `readText(name: text)` | función: `text` | Contents of a text asset. |
| `readJson(name: text)` | función: `any` | Reads a JSON asset as maps and lists. |
| `readCsv(name: text)` | función: `list` | Reads a CSV table as a list of rows (each row a list of text). |
| `exists(name: text)` | función: `bool` | Does the asset exist? |
| `list(type?: text)` | función: `list` | Asset names (of one type: image, sound, text, font, mesh, song, spriteanim). |

## World2D

| Miembro | Tipo | Descripción |
|---|---|---|
| `find(name: text)` | función: `any` | The first object in the 2D world with that name (searches everywhere). |
| `findAll(nameOrClass: text)` | función: `list` | Every object in the 2D world with that name or of that class. |
| `spawn(template: any, position?: Vec2, parent?: any)` | función: `any` | Creates a copy of an object (for example kept in ReplicatedStorage) in the 2D world, at that position. |
| `popup(text: any, position: any, color?: Color, size: number = 12)` | función: `any` | Floating text that rises and fades (damage, points, notices). The position can be an object. |
| `burst(preset: text, position: any, count: number = 24)` | función: `any` | Particle burst from a ready-made effect (fire, smoke, sparks, explosion, magic, dust, confetti...) that clears itself. |
| `shake(intensity: number = 8, seconds: number = 0.35)` | función: `void` | Shakes the current 2D camera. |
| `hitStop(seconds: number = 0.08)` | función: `Task` | Freezes the 2D world for an instant: gives hits more impact. |
| `slowMotion(scale: number = 0.3, seconds: number = 1)` | función: `Task` | Slow motion for a few seconds and a smooth return to normal. |
| `flash(color?: Color, seconds: number = 0.25, amount: number = 0.75)` | función: `Task` | Full-screen flash. |
| `fadeOut(seconds: number = 0.6, color?: Color)` | función: `Task` | Fade to a colour (black if none is given). Use it with await. |
| `fadeIn(seconds: number = 0.6)` | función: `Task` | Returns from the fade. |
| `overlapCircle(center: any, radius: number)` | función: `list` | Sprites touching a circle (explosions, attack ranges). |
| `raycast(from: any, to: any, ignore?: any)` | función: `map?` | Ray from one point to another: {instance, position, normal, distance} of the first thing it hits, or null. |
| `distance(a: any, b: any)` | función: `number` | Distance between two objects or points. |
| `direction(from: any, to: any)` | función: `Vec2` | Direction (length 1) from one object or point to another. |
| `timeScale` | propiedad: `number` | 2D time speed (1 normal, 0.3 slow, 0 frozen). |
| `camera` | propiedad: `any` | The current Camera2D (or null). |
| `mouse` | propiedad: `Vec2` | Mouse position in the 2D world. |

## Timer

| Miembro | Tipo | Descripción |
|---|---|---|
| `after(seconds: number, fn: function)` | función: `number` | Calls the function once after the given seconds. Returns its number. |
| `every(seconds: number, fn: function, times?: number)` | función: `number` | Calls the function every few seconds (forever or 'times' times). Returns its number. |
| `cancel(id: number)` | función: `void` | Stops a timer. |

## Clases

[Instance](#instance), [DataModel](#datamodel), [Workspace](#workspace), [Workspace2D](#workspace2d), [Lighting](#lighting), [Players](#players), [Player](#player), [StarterPlayer](#starterplayer), [StarterPlayerScripts](#starterplayerscripts), [StarterCharacterScripts](#startercharacterscripts), [StarterGui](#startergui), [ReplicatedStorage](#replicatedstorage), [ServerScriptService](#serverscriptservice), [ServerStorage](#serverstorage), [SoundService](#soundservice), [Teams](#teams), [Folder](#folder), [Model](#model), [BasePart](#basepart), [Part](#part), [SpawnLocation](#spawnlocation), [MeshPart](#meshpart), [UnionOperation](#unionoperation), [Camera](#camera), [Light](#light), [PointLight](#pointlight), [SpotLight](#spotlight), [ParticleEmitter](#particleemitter), [WeldConstraint](#weldconstraint), [ClickDetector](#clickdetector), [Humanoid](#humanoid), [LuaSourceContainer](#luasourcecontainer), [Script](#script), [LocalScript](#localscript), [ModuleScript](#modulescript), [TouchScript](#touchscript), [ClickScript](#clickscript), [TimerScript](#timerscript), [PlayerScript](#playerscript), [GuiScript](#guiscript), [ButtonScript](#buttonscript), [ValueBase](#valuebase), [StringValue](#stringvalue), [NumberValue](#numbervalue), [BoolValue](#boolvalue), [Vector3Value](#vector3value), [ColorValue](#colorvalue), [ObjectValue](#objectvalue), [RemoteEvent](#remoteevent), [BindableEvent](#bindableevent), [Sound](#sound), [Animation](#animation), [Team](#team), [ScreenGui](#screengui), [GuiObject](#guiobject), [Frame](#frame), [TextLabel](#textlabel), [TextButton](#textbutton), [TextBox](#textbox), [ImageLabel](#imagelabel), [ImageButton](#imagebutton), [Node2D](#node2d), [Sprite2D](#sprite2d), [SpriteAnimator](#spriteanimator), [ParticleEmitter2D](#particleemitter2d), [Tilemap2D](#tilemap2d), [Camera2D](#camera2d), [Light2D](#light2d), [Layer2D](#layer2d), [Water2D](#water2d), [Background2D](#background2d), [Line2D](#line2d), [Trail2D](#trail2d), [Joint2D](#joint2d), [PlatformerController2D](#platformercontroller2d), [TopDownController2D](#topdowncontroller2d), [Text2D](#text2d), [Note](#note)

### Instance

Base object of the hierarchy. Everything in LPO Engine is an instance.

| Miembro | Tipo | Descripción |
|---|---|---|
| `name` | propiedad: `text` | Instance name. |
| `className` | propiedad, solo lectura: `text` | Class name. |
| `parent` | propiedad: `any` | Parent (assign another instance to move it; null to take it out of the game). |
| `childAdded` | evento: `Event` | A direct child was added. Data: child: any. |
| `childRemoved` | evento: `Event` | A direct child was removed. Data: child: any. |
| `changed` | evento: `Event` | A property changed (receives its name). Data: property: text. |
| `destroying` | evento: `Event` | La instancia va a destruirse. |
| `find(name: text)` | método: `any` | Direct child with that name (or null). |
| `findDescendant(name: text)` | método: `any` | First descendant with that name (or null). |
| `findChildOfClass(className: text)` | método: `any` | First child of that class (or null). |
| `findAncestorOfClass(className: text)` | método: `any` | First ancestor of that class (or null). |
| `waitForChild(name: text, timeout: number = 10)` | método: `Task` | Task that finishes when the child exists (use it with await). Returns null when the time runs out. |
| `children()` | método: `list` | List of the direct children. |
| `descendants()` | método: `list` | List of every descendant. |
| `isA(className: text)` | método: `bool` | Is it of that class or a derived one? |
| `isDescendantOf(other: any)` | método: `bool` | Is it inside 'other'? |
| `clone()` | método: `any` | Copy (no parent). |
| `destroy()` | método: `void` | Destroys the instance and its children. |
| `clearChildren()` | método: `void` | Destroys every child. |
| `getAttribute(name: text)` | método: `any` | Atributo personalizado (o null). |
| `setAttribute(name: text, value: any)` | método: `void` | Stores a custom attribute. |
| `getFullName()` | método: `text` | Full path: Workspace.Model.Part. |
| `create(className: text, parent?: any)` | método: `any` | Creates an instance from a class name. |

### DataModel

The game root ('game'). It contains every service. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `getService(name: text)` | método: `any` | Service by name ("Players", "Lighting"...). |
| `workspace` | propiedad, solo lectura: `Workspace` | The service Workspace. |
| `workspace2D` | propiedad, solo lectura: `Workspace2D` | The service Workspace2D. |
| `lighting` | propiedad, solo lectura: `Lighting` | The service Lighting. |
| `players` | propiedad, solo lectura: `Players` | The service Players. |
| `replicatedStorage` | propiedad, solo lectura: `ReplicatedStorage` | The service ReplicatedStorage. |
| `serverStorage` | propiedad, solo lectura: `ServerStorage` | The service ServerStorage. |
| `serverScriptService` | propiedad, solo lectura: `ServerScriptService` | The service ServerScriptService. |
| `starterGui` | propiedad, solo lectura: `StarterGui` | The service StarterGui. |
| `starterPlayer` | propiedad, solo lectura: `StarterPlayer` | The service StarterPlayer. |
| `soundService` | propiedad, solo lectura: `SoundService` | The service SoundService. |
| `teams` | propiedad, solo lectura: `Teams` | The service Teams. |

### Workspace

The 3D world: everything inside is visible and has physics. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `gravity` | propiedad: `number` | Gravity in studs/s² (196.2 by default). |
| `fallenPartsDestroyHeight` | propiedad: `number` | Parts falling below this height are destroyed. |
| `currentCamera` | propiedad: `any` | Active camera. |
| `raycast(origin: Vec3, direction: Vec3, ignore?: any)` | método: `map?` | Casts a ray (its length is that of 'direction'). Returns {instance, position, normal, distance} or null. |

### Workspace2D

The 2D world: sprites and text with 2D physics (Box2D). Coordinates in pixels, Y pointing down. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `gravity` | propiedad: `Vec2` | 2D gravity in pixels/s². |
| `backgroundColor` | propiedad: `Color` | Background colour of the 2D scene. |
| `renderMode` | propiedad: `text` | How it blends with the 3D world. |
| `cameraPosition` | propiedad: `Vec2` | 2D camera centre. |
| `cameraZoom` | propiedad: `number` | 2D camera zoom. |
| `cameraTarget` | propiedad: `any` | Sprite the camera follows (optional). |
| `pixelsPerMeter` | propiedad: `number` | 2D physics scale. |
| `virtualResolution` | propiedad: `Vec2` | Internal game resolution (0 = the window size). Pixel art: 320x180, 480x270, 640x360. |
| `pixelPerfect` | propiedad: `bool` | Integer scaling without smoothing (crisp pixel art). |
| `defaultFilter` | propiedad: `text` | Filtering of images with filter = Auto. |
| `ambientColor` | propiedad: `Color` | 2D ambient light (white = no darkness; darker = Light2D stands out). |
| `bloom` | propiedad: `bool` | Glow of bright things (emission, particles, lights). |
| `bloomIntensity` | propiedad: `number` | Glow strength. |
| `bloomThreshold` | propiedad: `number` | Brightness above which it glows. |
| `vignette` | propiedad: `number` | Darkens the edges. |
| `chromaticAberration` | propiedad: `number` | Colour separation at the edges. |
| `scanlines` | propiedad: `number` | Old TV scanlines (CRT). |
| `grain` | propiedad: `number` | Film grain. |
| `pixelate` | propiedad: `number` | Pixelate the image (pixel size; 0 = off). |
| `exposure` | propiedad: `number` | Brillo general. |
| `contrast` | propiedad: `number` | Contraste (1 = neutro). |
| `saturation` | propiedad: `number` | Saturation (0 = black and white). |
| `tint` | propiedad: `Color` | Tint of the whole image. |
| `smoothScroll` | propiedad: `bool` | With pixelPerfect: the camera slides in screen pixels even when the art uses big pixels (no stutter while moving). |
| `timeScale` | propiedad: `number` | 2D time speed (physics, animations and particles): 0.3 = slow motion, 0 = frozen. |
| `flashColor` | propiedad: `Color` | Screen flash colour (World2D.flash). |
| `flashAmount` | propiedad: `number` | Full-screen flash (0..1). |
| `fadeColor` | propiedad: `Color` | Fade colour (World2D.fadeOut / fadeIn). |
| `fadeAmount` | propiedad: `number` | Fundido a fadeColor (0..1): transiciones. |
| `raycast(origin: Vec2, direction: Vec2, ignore?: any)` | método: `map?` | 2D ray (its length is that of 'direction'). Returns {instance, position, normal, distance} or null. |
| `overlapPoint(point: Vec2)` | método: `list` | Objects with 2D physics at a point. |

### Lighting

Lighting, sky, fog and time of day. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `ambient` | propiedad: `Color` | Ambient light (shaded areas). |
| `brightness` | propiedad: `number` | Sun intensity. |
| `clockTime` | propiedad: `number` | Time of day (0-24): moves the sun. |
| `skyTopColor` | propiedad: `Color` | Sky colour at the top. |
| `skyHorizonColor` | propiedad: `Color` | Horizon colour. |
| `sunColor` | propiedad: `Color` | Sunlight colour. |
| `fogColor` | propiedad: `Color` | Fog colour. |
| `fogStart` | propiedad: `number` | Distance where the fog starts. |
| `fogEnd` | propiedad: `number` | Distance of full fog. |
| `globalShadows` | propiedad: `bool` | Sun shadows. |
| `exposure` | propiedad: `number` | Camera exposure. |
| `bloom` | propiedad: `bool` | Glow around bright areas (Neon). |
| `bloomIntensity` | propiedad: `number` | Glow strength. |
| `contrast` | propiedad: `number` | Image contrast (1 = neutral). |
| `saturation` | propiedad: `number` | Colour saturation (0 = black and white). |
| `vignette` | propiedad: `number` | Screen edge darkening. |
| `tint` | propiedad: `Color` | Colour tint of the whole image. |
| `shadowSoftness` | propiedad: `number` | Shadow edge softness. |
| `ambientOcclusion` | propiedad: `number` | Contact shadow in corners and at the base of objects. |
| `sunSize` | propiedad: `number` | Sun disc size. |
| `chromaticAberration` | propiedad: `number` | Colour separation at the edges. |
| `grain` | propiedad: `number` | Film grain. |

### Players

The connected players. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `maxPlayers` | propiedad: `number` | Maximum players per server. |
| `respawnTime` | propiedad: `number` | Seconds until respawning. |
| `characterAutoLoads` | propiedad: `bool` | Create the character automatically. |
| `playerAdded` | evento: `Event` | A player joined. Data: player: any. |
| `playerRemoving` | evento: `Event` | A player leaves. Data: player: any. |
| `getPlayers()` | método: `list` | Connected players. |
| `playerFromCharacter(character: any)` | método: `any` | Player who owns a character (or null). |
| `localPlayer` | propiedad, solo lectura: `any` | (Client) The player on this computer. |

### Player

A connected player (created while playing). Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `userId` | propiedad, solo lectura: `number` | Player identifier. |
| `displayName` | propiedad: `text` | Display name. |
| `character` | propiedad: `any` | Character model. |
| `team` | propiedad: `any` | The player's team. |
| `kick(reason?: text)` | método: `void` | (Server) Kicks the player. |
| `playerGui` | propiedad, solo lectura: `any` | Folder with the player interface. |

### StarterPlayer

Character settings and player scripts (client). Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `characterWalkSpeed` | propiedad: `number` | Walk speed. |
| `characterJumpPower` | propiedad: `number` | Jump strength. |
| `cameraMaxZoomDistance` | propiedad: `number` | Maximum zoom. |
| `cameraMinZoomDistance` | propiedad: `number` | Minimum zoom. |
| `cameraMode` | propiedad: `text` | Camera mode. |
| `rigType` | propiedad: `text` | Skeleton: R15 (articulated, realistic animation) or R6 (classic). |
| `headColor` | propiedad: `Color` | Head colour. |
| `torsoColor` | propiedad: `Color` | Torso colour. |
| `armsColor` | propiedad: `Color` | Arm colour. |
| `legsColor` | propiedad: `Color` | Leg colour. |

### StarterPlayerScripts

LocalScripts copied to each player on joining (client). Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|

### StarterCharacterScripts

LocalScripts copied to the character every time it spawns. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|

### StarterGui

Interface copied to each player (client). Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|

### ReplicatedStorage

Objects and modules shared by server and clients. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|

### ServerScriptService

Server scripts (clients do not see them). Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|

### ServerStorage

Objects only the server sees. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|

### SoundService

Global music and sounds. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|

### Teams

Player teams. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|

### Folder

Folder to organise objects. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|

### Model

Groups parts to move them together (a car, a house, a character). Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `primaryPart` | propiedad: `any` | Primary part (model centre). |
| `getPivot()` | método: `Vec3` | Model centre (or its primaryPart). |
| `moveTo(position: Vec3)` | método: `void` | Moves the whole model so its centre ends at 'position'. |
| `getBoundingBox()` | método: `map` | Bounding box: {center, size}. |

### BasePart

Base of every 3D part with physics. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `position` | propiedad: `Vec3` | Centre position (studs). |
| `rotation` | propiedad: `Vec3` | Rotation in degrees (X, Y, Z). |
| `size` | propiedad: `Vec3` | Size (studs). |
| `color` | propiedad: `Color` | Color. |
| `material` | propiedad: `text` | Material. |
| `transparency` | propiedad: `number` | 0 opaca, 1 invisible. |
| `reflectance` | propiedad: `number` | Sky reflection (0-1). |
| `castShadow` | propiedad: `bool` | Casts a shadow. |
| `anchored` | propiedad: `bool` | Anchored: physics does not move it. |
| `canCollide` | propiedad: `bool` | Collides with other parts. |
| `canTouch` | propiedad: `bool` | Fires the touched/touchEnded events. |
| `locked` | propiedad: `bool` | It cannot be selected with the mouse in the editor. |
| `friction` | propiedad: `number` | Rozamiento (0-2). |
| `elasticity` | propiedad: `number` | Rebote (0-1). |
| `density` | propiedad: `number` | Density (mass per volume). |
| `velocity` | propiedad: `Vec3` | Linear velocity (studs/s). |
| `angularVelocity` | propiedad: `Vec3` | Angular velocity (rad/s). |
| `touched` | evento: `Event` | Another part started touching this one. Data: other: any. |
| `touchEnded` | evento: `Event` | Another part stopped touching it. Data: other: any. |
| `applyImpulse(impulse: Vec3)` | método: `void` | Pushes the part (not anchored). |
| `getMass()` | método: `number` | Part mass. |
| `lookAt(target: Vec3)` | método: `void` | Rotates the part so its front (-Z) faces the point. |
| `getTouchingParts()` | método: `list` | Parts touching it right now (while playing). |

### Part

Basic part: block, sphere, cylinder or wedge. Hereda de [BasePart](#basepart).

| Miembro | Tipo | Descripción |
|---|---|---|
| `shape` | propiedad: `text` | Forma. |

### SpawnLocation

Point where players spawn. Hereda de [Part](#part).

| Miembro | Tipo | Descripción |
|---|---|---|
| `enabled` | propiedad: `bool` | Players can spawn here. |
| `neutral` | propiedad: `bool` | Any team can spawn here. |
| `team` | propiedad: `any` | Team that spawns here. |

### MeshPart

Part with an imported mesh (OBJ, glTF/GLB). Hereda de [BasePart](#basepart).

| Miembro | Tipo | Descripción |
|---|---|---|
| `meshId` | propiedad: `text` | Mesh asset. |
| `textureId` | propiedad: `text` | Texture (image). |
| `meshData` | propiedad: `text` | Malla incrustada. |
| `doubleSided` | propiedad: `bool` | Draw both faces. |

### UnionOperation

Result of a part Union/Subtract (CSG). Contains the original parts. Hereda de [MeshPart](#meshpart).

| Miembro | Tipo | Descripción |
|---|---|---|
| `usePartColor` | propiedad: `bool` | Uses the colour of the union instead of the originals. |

### Camera

3D camera. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `position` | propiedad: `Vec3` | Position. |
| `rotation` | propiedad: `Vec3` | Rotation in degrees (pitch, yaw, roll). |
| `fieldOfView` | propiedad: `number` | Vertical field of view (degrees). |
| `cameraType` | propiedad: `text` | Custom follows the character; Scriptable is controlled by your script. |
| `subject` | propiedad: `any` | What it follows (the character by default). |
| `lookAt(target: Vec3)` | método: `void` | Points the camera at a point. |

### Light

Base of the lights. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `color` | propiedad: `Color` | Light colour. |
| `brightness` | propiedad: `number` | Intensidad. |
| `range` | propiedad: `number` | Alcance (studs). |
| `enabled` | propiedad: `bool` | Encendida. |

### PointLight

Light in every direction (inside a part). Hereda de [Light](#light).

| Miembro | Tipo | Descripción |
|---|---|---|

### SpotLight

Spotlight: lights forward (-Z) from its part. Hereda de [Light](#light).

| Miembro | Tipo | Descripción |
|---|---|---|
| `angle` | propiedad: `number` | Cone angle (degrees). |

### ParticleEmitter

Emits particles (fire, smoke, sparks) from its part. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `enabled` | propiedad: `bool` | Emits particles. |
| `rate` | propiedad: `number` | Particles per second. |
| `lifetime` | propiedad: `Vec2` | Minimum and maximum lifetime (s). |
| `speed` | propiedad: `Vec2` | Minimum and maximum speed. |
| `spreadAngle` | propiedad: `number` | Spread (degrees). |
| `acceleration` | propiedad: `Vec3` | Acceleration (for example gravity or wind). |
| `color` | propiedad: `Color` | Initial colour. |
| `colorEnd` | propiedad: `Color` | Final colour. |
| `sizeRange` | propiedad: `Vec2` | Start and end size. |
| `texture` | propiedad: `text` | Particle image (optional). |
| `lightEmission` | propiedad: `number` | Brillo aditivo (0-1). |
| `transparency` | propiedad: `number` | Transparencia. |
| `burst` | propiedad: `number` | Burst particles on start (and with emit()). |
| `maxParticles` | propiedad: `number` | Maximum live particles. |
| `drag` | propiedad: `number` | Air drag. |
| `spin` | propiedad: `Vec2` | Minimum and maximum spin (degrees/s). |
| `blendMode` | propiedad: `text` | Additive adds light (fire, magic); Normal covers (smoke, dust). |
| `emit(count: number = 10)` | método: `void` | Emits a burst of particles (explosions, impacts). |

### WeldConstraint

Joins two parts so they move together. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `part0` | propiedad: `any` | First part. |
| `part1` | propiedad: `any` | Second part. |
| `enabled` | propiedad: `bool` | Activa. |

### ClickDetector

Makes its part clickable with the mouse. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `maxActivationDistance` | propiedad: `number` | Maximum distance. |
| `mouseClick` | evento: `Event` | A player clicked the part. Data: player: any. |

### Humanoid

Health and movement of a character. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `walkSpeed` | propiedad: `number` | Walk speed (studs/s). |
| `jumpPower` | propiedad: `number` | Initial jump speed. |
| `health` | propiedad: `number` | Current health. |
| `maxHealth` | propiedad: `number` | Maximum health. |
| `displayName` | propiedad: `text` | Name shown above the head. |
| `died` | evento: `Event` | Health reached 0. |
| `healthChanged` | evento: `Event` | Health changed. Data: health: number. |
| `takeDamage(amount: number)` | método: `void` | Takes health. |
| `moveTo(position: Vec3)` | método: `void` | Walks to a point. |
| `jump()` | método: `void` | Jumps (if on the ground). |

### LuaSourceContainer

Base of the scripts. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `source` | propiedad: `text` | HyperEZ code. |
| `enabled` | propiedad: `bool` | Runs when playing. |

### Script

SERVER script (HyperEZ). It goes in ServerScriptService or in Workspace. Hereda de [LuaSourceContainer](#luasourcecontainer).

| Miembro | Tipo | Descripción |
|---|---|---|

### LocalScript

CLIENT script (HyperEZ): input, camera, interface. It goes in StarterPlayerScripts, StarterGui or StarterCharacterScripts. Hereda de [LuaSourceContainer](#luasourcecontainer).

| Miembro | Tipo | Descripción |
|---|---|---|

### ModuleScript

Reusable HyperEZ module: used with import (for example import ReplicatedStorage.Utilities). Hereda de [LuaSourceContainer](#luasourcecontainer).

| Miembro | Tipo | Descripción |
|---|---|---|

### TouchScript

ON TOUCH script (server). Put it inside a part: its code runs every time a player touches it. Ready variables: part, player (who touches it) and character (their body). Hereda de [Script](#script).

| Miembro | Tipo | Descripción |
|---|---|---|

### ClickScript

ON CLICK script (server). Put it inside a part: its code runs when a player clicks it. Ready variables: part and player. Hereda de [Script](#script).

| Miembro | Tipo | Descripción |
|---|---|---|

### TimerScript

TIMER script (server): its code repeats every 'interval' seconds while the game runs. Ready variable: tick (1, 2, 3...). Hereda de [Script](#script).

| Miembro | Tipo | Descripción |
|---|---|---|
| `interval` | propiedad: `number` | Seconds between repetitions (0.03 minimum). |

### PlayerScript

PER PLAYER script (server): its code runs once for every player who joins. Ready variable: player. Hereda de [Script](#script).

| Miembro | Tipo | Descripción |
|---|---|---|

### GuiScript

INTERFACE script (client). Put it inside a ScreenGui or an element: it controls that interface on each player's screen. Ready variables: gui (what contains the script) and player. Hereda de [LocalScript](#localscript).

| Miembro | Tipo | Descripción |
|---|---|---|

### ButtonScript

ON PRESS script (client). Put it inside a TextButton or ImageButton: its code runs every time the player presses it. Ready variables: button and player. Hereda de [LocalScript](#localscript).

| Miembro | Tipo | Descripción |
|---|---|---|

### ValueBase

Base of the values. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|

### StringValue

Stores a text. Hereda de [ValueBase](#valuebase).

| Miembro | Tipo | Descripción |
|---|---|---|
| `value` | propiedad: `text` | Valor. |

### NumberValue

Stores a number. Hereda de [ValueBase](#valuebase).

| Miembro | Tipo | Descripción |
|---|---|---|
| `value` | propiedad: `number` | Valor. |

### BoolValue

Guarda verdadero/falso. Hereda de [ValueBase](#valuebase).

| Miembro | Tipo | Descripción |
|---|---|---|
| `value` | propiedad: `bool` | Valor. |

### Vector3Value

Stores a Vec3. Hereda de [ValueBase](#valuebase).

| Miembro | Tipo | Descripción |
|---|---|---|
| `value` | propiedad: `Vec3` | Valor. |

### ColorValue

Stores a colour. Hereda de [ValueBase](#valuebase).

| Miembro | Tipo | Descripción |
|---|---|---|
| `value` | propiedad: `Color` | Valor. |

### ObjectValue

Stores a reference to another instance. Hereda de [ValueBase](#valuebase).

| Miembro | Tipo | Descripción |
|---|---|---|
| `value` | propiedad: `any` | Instancia. |

### RemoteEvent

Messages between server and clients (fireServer, fireClient, fireAllClients). Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `onServerEvent` | evento: `Event` | (Server) A client called fireServer (value: the data sent). Data: player: any, value: any. |
| `onClientEvent` | evento: `Event` | (Client) The server called fireClient/fireAllClients. Data: value: any. |
| `fireServer(value?: any)` | método: `void` | (Client) Sends a message to the server. |
| `fireClient(player: any, value?: any)` | método: `void` | (Server) Sends a message to one player. |
| `fireAllClients(value?: any)` | método: `void` | (Server) Sends a message to every player. |

### BindableEvent

Event between scripts on the same side (server-server or client-client). Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `event` | evento: `Event` | Someone called fire(value). Data: value: any. |
| `fire(value?: any)` | método: `void` | Fires the event 'event' on this side. |

### Sound

Sound or music. Inside a part it plays in 3D. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `soundId` | propiedad: `text` | Sound asset (WAV, OGG, MP3) or a Music studio song. |
| `volume` | propiedad: `number` | Volume (0-10). |
| `playbackSpeed` | propiedad: `number` | Speed (changes the pitch). |
| `looped` | propiedad: `bool` | Repeat when finished. |
| `playing` | propiedad: `bool` | Playing (if active at the start, it plays). |
| `rollOffMaxDistance` | propiedad: `number` | Distance at which it can no longer be heard (3D). |
| `ended` | evento: `Event` | Finished playing. |
| `play()` | método: `void` | Empieza a sonar. |
| `stop()` | método: `void` | Stops and goes back to the start. |
| `pause()` | método: `void` | Pausa. |
| `isPlaying` | propiedad, solo lectura: `bool` | Is it playing? |
| `timeLength` | propiedad, solo lectura: `number` | Duration in seconds. |

### Animation

Keyframe animation of its model's properties (Animation editor). Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `data` | propiedad: `text` | Tracks and keyframes (JSON). |
| `looped` | propiedad: `bool` | Repetir. |
| `speed` | propiedad: `number` | Playback speed. |
| `autoPlay` | propiedad: `bool` | Starts by itself when playing. |
| `ended` | evento: `Event` | Finished (if it does not loop). |
| `play()` | método: `void` | Plays the animation. |
| `stop()` | método: `void` | Stops the animation. |
| `isPlaying` | propiedad, solo lectura: `bool` | Is it playing? |

### Team

A team of players. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `teamColor` | propiedad: `Color` | Team colour. |
| `autoAssignable` | propiedad: `bool` | Players are assigned automatically. |

### ScreenGui

Interface layer on screen (inside StarterGui). Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `enabled` | propiedad: `bool` | Visible. |
| `displayOrder` | propiedad: `number` | Drawing order (higher = on top). |

### GuiObject

Base of the interface elements. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `position` | propiedad: `Vec2` | Position relative to the parent (0-1). |
| `positionOffset` | propiedad: `Vec2` | Offset in pixels. |
| `size` | propiedad: `Vec2` | Size relative to the parent (0-1). |
| `sizeOffset` | propiedad: `Vec2` | Extra size in pixels. |
| `anchorPoint` | propiedad: `Vec2` | Anchor point (0,0 corner; 0.5,0.5 centre). |
| `backgroundColor` | propiedad: `Color` | Background colour. |
| `backgroundTransparency` | propiedad: `number` | Background transparency. |
| `borderColor` | propiedad: `Color` | Border colour. |
| `borderSize` | propiedad: `number` | Border width (px). |
| `cornerRadius` | propiedad: `number` | Esquinas redondeadas (px). |
| `visible` | propiedad: `bool` | Visible. |
| `zIndex` | propiedad: `number` | Order among siblings. |
| `mouseEnter` | evento: `Event` | The mouse entered. |
| `mouseLeave` | evento: `Event` | The mouse left. |

### Frame

Interface rectangle (container). Hereda de [GuiObject](#guiobject).

| Miembro | Tipo | Descripción |
|---|---|---|

### TextLabel

On-screen text. Hereda de [GuiObject](#guiobject).

| Miembro | Tipo | Descripción |
|---|---|---|
| `text` | propiedad: `text` | Texto. |
| `textColor` | propiedad: `Color` | Text colour. |
| `textSize` | propiedad: `number` | Font size (px). |
| `textTransparency` | propiedad: `number` | Text transparency. |
| `textXAlignment` | propiedad: `text` | Horizontal alignment. |
| `textYAlignment` | propiedad: `text` | Vertical alignment. |
| `textWrapped` | propiedad: `bool` | Split into several lines. |
| `bold` | propiedad: `bool` | Negrita (simulada). |
| `font` | propiedad: `text` | Imported font (TTF/OTF); empty = the engine font. |

### TextButton

Button with text. Hereda de [TextLabel](#textlabel).

| Miembro | Tipo | Descripción |
|---|---|---|
| `autoButtonColor` | propiedad: `bool` | Darken on hover/press. |
| `activated` | evento: `Event` | The button was pressed. |

### TextBox

Text input box. Hereda de [TextLabel](#textlabel).

| Miembro | Tipo | Descripción |
|---|---|---|
| `placeholderText` | propiedad: `text` | Hint text when it is empty. |
| `clearTextOnFocus` | propiedad: `bool` | Clear when typing starts. |
| `focusLost` | evento: `Event` | Typing finished (enterPressed = Enter was pressed). Data: enterPressed: bool. |

### ImageLabel

On-screen image. Hereda de [GuiObject](#guiobject).

| Miembro | Tipo | Descripción |
|---|---|---|
| `image` | propiedad: `text` | Image asset. |
| `imageColor` | propiedad: `Color` | Tinte. |
| `imageTransparency` | propiedad: `number` | Transparencia. |
| `scaleType` | propiedad: `text` | Ajuste. |

### ImageButton

Button with an image. Hereda de [ImageLabel](#imagelabel).

| Miembro | Tipo | Descripción |
|---|---|---|
| `activated` | evento: `Event` | The button was pressed. |

### Node2D

Base of 2D objects: position, rotation, scale, draw order and visibility. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `position` | propiedad: `Vec2` | Position (pixels; Y grows downwards). |
| `rotation` | propiedad: `number` | Rotation (degrees, clockwise). |
| `scale` | propiedad: `Vec2` | Scale (1 = normal size; negative flips). |
| `zIndex` | propiedad: `number` | Drawing order (higher = in front). |
| `visible` | propiedad: `bool` | Visible (also hides its children). |
| `getWorldPosition()` | método: `Vec2` | World position (adding those of its parents). |
| `lookAt(target: Vec2)` | método: `void` | Rotates the object to face a point. |

### Sprite2D

Image or 2D shape with optional physics (Box2D), frame animation, outline, flash, shadow, glow and lights. Hereda de [Node2D](#node2d).

| Miembro | Tipo | Descripción |
|---|---|---|
| `size` | propiedad: `Vec2` | Size (pixels). |
| `pivot` | propiedad: `Vec2` | Pivot inside the sprite (0,0 top left corner; 0.5,0.5 centre; 0.5,1 feet). |
| `image` | propiedad: `text` | Image (empty = coloured shape). |
| `color` | propiedad: `Color` | Colour (or image tint). |
| `transparency` | propiedad: `number` | Transparencia (0 opaco, 1 invisible). |
| `shape` | propiedad: `text` | Shape (drawing without an image and collision). |
| `cornerRadius` | propiedad: `number` | Corner radius (RoundedBox). |
| `sides` | propiedad: `number` | Lados o puntas (Polygon, Star). |
| `innerRatio` | propiedad: `number` | Radio interior (Star, Ring). |
| `flipX` | propiedad: `bool` | Voltear en horizontal. |
| `flipY` | propiedad: `bool` | Voltear en vertical. |
| `blendMode` | propiedad: `text` | Blends with what is behind. |
| `filter` | propiedad: `text` | Image filtering (Pixel for pixel art). |
| `regionPosition` | propiedad: `Vec2` | Corner of the part of the image that is used (pixels). |
| `regionSize` | propiedad: `Vec2` | Size of the part of the image (0 = the whole image). |
| `tiling` | propiedad: `Vec2` | Times the image repeats (floors, walls). |
| `lit` | propiedad: `bool` | Affected by 2D lights and ambient light. |
| `emission` | propiedad: `number` | Self-illumination: glows with bloom (0 = none). |
| `outlineColor` | propiedad: `Color` | Outline colour. |
| `outlineSize` | propiedad: `number` | Outline width (0 = no outline). |
| `flashColor` | propiedad: `Color` | Flash colour. |
| `flash` | propiedad: `number` | Flash 0..1 (animate it with Tween or use flashOnce). |
| `shadowOpacity` | propiedad: `number` | Drop shadow (0 = no shadow). |
| `castShadow` | propiedad: `bool` | Blocks the light of Light2D: casts shadows. |
| `normalMap` | propiedad: `text` | Normal map (relief with lighting); same grid as the image. |
| `relief` | propiedad: `number` | Automatic relief derived from the image or shape (0 = flat). |
| `shadowOffset` | propiedad: `Vec2` | Shadow offset (pixels). |
| `shadowColor` | propiedad: `Color` | Shadow colour. |
| `frames` | propiedad: `number` | Sprite sheet frames. |
| `columns` | propiedad: `number` | Sheet columns (0 = all in one row). |
| `frameRate` | propiedad: `number` | Frames per second (0 = still). With SpriteAnimator it is controlled by the animator. |
| `frame` | propiedad: `number` | Current frame. |
| `body` | propiedad: `text` | Body type: Static (ground), Dynamic (falls and collides), Kinematic (moved by you). |
| `collisionSize` | propiedad: `Vec2` | Collision size (0 = the sprite size). |
| `collisionOffset` | propiedad: `Vec2` | Collision offset. |
| `friction` | propiedad: `number` | Rozamiento. |
| `restitution` | propiedad: `number` | Rebote. |
| `density` | propiedad: `number` | Density (mass). |
| `fixedRotation` | propiedad: `bool` | Does not rotate (characters). |
| `gravityScale` | propiedad: `number` | Gravity multiplier (0 = floats). |
| `isSensor` | propiedad: `bool` | Detects contacts without colliding (coins, zones). |
| `oneWay` | propiedad: `bool` | One-way platform: you can jump through it from below. |
| `collisionLayer` | propiedad: `number` | Collision layer (1..16). |
| `collisionMask` | propiedad: `text` | Layers it collides with: "all" or a list ("1,3"). |
| `linearDamping` | propiedad: `number` | Movement drag (air, water). |
| `angularDamping` | propiedad: `number` | Angular drag. |
| `bullet` | propiedad: `bool` | Continuous detection for very fast objects (bullets). |
| `velocity` | propiedad: `Vec2` | Speed (px/s). |
| `angularVelocity` | propiedad: `number` | Spin speed (degrees/s). |
| `onGround` | propiedad, solo lectura: `bool` | (While playing) Is it resting on something? |
| `touched` | evento: `Event` | Another 2D object started touching it. Data: other: any. |
| `touchEnded` | evento: `Event` | Stopped touching it. Data: other: any. |
| `clicked` | evento: `Event` | (While playing) The player clicked the sprite. Data: button: number. |
| `applyImpulse(impulse: Vec2)` | método: `void` | Pushes the sprite at once (dynamic body). |
| `applyForce(force: Vec2)` | método: `void` | Pushes the sprite gradually (call it every frame). |
| `applyTorque(torque: number)` | método: `void` | Makes it spin. |
| `getTouching()` | método: `list` | 2D objects touching it now (while playing). |
| `isOnGround()` | método: `bool` | Is it resting on something? (while playing) |
| `flashOnce(duration: number = 0.15, color?: Color)` | método: `Task` | Quick flash (hits, picking up items). |
| `playAnimation(name?: text)` | método: `void` | Plays an animation from its SpriteAnimator ("run", "jump"...). |

### SpriteAnimator

Plays named animations ("idle", "run"...) from a sprite animation asset on the parent Sprite2D. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `animations` | propiedad: `text` | Animation asset (sheet, grid and clips). |
| `animation` | propiedad: `text` | Animation being played. |
| `playing` | propiedad: `bool` | Reproduciendo. |
| `speed` | propiedad: `number` | Speed (1 = normal). |
| `finished` | evento: `Event` | A non-looping animation finished. Data: animation: text. |
| `frameChanged` | evento: `Event` | Changed frame (steps, hits, sounds). Data: frame: number. |
| `play(name?: text)` | método: `void` | Plays an animation (without a name: restarts the current one). |
| `stop()` | método: `void` | Stops and goes back to the first frame. |
| `pause()` | método: `void` | Pausa. |

### ParticleEmitter2D

2D particle effects: fire, smoke, sparks, explosions, magic, rain, snow... Choose a ready-made effect in Properties. Hereda de [Node2D](#node2d).

| Miembro | Tipo | Descripción |
|---|---|---|
| `emitting` | propiedad: `bool` | Emitting particles. |
| `rate` | propiedad: `number` | Particles per second. |
| `burst` | propiedad: `number` | Burst particles on start. |
| `oneShot` | propiedad: `bool` | Only the initial burst (explosions). |
| `emissionShape` | propiedad: `text` | Spawn area. |
| `emissionSize` | propiedad: `Vec2` | Zone size (radius or width and height). |
| `maxParticles` | propiedad: `number` | Maximum live particles. |
| `localSpace` | propiedad: `bool` | Particles move with the emitter. |
| `lifetime` | propiedad: `Vec2` | Minimum and maximum lifetime (s). |
| `speed` | propiedad: `Vec2` | Minimum and maximum speed (px/s). |
| `direction` | propiedad: `number` | Direction (degrees: 0 right, 90 down, -90 up). |
| `spread` | propiedad: `number` | Spray angle (degrees; 360 = every direction). |
| `gravity` | propiedad: `Vec2` | Particle gravity (px/s²). |
| `drag` | propiedad: `number` | Air drag. |
| `spin` | propiedad: `Vec2` | Minimum and maximum spin (degrees/s). |
| `alignToVelocity` | propiedad: `bool` | Point each particle where it goes (sparks, rain). |
| `sizeRange` | propiedad: `Vec2` | Size when born and when dying (px). |
| `sizeRandom` | propiedad: `number` | Random size variation. |
| `colorStart` | propiedad: `Color` | Colour when born. |
| `colorEnd` | propiedad: `Color` | Colour when dying. |
| `alphaStart` | propiedad: `number` | Opacity when born. |
| `alphaEnd` | propiedad: `number` | Opacity when dying. |
| `particleShape` | propiedad: `text` | Shape of particles without an image. |
| `texture` | propiedad: `text` | Image of each particle (optional). |
| `textureFrames` | propiedad: `number` | Horizontal frames in the image. |
| `blendMode` | propiedad: `text` | Blending (Additive for fire and light). |
| `emission` | propiedad: `number` | Glow (bloom). |
| `lit` | propiedad: `bool` | Affected by 2D lights. |
| `emit(count: number = 10)` | método: `void` | Emits a burst of particles (explosions, impacts). |
| `clear()` | método: `void` | Clears the live particles. |
| `applyPreset(name: text)` | método: `void` | Applies a ready-made effect: fire, smoke, sparks, explosion, magic, rain, snow, dust, confetti, bubbles, fireflies, heal. |

### Tilemap2D

Tile map: choose a tile set (an image laid out in a grid) and paint the level with the tile brush. Collisions are generated automatically. Hereda de [Node2D](#node2d).

| Miembro | Tipo | Descripción |
|---|---|---|
| `tileset` | propiedad: `text` | Image with the tiles laid out in a grid. |
| `tileSize` | propiedad: `Vec2` | Size of each tile in the image (px). |
| `cellSize` | propiedad: `Vec2` | Size of each tile in the world (0 = the image size). |
| `color` | propiedad: `Color` | Tinte. |
| `transparency` | propiedad: `number` | Transparencia. |
| `lit` | propiedad: `bool` | Affected by 2D lights. |
| `collision` | propiedad: `bool` | Solid tiles collide. |
| `solidTiles` | propiedad: `text` | Solid tiles: "all", "none" or a list ("0-15,20"). |
| `friction` | propiedad: `number` | Rozamiento. |
| `oneWay` | propiedad: `bool` | Can be passed through from below (platforms). |
| `collisionLayer` | propiedad: `number` | Collision layer (1..16). |
| `castShadows` | propiedad: `bool` | Solid tiles block the light of Light2D (shadows). |
| `relief` | propiedad: `number` | Automatic relief with lighting (0 = flat). |
| `autotile` | propiedad: `text` | Auto tiles: first tile of each block of 16 variants ("0" or "0,16"). The edge is chosen automatically while painting. |
| `getTile(x: number, y: number)` | método: `number` | Tile at (x, y) (-1 = empty). |
| `setTile(x: number, y: number, tile: number)` | método: `void` | Places a tile (-1 erases it). |
| `fillRect(x: number, y: number, w: number, h: number, tile: number)` | método: `void` | Fills a rectangle of tiles. |
| `clearTiles()` | método: `void` | Clears every tile. |
| `worldToCell(point: Vec2)` | método: `Vec2` | Tile (x, y) at a world point. |
| `cellToWorld(x: number, y: number)` | método: `Vec2` | Tile centre in the world. |

### Camera2D

2D camera: follows an object smoothly, with dead zone, level bounds, zoom and shake. Hereda de [Node2D](#node2d).

| Miembro | Tipo | Descripción |
|---|---|---|
| `current` | propiedad: `bool` | It is the camera used while playing. |
| `zoom` | propiedad: `number` | Zoom (2 = twice as close). |
| `follow` | propiedad: `any` | Object it follows (optional). |
| `smoothing` | propiedad: `number` | Smoothing (0 = follows instantly). |
| `offset` | propiedad: `Vec2` | Offset from the target. |
| `deadZone` | propiedad: `Vec2` | Zone (width, height) where the target moves without moving the camera. |
| `limitsEnabled` | propiedad: `bool` | Show nothing outside the level bounds. |
| `limitMin` | propiedad: `Vec2` | Top left corner of the level. |
| `limitMax` | propiedad: `Vec2` | Bottom right corner of the level. |
| `pixelSnap` | propiedad: `bool` | Round to whole pixels (pixel art without jitter). |
| `shake(intensity: number = 8, duration: number = 0.35)` | método: `void` | Shakes the camera (hits, explosions). |

### Light2D

2D light (torches, street lamps, magic). Darken the scene with Workspace2D.ambientColor so it shows. Hereda de [Node2D](#node2d).

| Miembro | Tipo | Descripción |
|---|---|---|
| `enabled` | propiedad: `bool` | Encendida. |
| `color` | propiedad: `Color` | Color. |
| `energy` | propiedad: `number` | Intensidad. |
| `radius` | propiedad: `number` | Alcance (px). |
| `falloff` | propiedad: `number` | Falloff towards the edge (higher = softer edge). |
| `flicker` | propiedad: `number` | Parpadeo (antorchas, fuego). |
| `lightType` | propiedad: `text` | Point, Spot (aimed by rotation) or Directional (sun, moon). |
| `angle` | propiedad: `number` | Spotlight angle (degrees). |
| `halo` | propiedad: `number` | Light visible in the air: dust, fog and rays between the shadows. |
| `height` | propiedad: `number` | Height above the scene: lower shows more relief. |
| `castShadows` | propiedad: `bool` | Objects with castShadow and tiles with castShadows cast shadows. |
| `shadowSoftness` | propiedad: `number` | 0 = hard; 1 = very soft far from the object. |
| `shadowStrength` | propiedad: `number` | 0 = no shadow; 1 = black. |

### Layer2D

2D layer: groups objects to order (layer zIndex), hide or lock them together, with parallax, opacity and tint. Hereda de [Node2D](#node2d).

| Miembro | Tipo | Descripción |
|---|---|---|
| `opacity` | propiedad: `number` | Opacity of everything inside. |
| `tint` | propiedad: `Color` | Tint of everything inside. |
| `parallax` | propiedad: `Vec2` | 1 = with the world; 0.5 = far (moves half as much); 1.3 = near. Visible while playing. |
| `locked` | propiedad: `bool` | Locked: its objects cannot be selected in the 2D view in the editor. |

### Water2D

2D water with waves, reflection and refraction of what is behind. Dynamic bodies float and slow down inside. Hereda de [Node2D](#node2d).

| Miembro | Tipo | Descripción |
|---|---|---|
| `size` | propiedad: `Vec2` | Width and depth (px). The surface is the top edge. |
| `color` | propiedad: `Color` | Deep water colour. |
| `surfaceColor` | propiedad: `Color` | Colour of the foam and surface shine. |
| `transparency` | propiedad: `number` | How much of what is behind shows through. |
| `reflectivity` | propiedad: `number` | Reflection of what is above. |
| `waveHeight` | propiedad: `number` | Wave height (px). |
| `waveLength` | propiedad: `number` | Distance between waves (px). |
| `waveSpeed` | propiedad: `number` | Wave speed. |
| `distortion` | propiedad: `number` | Refraction: how much what is seen through ripples (px). |
| `foam` | propiedad: `number` | Foam on the surface. |
| `buoyancy` | propiedad: `number` | Upward push (more than 1 = bodies float). |
| `drag` | propiedad: `number` | Drag inside water. |
| `entered` | evento: `Event` | A 2D body enters the water (splashes, sound). Data: other: any. |
| `exited` | evento: `Event` | A 2D body leaves the water. Data: other: any. |

### Background2D

Repeating background with parallax (skies, mountains, clouds): moves slower than the camera. Hereda de [Node2D](#node2d).

| Miembro | Tipo | Descripción |
|---|---|---|
| `image` | propiedad: `text` | Image. |
| `color` | propiedad: `Color` | Tinte. |
| `transparency` | propiedad: `number` | Transparencia. |
| `scrollFactor` | propiedad: `Vec2` | 0 = fixed on screen, 1 = moves with the world (0.2 far, 0.6 near). |
| `repeatX` | propiedad: `bool` | Repetir en horizontal. |
| `repeatY` | propiedad: `bool` | Repetir en vertical. |
| `size` | propiedad: `Vec2` | Size of each copy (0 = the image size). |
| `autoScroll` | propiedad: `Vec2` | Automatic scrolling (clouds): px/s. |
| `lit` | propiedad: `bool` | Affected by 2D lights. |

### Line2D

Line with several points (paths, ropes, rays, outlines). Edit the points by dragging them in the 2D view. Hereda de [Node2D](#node2d).

| Miembro | Tipo | Descripción |
|---|---|---|
| `points` | propiedad: `text` | Points: "x,y; x,y; ..." (relative to the position). |
| `width` | propiedad: `number` | Thickness. |
| `widthEnd` | propiedad: `number` | Width at the end (-1 = the same). |
| `color` | propiedad: `Color` | Colour at the start. |
| `colorEnd` | propiedad: `Color` | Colour at the end. |
| `transparency` | propiedad: `number` | Transparencia. |
| `closed` | propiedad: `bool` | Close (join the last point to the first). |
| `roundCaps` | propiedad: `bool` | Rounded ends and corners. |
| `emission` | propiedad: `number` | Glow (bloom: lasers). |

### Trail2D

Trail left by its parent while moving (swords, projectiles, cars, shooting stars). Hereda de [Node2D](#node2d).

| Miembro | Tipo | Descripción |
|---|---|---|
| `emitting` | propiedad: `bool` | Dejando estela. |
| `lifetime` | propiedad: `number` | Trail duration (s). |
| `width` | propiedad: `number` | Width at the start. |
| `widthEnd` | propiedad: `number` | Width at the end. |
| `color` | propiedad: `Color` | Colour at the start. |
| `colorEnd` | propiedad: `Color` | Colour at the end. |
| `alphaStart` | propiedad: `number` | Opacity at the start. |
| `alphaEnd` | propiedad: `number` | Opacity at the end. |
| `blendMode` | propiedad: `text` | Mezcla. |
| `emission` | propiedad: `number` | Brillo. |
| `minDistance` | propiedad: `number` | Minimum distance between points (px). |

### Joint2D

Joins two sprites with physics: hinge, distance, spring, rope, weld or wheel. Put it inside one and choose the other in bodyB. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `jointType` | propiedad: `text` | Joint type. |
| `bodyA` | propiedad: `any` | First sprite (empty = the parent). |
| `bodyB` | propiedad: `any` | Second sprite. |
| `anchorA` | propiedad: `Vec2` | Anchor point on the first one (px from its centre). |
| `anchorB` | propiedad: `Vec2` | Anchor point on the second one. |
| `length` | propiedad: `number` | Longitud (Distance, Spring, Rope; 0 = la inicial). |
| `stiffness` | propiedad: `number` | Spring stiffness (Hz). |
| `damping` | propiedad: `number` | Spring damping. |
| `collideConnected` | propiedad: `bool` | Both sprites collide with each other. |
| `motor` | propiedad: `bool` | Motor (Revolute, Wheel). |
| `motorSpeed` | propiedad: `number` | Motor speed (degrees/s). |
| `maxMotorTorque` | propiedad: `number` | Maximum motor force. |
| `limit` | propiedad: `bool` | Limit the rotation (Revolute). |
| `lowerAngle` | propiedad: `number` | Minimum angle. |
| `upperAngle` | propiedad: `number` | Maximum angle. |

### PlatformerController2D

No-code platformer movement for the parent Sprite2D (Dynamic body): run, jump, double jump, coyote time and jump buffering. If the sprite has a SpriteAnimator, it switches animations by itself. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `enabled` | propiedad: `bool` | Activo. |
| `speed` | propiedad: `number` | Maximum speed (px/s). |
| `acceleration` | propiedad: `number` | Acceleration (px/s²). |
| `deceleration` | propiedad: `number` | Braking when released (px/s²). |
| `airControl` | propiedad: `number` | Air control (0..1). |
| `jumpHeight` | propiedad: `number` | Jump height (px). |
| `maxJumps` | propiedad: `number` | Consecutive jumps (2 = double jump). |
| `coyoteTime` | propiedad: `number` | Time to jump after leaving a ledge (s). |
| `jumpBuffer` | propiedad: `number` | Time a jump is remembered before touching the ground (s). |
| `variableJump` | propiedad: `bool` | Releasing the key early cuts the jump. |
| `fallMultiplier` | propiedad: `number` | Extra gravity when falling (weighty jumps). |
| `leftKeys` | propiedad: `text` | Keys to go left. |
| `rightKeys` | propiedad: `text` | Keys to go right. |
| `jumpKeys` | propiedad: `text` | Keys to jump. |
| `flipSprite` | propiedad: `bool` | Flip the sprite towards where it runs. |
| `animIdle` | propiedad: `text` | Idle animation. |
| `animRun` | propiedad: `text` | Running animation. |
| `animJump` | propiedad: `text` | Rising animation. |
| `animFall` | propiedad: `text` | Falling animation. |
| `jumped` | evento: `Event` | Jumped. |
| `landed` | evento: `Event` | Touched the ground. |

### TopDownController2D

Eight-direction top-down movement for the parent Sprite2D (RPG, adventures). With a Dynamic body it collides with walls. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `enabled` | propiedad: `bool` | Activo. |
| `speed` | propiedad: `number` | Maximum speed (px/s). |
| `acceleration` | propiedad: `number` | Acceleration. |
| `deceleration` | propiedad: `number` | Frenado. |
| `upKeys` | propiedad: `text` | Arriba. |
| `downKeys` | propiedad: `text` | Abajo. |
| `leftKeys` | propiedad: `text` | Izquierda. |
| `rightKeys` | propiedad: `text` | Derecha. |
| `facing` | propiedad: `text` | How it faces where it goes. |
| `animIdle` | propiedad: `text` | Idle animation. |
| `animWalk` | propiedad: `text` | Walking animation. |

### Text2D

Text inside the 2D world (floating scores, signs, dialogues). Hereda de [Node2D](#node2d).

| Miembro | Tipo | Descripción |
|---|---|---|
| `text` | propiedad: `text` | Texto. |
| `textSize` | propiedad: `number` | Size (px). |
| `color` | propiedad: `Color` | Color. |
| `transparency` | propiedad: `number` | Transparencia. |
| `alignment` | propiedad: `text` | Alignment. |
| `bold` | propiedad: `bool` | Negrita. |
| `font` | propiedad: `text` | Imported font (TTF/OTF); empty = the engine font. |
| `outlineColor` | propiedad: `Color` | Outline colour. |
| `outlineSize` | propiedad: `number` | Outline width (px). |
| `shadowOpacity` | propiedad: `number` | Sombra. |

### Note

Team note anchored to a point in the world: comments, tasks or ideas. Only visible in the editor. Hereda de [Instance](#instance).

| Miembro | Tipo | Descripción |
|---|---|---|
| `text` | propiedad: `text` | Note text. |
| `author` | propiedad: `text` | Who wrote it. |
| `position` | propiedad: `Vec3` | World point where it is anchored. |
| `color` | propiedad: `Color` | Marker colour. |
| `resolved` | propiedad: `bool` | Resolved (shown dimmed). |
| `createdAt` | propiedad: `number` | Creation date (seconds). |

## Enumeraciones

| Nombre | Valores | Descripción |
|---|---|---|
| `BlendMode2D` | `Normal`, `Additive`, `Multiply`, `Screen` | How it blends with what is behind: Normal, Additive (adds light: fire, magic), Multiply (darkens), Screen (lightens). |
| `BodyType2D` | `None`, `Static`, `Dynamic`, `Kinematic` | 2D physics of a sprite. |
| `CameraMode` | `Classic`, `LockFirstPerson` | Player camera mode. |
| `CameraType` | `Custom`, `Scriptable`, `Fixed` | How the camera moves. |
| `EmissionShape2D` | `Point`, `Circle`, `Rectangle`, `Ring`, `Line` | Zone where particles are born. |
| `Facing2D` | `None`, `Flip`, `Rotate` | How the character faces the direction it moves. |
| `JointType2D` | `Revolute`, `Distance`, `Spring`, `Rope`, `Weld`, `Wheel` | Joint type: hinge, fixed distance, spring, rope, weld or wheel (with suspension). |
| `LightType2D` | `Point`, `Spot`, `Directional` | Point: lights a circle. Spot: a spotlight aimed by rotation (0 right, 90 down). Directional: a sun or moon lighting everything. |
| `Material` | `Plastic`, `SmoothPlastic`, `Neon`, `Metal`, `Wood`, `Glass`, `Grass`, `Brick`, `Concrete`, `Ice`, `Sand`, `Fabric`, `Marble`, `Slate`, `ForceField` | Part material: changes the look (procedural texture, shine, reflections). |
| `PartShape` | `Block`, `Ball`, `Cylinder`, `Wedge` | Shape of a part. |
| `ParticleShape2D` | `Soft`, `Circle`, `Square`, `Spark`, `Star`, `Ring` | Shape of each particle (when it has no image). |
| `RenderMode2D` | `Auto`, `Overlay`, `Exclusive`, `Off` | Auto: 2D only when there are no 3D parts; Overlay: on top of 3D; Exclusive: 2D only; Off: not drawn. |
| `RigType` | `R15`, `R6` | Character skeleton: R15 (15 parts with elbows, knees, hands and feet) or R6 (6 parts). |
| `ScaleType` | `Stretch`, `Fit` | How an image fits its box. |
| `Shape2D` | `Box`, `Circle`, `RoundedBox`, `Capsule`, `Triangle`, `Polygon`, `Star`, `Ring` | 2D shape (drawing without an image and collision). |
| `TextXAlignment` | `Left`, `Center`, `Right` | Horizontal text alignment. |
| `TextYAlignment` | `Top`, `Center`, `Bottom` | Vertical text alignment. |
| `TextureFilter2D` | `Auto`, `Pixel`, `Smooth` | Image filtering: Pixel (crisp pixel art), Smooth (smoothed) or Auto. |
