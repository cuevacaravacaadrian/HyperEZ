# LPO Engine API for HyperEZ

Generated automatically from the engine reflection (`LPOEngine --docs`). Every class, property and event really exists in the engine.

## Globals

- `Game` — The running game: time, side (server/client) and the update event of every frame.
- `Input` — (Client) The player's keyboard, mouse and gamepad.
- `Tween` — Tweens: animate number, Vec2, Vec3 and Color properties.
- `Debris` — Destroys objects after a while.
- `DataStore` — (Server) Data kept between sessions (scores, inventories...).
- `Assets` — Game assets: reads imported text and data (JSON, CSV, dialogues, levels).
- `World2D` — Helpers for 2D games: find and create objects, floating text, particles, shake, slow motion, hit freeze, flashes, fades and zone queries.
- `Timer` — Timers: call a function after a while or every so often (game time).
- `game`: DataModel — The game (root of everything).
- `workspace`: Workspace — The 3D world.
- `workspace2D`: Workspace2D — The 2D world.

## Game

- **time**: number *(property)* — Game seconds since it started.
- **isServer**: bool *(property)* — Does this script run on the server?
- **isClient**: bool *(property)* — Does this script run on a client?
- **isStudio**: bool *(property)* — Is it being tested in LPO Engine?
- **update**(dt: number): void *(event)* — Every frame (dt = seconds since the previous one).

## Input

- **isKeyDown**(key: text): bool *(function)* — Is the key pressed? ("W", "Space", "Left", "LeftShift"...)
- **isMouseDown**(button: number = 1): bool *(function)* — Is the mouse button pressed? (1 left, 2 middle, 3 right)
- **mousePosition**: Vec2 *(property)* — Mouse position in the game view (pixels).
- **mouseDelta**: Vec2 *(property)* — Mouse movement in this frame.
- **viewSize**: Vec2 *(property)* — Game view size (pixels).
- **mouseHit**: Vec3 *(property)* — 3D world point under the mouse.
- **mouseTarget**: any *(property)* — Part under the mouse (or null).
- **gamepadStick**: Vec2 *(property)* — Left stick of the gamepad (-1..1).
- **mouseWorld2D**: Vec2 *(property)* — Mouse position in the 2D world (with the 2D camera).
- **keyDown**(key: text): void *(event)* — A key was pressed.
- **keyUp**(key: text): void *(event)* — A key was released.
- **mouseDown**(button: number, position: Vec2): void *(event)* — A mouse button was pressed.
- **mouseUp**(button: number, position: Vec2): void *(event)* — A mouse button was released.
- **mouseWheel**(delta: number): void *(event)* — The mouse wheel moved.

## Tween

- **to**(target: any, props: map, duration: number, easing: text = "quadOut", delay: number = 0): Task *(function)* — Animates the properties to the given values. Curves: linear, quadIn, quadOut, quadInOut, cubicOut, sineInOut, backOut, bounceOut, elasticOut.

## Debris

- **add**(instance: any, seconds: number = 5): void *(function)* — Destroys the instance after the given seconds.

## DataStore

- **get**(key: text, default?: any): any *(function)* — Stored value (or 'default').
- **set**(key: text, value: any): void *(function)* — Stores a value (numbers, text, lists, maps...).
- **remove**(key: text): void *(function)* — Deletes a value.
- **keys**(): list *(function)* — Claves guardadas.

## Assets

- **readText**(name: text): text *(function)* — Contents of a text asset.
- **readJson**(name: text): any *(function)* — Reads a JSON asset as maps and lists.
- **readCsv**(name: text): list *(function)* — Reads a CSV table as a list of rows (each row a list of text).
- **exists**(name: text): bool *(function)* — Does the asset exist?
- **list**(type?: text): list *(function)* — Asset names (of one type: image, sound, text, font, mesh, song, spriteanim).

## World2D

- **find**(name: text): any *(function)* — The first object in the 2D world with that name (searches everywhere).
- **findAll**(nameOrClass: text): list *(function)* — Every object in the 2D world with that name or of that class.
- **spawn**(template: any, position?: Vec2, parent?: any): any *(function)* — Creates a copy of an object (for example kept in ReplicatedStorage) in the 2D world, at that position.
- **popup**(text: any, position: any, color?: Color, size: number = 12): any *(function)* — Floating text that rises and fades (damage, points, notices). The position can be an object.
- **burst**(preset: text, position: any, count: number = 24): any *(function)* — Particle burst from a ready-made effect (fire, smoke, sparks, explosion, magic, dust, confetti...) that clears itself.
- **shake**(intensity: number = 8, seconds: number = 0.35): void *(function)* — Shakes the current 2D camera.
- **hitStop**(seconds: number = 0.08): Task *(function)* — Freezes the 2D world for an instant: gives hits more impact.
- **slowMotion**(scale: number = 0.3, seconds: number = 1): Task *(function)* — Slow motion for a few seconds and a smooth return to normal.
- **flash**(color?: Color, seconds: number = 0.25, amount: number = 0.75): Task *(function)* — Full-screen flash.
- **fadeOut**(seconds: number = 0.6, color?: Color): Task *(function)* — Fade to a colour (black if none is given). Use it with await.
- **fadeIn**(seconds: number = 0.6): Task *(function)* — Returns from the fade.
- **overlapCircle**(center: any, radius: number): list *(function)* — Sprites touching a circle (explosions, attack ranges).
- **raycast**(from: any, to: any, ignore?: any): map? *(function)* — Ray from one point to another: {instance, position, normal, distance} of the first thing it hits, or null.
- **distance**(a: any, b: any): number *(function)* — Distance between two objects or points.
- **direction**(from: any, to: any): Vec2 *(function)* — Direction (length 1) from one object or point to another.
- **timeScale**: number *(property)* — 2D time speed (1 normal, 0.3 slow, 0 frozen).
- **camera**: any *(property)* — The current Camera2D (or null).
- **mouse**: Vec2 *(property)* — Mouse position in the 2D world.

## Timer

- **after**(seconds: number, fn: function): number *(function)* — Calls the function once after the given seconds. Returns its number.
- **every**(seconds: number, fn: function, times?: number): number *(function)* — Calls the function every few seconds (forever or 'times' times). Returns its number.
- **cancel**(id: number): void *(function)* — Stops a timer.

## Classes

### Instance

Base object of the hierarchy. Everything in LPO Engine is an instance.

Area: General. 

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **create**(className: text, parent?: any): any *(method)* — Creates an instance from a class name.

### DataModel

The game root ('game'). It contains every service.

Inherits from **Instance**. Area: General. 

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **getService**(name: text): any *(method)* — Service by name ("Players", "Lighting"...).
- **workspace**: Workspace *(property, read-only)* — The service Workspace.
- **workspace2D**: Workspace2D *(property, read-only)* — The service Workspace2D.
- **lighting**: Lighting *(property, read-only)* — The service Lighting.
- **players**: Players *(property, read-only)* — The service Players.
- **replicatedStorage**: ReplicatedStorage *(property, read-only)* — The service ReplicatedStorage.
- **serverStorage**: ServerStorage *(property, read-only)* — The service ServerStorage.
- **serverScriptService**: ServerScriptService *(property, read-only)* — The service ServerScriptService.
- **starterGui**: StarterGui *(property, read-only)* — The service StarterGui.
- **starterPlayer**: StarterPlayer *(property, read-only)* — The service StarterPlayer.
- **soundService**: SoundService *(property, read-only)* — The service SoundService.
- **teams**: Teams *(property, read-only)* — The service Teams.

### Workspace

The 3D world: everything inside is visible and has physics.

Inherits from **Instance**. Area: 3D. 

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **gravity**: number *(property)* — Gravity in studs/s² (196.2 by default).
- **fallenPartsDestroyHeight**: number *(property)* — Parts falling below this height are destroyed.
- **currentCamera**: any *(property)* — Active camera.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **raycast**(origin: Vec3, direction: Vec3, ignore?: any): map? *(method)* — Casts a ray (its length is that of 'direction'). Returns {instance, position, normal, distance} or null.

### Workspace2D

The 2D world: sprites and text with 2D physics (Box2D). Coordinates in pixels, Y pointing down.

Inherits from **Instance**. Area: 2D. 

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **gravity**: Vec2 *(property)* — 2D gravity in pixels/s².
- **backgroundColor**: Color *(property)* — Background colour of the 2D scene.
- **renderMode**: text *(property)* — How it blends with the 3D world.
- **cameraPosition**: Vec2 *(property)* — 2D camera centre.
- **cameraZoom**: number *(property)* — 2D camera zoom.
- **cameraTarget**: any *(property)* — Sprite the camera follows (optional).
- **pixelsPerMeter**: number *(property)* — 2D physics scale.
- **virtualResolution**: Vec2 *(property)* — Internal game resolution (0 = the window size). Pixel art: 320x180, 480x270, 640x360.
- **pixelPerfect**: bool *(property)* — Integer scaling without smoothing (crisp pixel art).
- **defaultFilter**: text *(property)* — Filtering of images with filter = Auto.
- **ambientColor**: Color *(property)* — 2D ambient light (white = no darkness; darker = Light2D stands out).
- **bloom**: bool *(property)* — Glow of bright things (emission, particles, lights).
- **bloomIntensity**: number *(property)* — Glow strength.
- **bloomThreshold**: number *(property)* — Brightness above which it glows.
- **vignette**: number *(property)* — Darkens the edges.
- **chromaticAberration**: number *(property)* — Colour separation at the edges.
- **scanlines**: number *(property)* — Old TV scanlines (CRT).
- **grain**: number *(property)* — Film grain.
- **pixelate**: number *(property)* — Pixelate the image (pixel size; 0 = off).
- **exposure**: number *(property)* — Brillo general.
- **contrast**: number *(property)* — Contraste (1 = neutro).
- **saturation**: number *(property)* — Saturation (0 = black and white).
- **tint**: Color *(property)* — Tint of the whole image.
- **smoothScroll**: bool *(property)* — With pixelPerfect: the camera slides in screen pixels even when the art uses big pixels (no stutter while moving).
- **timeScale**: number *(property)* — 2D time speed (physics, animations and particles): 0.3 = slow motion, 0 = frozen.
- **flashColor**: Color *(property)* — Screen flash colour (World2D.flash).
- **flashAmount**: number *(property)* — Full-screen flash (0..1).
- **fadeColor**: Color *(property)* — Fade colour (World2D.fadeOut / fadeIn).
- **fadeAmount**: number *(property)* — Fundido a fadeColor (0..1): transiciones.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **raycast**(origin: Vec2, direction: Vec2, ignore?: any): map? *(method)* — 2D ray (its length is that of 'direction'). Returns {instance, position, normal, distance} or null.
- **overlapPoint**(point: Vec2): list *(method)* — Objects with 2D physics at a point.

### Lighting

Lighting, sky, fog and time of day.

Inherits from **Instance**. Area: 3D. 

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **ambient**: Color *(property)* — Ambient light (shaded areas).
- **brightness**: number *(property)* — Sun intensity.
- **clockTime**: number *(property)* — Time of day (0-24): moves the sun.
- **skyTopColor**: Color *(property)* — Sky colour at the top.
- **skyHorizonColor**: Color *(property)* — Horizon colour.
- **sunColor**: Color *(property)* — Sunlight colour.
- **fogColor**: Color *(property)* — Fog colour.
- **fogStart**: number *(property)* — Distance where the fog starts.
- **fogEnd**: number *(property)* — Distance of full fog.
- **globalShadows**: bool *(property)* — Sun shadows.
- **exposure**: number *(property)* — Camera exposure.
- **bloom**: bool *(property)* — Glow around bright areas (Neon).
- **bloomIntensity**: number *(property)* — Glow strength.
- **contrast**: number *(property)* — Image contrast (1 = neutral).
- **saturation**: number *(property)* — Colour saturation (0 = black and white).
- **vignette**: number *(property)* — Screen edge darkening.
- **tint**: Color *(property)* — Colour tint of the whole image.
- **shadowSoftness**: number *(property)* — Shadow edge softness.
- **ambientOcclusion**: number *(property)* — Contact shadow in corners and at the base of objects.
- **sunSize**: number *(property)* — Sun disc size.
- **chromaticAberration**: number *(property)* — Colour separation at the edges.
- **grain**: number *(property)* — Film grain.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### Players

The connected players.

Inherits from **Instance**. Area: Players. 

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **maxPlayers**: number *(property)* — Maximum players per server.
- **respawnTime**: number *(property)* — Seconds until respawning.
- **characterAutoLoads**: bool *(property)* — Create the character automatically.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **playerAdded**: Event *(event)* — A player joined. Data: player: any.
- **playerRemoving**: Event *(event)* — A player leaves. Data: player: any.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **getPlayers**(): list *(method)* — Connected players.
- **playerFromCharacter**(character: any): any *(method)* — Player who owns a character (or null).
- **localPlayer**: any *(property, read-only)* — (Client) The player on this computer.

### Player

A connected player (created while playing).

Inherits from **Instance**. Area: Players. 

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **userId**: number *(property, read-only)* — Player identifier.
- **displayName**: text *(property)* — Display name.
- **character**: any *(property)* — Character model.
- **team**: any *(property)* — The player's team.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **kick**(reason?: text): void *(method)* — (Server) Kicks the player.
- **playerGui**: any *(property, read-only)* — Folder with the player interface.

### StarterPlayer

Character settings and player scripts (client).

Inherits from **Instance**. Area: Client. 

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **characterWalkSpeed**: number *(property)* — Walk speed.
- **characterJumpPower**: number *(property)* — Jump strength.
- **cameraMaxZoomDistance**: number *(property)* — Maximum zoom.
- **cameraMinZoomDistance**: number *(property)* — Minimum zoom.
- **cameraMode**: text *(property)* — Camera mode.
- **rigType**: text *(property)* — Skeleton: R15 (articulated, realistic animation) or R6 (classic).
- **headColor**: Color *(property)* — Head colour.
- **torsoColor**: Color *(property)* — Torso colour.
- **armsColor**: Color *(property)* — Arm colour.
- **legsColor**: Color *(property)* — Leg colour.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### StarterPlayerScripts

LocalScripts copied to each player on joining (client).

Inherits from **Instance**. Area: Client. 

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### StarterCharacterScripts

LocalScripts copied to the character every time it spawns.

Inherits from **Instance**. Area: Client. 

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### StarterGui

Interface copied to each player (client).

Inherits from **Instance**. Area: Client. 

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### ReplicatedStorage

Objects and modules shared by server and clients.

Inherits from **Instance**. Area: Shared. 

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### ServerScriptService

Server scripts (clients do not see them).

Inherits from **Instance**. Area: Server. 

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### ServerStorage

Objects only the server sees.

Inherits from **Instance**. Area: Server. 

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### SoundService

Global music and sounds.

Inherits from **Instance**. Area: Audio. 

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### Teams

Player teams.

Inherits from **Instance**. Area: Players. 

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### Folder

Folder to organise objects.

Inherits from **Instance**. Area: General. Created with `Folder(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### Model

Groups parts to move them together (a car, a house, a character).

Inherits from **Instance**. Area: 3D. Created with `Model(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **primaryPart**: any *(property)* — Primary part (model centre).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **getPivot**(): Vec3 *(method)* — Model centre (or its primaryPart).
- **moveTo**(position: Vec3): void *(method)* — Moves the whole model so its centre ends at 'position'.
- **getBoundingBox**(): map *(method)* — Bounding box: {center, size}.

### BasePart

Base of every 3D part with physics.

Inherits from **Instance**. Area: 3D. 

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec3 *(property)* — Centre position (studs).
- **rotation**: Vec3 *(property)* — Rotation in degrees (X, Y, Z).
- **size**: Vec3 *(property)* — Size (studs).
- **color**: Color *(property)* — Color.
- **material**: text *(property)* — Material.
- **transparency**: number *(property)* — 0 opaca, 1 invisible.
- **reflectance**: number *(property)* — Sky reflection (0-1).
- **castShadow**: bool *(property)* — Casts a shadow.
- **anchored**: bool *(property)* — Anchored: physics does not move it.
- **canCollide**: bool *(property)* — Collides with other parts.
- **canTouch**: bool *(property)* — Fires the touched/touchEnded events.
- **locked**: bool *(property)* — It cannot be selected with the mouse in the editor.
- **friction**: number *(property)* — Rozamiento (0-2).
- **elasticity**: number *(property)* — Rebote (0-1).
- **density**: number *(property)* — Density (mass per volume).
- **velocity**: Vec3 *(property)* — Linear velocity (studs/s).
- **angularVelocity**: Vec3 *(property)* — Angular velocity (rad/s).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **touched**: Event *(event)* — Another part started touching this one. Data: other: any.
- **touchEnded**: Event *(event)* — Another part stopped touching it. Data: other: any.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **applyImpulse**(impulse: Vec3): void *(method)* — Pushes the part (not anchored).
- **getMass**(): number *(method)* — Part mass.
- **lookAt**(target: Vec3): void *(method)* — Rotates the part so its front (-Z) faces the point.
- **getTouchingParts**(): list *(method)* — Parts touching it right now (while playing).

### Part

Basic part: block, sphere, cylinder or wedge.

Inherits from **BasePart**. Area: 3D. Created with `Part(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec3 *(property)* — Centre position (studs).
- **rotation**: Vec3 *(property)* — Rotation in degrees (X, Y, Z).
- **size**: Vec3 *(property)* — Size (studs).
- **color**: Color *(property)* — Color.
- **material**: text *(property)* — Material.
- **transparency**: number *(property)* — 0 opaca, 1 invisible.
- **reflectance**: number *(property)* — Sky reflection (0-1).
- **castShadow**: bool *(property)* — Casts a shadow.
- **anchored**: bool *(property)* — Anchored: physics does not move it.
- **canCollide**: bool *(property)* — Collides with other parts.
- **canTouch**: bool *(property)* — Fires the touched/touchEnded events.
- **locked**: bool *(property)* — It cannot be selected with the mouse in the editor.
- **friction**: number *(property)* — Rozamiento (0-2).
- **elasticity**: number *(property)* — Rebote (0-1).
- **density**: number *(property)* — Density (mass per volume).
- **velocity**: Vec3 *(property)* — Linear velocity (studs/s).
- **angularVelocity**: Vec3 *(property)* — Angular velocity (rad/s).
- **shape**: text *(property)* — Forma.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **touched**: Event *(event)* — Another part started touching this one. Data: other: any.
- **touchEnded**: Event *(event)* — Another part stopped touching it. Data: other: any.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **applyImpulse**(impulse: Vec3): void *(method)* — Pushes the part (not anchored).
- **getMass**(): number *(method)* — Part mass.
- **lookAt**(target: Vec3): void *(method)* — Rotates the part so its front (-Z) faces the point.
- **getTouchingParts**(): list *(method)* — Parts touching it right now (while playing).

### SpawnLocation

Point where players spawn.

Inherits from **Part**. Area: 3D. Created with `SpawnLocation(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec3 *(property)* — Centre position (studs).
- **rotation**: Vec3 *(property)* — Rotation in degrees (X, Y, Z).
- **size**: Vec3 *(property)* — Size (studs).
- **color**: Color *(property)* — Color.
- **material**: text *(property)* — Material.
- **transparency**: number *(property)* — 0 opaca, 1 invisible.
- **reflectance**: number *(property)* — Sky reflection (0-1).
- **castShadow**: bool *(property)* — Casts a shadow.
- **anchored**: bool *(property)* — Anchored: physics does not move it.
- **canCollide**: bool *(property)* — Collides with other parts.
- **canTouch**: bool *(property)* — Fires the touched/touchEnded events.
- **locked**: bool *(property)* — It cannot be selected with the mouse in the editor.
- **friction**: number *(property)* — Rozamiento (0-2).
- **elasticity**: number *(property)* — Rebote (0-1).
- **density**: number *(property)* — Density (mass per volume).
- **velocity**: Vec3 *(property)* — Linear velocity (studs/s).
- **angularVelocity**: Vec3 *(property)* — Angular velocity (rad/s).
- **shape**: text *(property)* — Forma.
- **enabled**: bool *(property)* — Players can spawn here.
- **neutral**: bool *(property)* — Any team can spawn here.
- **team**: any *(property)* — Team that spawns here.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **touched**: Event *(event)* — Another part started touching this one. Data: other: any.
- **touchEnded**: Event *(event)* — Another part stopped touching it. Data: other: any.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **applyImpulse**(impulse: Vec3): void *(method)* — Pushes the part (not anchored).
- **getMass**(): number *(method)* — Part mass.
- **lookAt**(target: Vec3): void *(method)* — Rotates the part so its front (-Z) faces the point.
- **getTouchingParts**(): list *(method)* — Parts touching it right now (while playing).

### MeshPart

Part with an imported mesh (OBJ, glTF/GLB).

Inherits from **BasePart**. Area: 3D. Created with `MeshPart(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec3 *(property)* — Centre position (studs).
- **rotation**: Vec3 *(property)* — Rotation in degrees (X, Y, Z).
- **size**: Vec3 *(property)* — Size (studs).
- **color**: Color *(property)* — Color.
- **material**: text *(property)* — Material.
- **transparency**: number *(property)* — 0 opaca, 1 invisible.
- **reflectance**: number *(property)* — Sky reflection (0-1).
- **castShadow**: bool *(property)* — Casts a shadow.
- **anchored**: bool *(property)* — Anchored: physics does not move it.
- **canCollide**: bool *(property)* — Collides with other parts.
- **canTouch**: bool *(property)* — Fires the touched/touchEnded events.
- **locked**: bool *(property)* — It cannot be selected with the mouse in the editor.
- **friction**: number *(property)* — Rozamiento (0-2).
- **elasticity**: number *(property)* — Rebote (0-1).
- **density**: number *(property)* — Density (mass per volume).
- **velocity**: Vec3 *(property)* — Linear velocity (studs/s).
- **angularVelocity**: Vec3 *(property)* — Angular velocity (rad/s).
- **meshId**: text *(property)* — Mesh asset.
- **textureId**: text *(property)* — Texture (image).
- **meshData**: text *(property)* — Malla incrustada.
- **doubleSided**: bool *(property)* — Draw both faces.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **touched**: Event *(event)* — Another part started touching this one. Data: other: any.
- **touchEnded**: Event *(event)* — Another part stopped touching it. Data: other: any.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **applyImpulse**(impulse: Vec3): void *(method)* — Pushes the part (not anchored).
- **getMass**(): number *(method)* — Part mass.
- **lookAt**(target: Vec3): void *(method)* — Rotates the part so its front (-Z) faces the point.
- **getTouchingParts**(): list *(method)* — Parts touching it right now (while playing).

### UnionOperation

Result of a part Union/Subtract (CSG). Contains the original parts.

Inherits from **MeshPart**. Area: 3D. Created with `UnionOperation(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec3 *(property)* — Centre position (studs).
- **rotation**: Vec3 *(property)* — Rotation in degrees (X, Y, Z).
- **size**: Vec3 *(property)* — Size (studs).
- **color**: Color *(property)* — Color.
- **material**: text *(property)* — Material.
- **transparency**: number *(property)* — 0 opaca, 1 invisible.
- **reflectance**: number *(property)* — Sky reflection (0-1).
- **castShadow**: bool *(property)* — Casts a shadow.
- **anchored**: bool *(property)* — Anchored: physics does not move it.
- **canCollide**: bool *(property)* — Collides with other parts.
- **canTouch**: bool *(property)* — Fires the touched/touchEnded events.
- **locked**: bool *(property)* — It cannot be selected with the mouse in the editor.
- **friction**: number *(property)* — Rozamiento (0-2).
- **elasticity**: number *(property)* — Rebote (0-1).
- **density**: number *(property)* — Density (mass per volume).
- **velocity**: Vec3 *(property)* — Linear velocity (studs/s).
- **angularVelocity**: Vec3 *(property)* — Angular velocity (rad/s).
- **meshId**: text *(property)* — Mesh asset.
- **textureId**: text *(property)* — Texture (image).
- **meshData**: text *(property)* — Malla incrustada.
- **doubleSided**: bool *(property)* — Draw both faces.
- **usePartColor**: bool *(property)* — Uses the colour of the union instead of the originals.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **touched**: Event *(event)* — Another part started touching this one. Data: other: any.
- **touchEnded**: Event *(event)* — Another part stopped touching it. Data: other: any.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **applyImpulse**(impulse: Vec3): void *(method)* — Pushes the part (not anchored).
- **getMass**(): number *(method)* — Part mass.
- **lookAt**(target: Vec3): void *(method)* — Rotates the part so its front (-Z) faces the point.
- **getTouchingParts**(): list *(method)* — Parts touching it right now (while playing).

### Camera

3D camera.

Inherits from **Instance**. Area: 3D. Created with `Camera(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec3 *(property)* — Position.
- **rotation**: Vec3 *(property)* — Rotation in degrees (pitch, yaw, roll).
- **fieldOfView**: number *(property)* — Vertical field of view (degrees).
- **cameraType**: text *(property)* — Custom follows the character; Scriptable is controlled by your script.
- **subject**: any *(property)* — What it follows (the character by default).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **lookAt**(target: Vec3): void *(method)* — Points the camera at a point.

### Light

Base of the lights.

Inherits from **Instance**. Area: 3D. 

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **color**: Color *(property)* — Light colour.
- **brightness**: number *(property)* — Intensidad.
- **range**: number *(property)* — Alcance (studs).
- **enabled**: bool *(property)* — Encendida.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### PointLight

Light in every direction (inside a part).

Inherits from **Light**. Area: 3D. Created with `PointLight(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **color**: Color *(property)* — Light colour.
- **brightness**: number *(property)* — Intensidad.
- **range**: number *(property)* — Alcance (studs).
- **enabled**: bool *(property)* — Encendida.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### SpotLight

Spotlight: lights forward (-Z) from its part.

Inherits from **Light**. Area: 3D. Created with `SpotLight(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **color**: Color *(property)* — Light colour.
- **brightness**: number *(property)* — Intensidad.
- **range**: number *(property)* — Alcance (studs).
- **enabled**: bool *(property)* — Encendida.
- **angle**: number *(property)* — Cone angle (degrees).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### ParticleEmitter

Emits particles (fire, smoke, sparks) from its part.

Inherits from **Instance**. Area: 3D. Created with `ParticleEmitter(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **enabled**: bool *(property)* — Emits particles.
- **rate**: number *(property)* — Particles per second.
- **lifetime**: Vec2 *(property)* — Minimum and maximum lifetime (s).
- **speed**: Vec2 *(property)* — Minimum and maximum speed.
- **spreadAngle**: number *(property)* — Spread (degrees).
- **acceleration**: Vec3 *(property)* — Acceleration (for example gravity or wind).
- **color**: Color *(property)* — Initial colour.
- **colorEnd**: Color *(property)* — Final colour.
- **sizeRange**: Vec2 *(property)* — Start and end size.
- **texture**: text *(property)* — Particle image (optional).
- **lightEmission**: number *(property)* — Brillo aditivo (0-1).
- **transparency**: number *(property)* — Transparencia.
- **burst**: number *(property)* — Burst particles on start (and with emit()).
- **maxParticles**: number *(property)* — Maximum live particles.
- **drag**: number *(property)* — Air drag.
- **spin**: Vec2 *(property)* — Minimum and maximum spin (degrees/s).
- **blendMode**: text *(property)* — Additive adds light (fire, magic); Normal covers (smoke, dust).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **emit**(count: number = 10): void *(method)* — Emits a burst of particles (explosions, impacts).

### WeldConstraint

Joins two parts so they move together.

Inherits from **Instance**. Area: 3D. Created with `WeldConstraint(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **part0**: any *(property)* — First part.
- **part1**: any *(property)* — Second part.
- **enabled**: bool *(property)* — Activa.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### ClickDetector

Makes its part clickable with the mouse.

Inherits from **Instance**. Area: 3D. Created with `ClickDetector(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **maxActivationDistance**: number *(property)* — Maximum distance.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **mouseClick**: Event *(event)* — A player clicked the part. Data: player: any.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### Humanoid

Health and movement of a character.

Inherits from **Instance**. Area: 3D. Created with `Humanoid(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **walkSpeed**: number *(property)* — Walk speed (studs/s).
- **jumpPower**: number *(property)* — Initial jump speed.
- **health**: number *(property)* — Current health.
- **maxHealth**: number *(property)* — Maximum health.
- **displayName**: text *(property)* — Name shown above the head.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **died**: Event *(event)* — Health reached 0.
- **healthChanged**: Event *(event)* — Health changed. Data: health: number.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **takeDamage**(amount: number): void *(method)* — Takes health.
- **moveTo**(position: Vec3): void *(method)* — Walks to a point.
- **jump**(): void *(method)* — Jumps (if on the ground).

### LuaSourceContainer

Base of the scripts.

Inherits from **Instance**. Area: General. 

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **source**: text *(property)* — HyperEZ code.
- **enabled**: bool *(property)* — Runs when playing.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### Script

SERVER script (HyperEZ). It goes in ServerScriptService or in Workspace.

Inherits from **LuaSourceContainer**. Area: Scripts. Created with `Script(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **source**: text *(property)* — HyperEZ code.
- **enabled**: bool *(property)* — Runs when playing.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### LocalScript

CLIENT script (HyperEZ): input, camera, interface. It goes in StarterPlayerScripts, StarterGui or StarterCharacterScripts.

Inherits from **LuaSourceContainer**. Area: Scripts. Created with `LocalScript(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **source**: text *(property)* — HyperEZ code.
- **enabled**: bool *(property)* — Runs when playing.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### ModuleScript

Reusable HyperEZ module: used with import (for example import ReplicatedStorage.Utilities).

Inherits from **LuaSourceContainer**. Area: Scripts. Created with `ModuleScript(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **source**: text *(property)* — HyperEZ code.
- **enabled**: bool *(property)* — Runs when playing.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### TouchScript

ON TOUCH script (server). Put it inside a part: its code runs every time a player touches it. Ready variables: part, player (who touches it) and character (their body).

Inherits from **Script**. Area: Scripts. Created with `TouchScript(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **source**: text *(property)* — HyperEZ code.
- **enabled**: bool *(property)* — Runs when playing.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### ClickScript

ON CLICK script (server). Put it inside a part: its code runs when a player clicks it. Ready variables: part and player.

Inherits from **Script**. Area: Scripts. Created with `ClickScript(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **source**: text *(property)* — HyperEZ code.
- **enabled**: bool *(property)* — Runs when playing.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### TimerScript

TIMER script (server): its code repeats every 'interval' seconds while the game runs. Ready variable: tick (1, 2, 3...).

Inherits from **Script**. Area: Scripts. Created with `TimerScript(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **source**: text *(property)* — HyperEZ code.
- **enabled**: bool *(property)* — Runs when playing.
- **interval**: number *(property)* — Seconds between repetitions (0.03 minimum).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### PlayerScript

PER PLAYER script (server): its code runs once for every player who joins. Ready variable: player.

Inherits from **Script**. Area: Scripts. Created with `PlayerScript(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **source**: text *(property)* — HyperEZ code.
- **enabled**: bool *(property)* — Runs when playing.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### GuiScript

INTERFACE script (client). Put it inside a ScreenGui or an element: it controls that interface on each player's screen. Ready variables: gui (what contains the script) and player.

Inherits from **LocalScript**. Area: Scripts. Created with `GuiScript(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **source**: text *(property)* — HyperEZ code.
- **enabled**: bool *(property)* — Runs when playing.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### ButtonScript

ON PRESS script (client). Put it inside a TextButton or ImageButton: its code runs every time the player presses it. Ready variables: button and player.

Inherits from **LocalScript**. Area: Scripts. Created with `ButtonScript(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **source**: text *(property)* — HyperEZ code.
- **enabled**: bool *(property)* — Runs when playing.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### ValueBase

Base of the values.

Inherits from **Instance**. Area: General. 

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### StringValue

Stores a text.

Inherits from **ValueBase**. Area: General. Created with `StringValue(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **value**: text *(property)* — Valor.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### NumberValue

Stores a number.

Inherits from **ValueBase**. Area: General. Created with `NumberValue(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **value**: number *(property)* — Valor.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### BoolValue

Guarda verdadero/falso.

Inherits from **ValueBase**. Area: General. Created with `BoolValue(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **value**: bool *(property)* — Valor.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### Vector3Value

Stores a Vec3.

Inherits from **ValueBase**. Area: General. Created with `Vector3Value(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **value**: Vec3 *(property)* — Valor.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### ColorValue

Stores a colour.

Inherits from **ValueBase**. Area: General. Created with `ColorValue(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **value**: Color *(property)* — Valor.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### ObjectValue

Stores a reference to another instance.

Inherits from **ValueBase**. Area: General. Created with `ObjectValue(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **value**: any *(property)* — Instancia.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### RemoteEvent

Messages between server and clients (fireServer, fireClient, fireAllClients).

Inherits from **Instance**. Area: Shared. Created with `RemoteEvent(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **onServerEvent**: Event *(event)* — (Server) A client called fireServer (value: the data sent). Data: player: any, value: any.
- **onClientEvent**: Event *(event)* — (Client) The server called fireClient/fireAllClients. Data: value: any.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **fireServer**(value?: any): void *(method)* — (Client) Sends a message to the server.
- **fireClient**(player: any, value?: any): void *(method)* — (Server) Sends a message to one player.
- **fireAllClients**(value?: any): void *(method)* — (Server) Sends a message to every player.

### BindableEvent

Event between scripts on the same side (server-server or client-client).

Inherits from **Instance**. Area: General. Created with `BindableEvent(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **event**: Event *(event)* — Someone called fire(value). Data: value: any.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **fire**(value?: any): void *(method)* — Fires the event 'event' on this side.

### Sound

Sound or music. Inside a part it plays in 3D.

Inherits from **Instance**. Area: Audio. Created with `Sound(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **soundId**: text *(property)* — Sound asset (WAV, OGG, MP3) or a Music studio song.
- **volume**: number *(property)* — Volume (0-10).
- **playbackSpeed**: number *(property)* — Speed (changes the pitch).
- **looped**: bool *(property)* — Repeat when finished.
- **playing**: bool *(property)* — Playing (if active at the start, it plays).
- **rollOffMaxDistance**: number *(property)* — Distance at which it can no longer be heard (3D).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **ended**: Event *(event)* — Finished playing.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **play**(): void *(method)* — Empieza a sonar.
- **stop**(): void *(method)* — Stops and goes back to the start.
- **pause**(): void *(method)* — Pausa.
- **isPlaying**: bool *(property, read-only)* — Is it playing?
- **timeLength**: number *(property, read-only)* — Duration in seconds.

### Animation

Keyframe animation of its model's properties (Animation editor).

Inherits from **Instance**. Area: 3D. Created with `Animation(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **data**: text *(property)* — Tracks and keyframes (JSON).
- **looped**: bool *(property)* — Repetir.
- **speed**: number *(property)* — Playback speed.
- **autoPlay**: bool *(property)* — Starts by itself when playing.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **ended**: Event *(event)* — Finished (if it does not loop).
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **play**(): void *(method)* — Plays the animation.
- **stop**(): void *(method)* — Stops the animation.
- **isPlaying**: bool *(property, read-only)* — Is it playing?

### Team

A team of players.

Inherits from **Instance**. Area: Players. Created with `Team(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **teamColor**: Color *(property)* — Team colour.
- **autoAssignable**: bool *(property)* — Players are assigned automatically.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### ScreenGui

Interface layer on screen (inside StarterGui).

Inherits from **Instance**. Area: GUI. Created with `ScreenGui(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **enabled**: bool *(property)* — Visible.
- **displayOrder**: number *(property)* — Drawing order (higher = on top).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### GuiObject

Base of the interface elements.

Inherits from **Instance**. Area: GUI. 

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec2 *(property)* — Position relative to the parent (0-1).
- **positionOffset**: Vec2 *(property)* — Offset in pixels.
- **size**: Vec2 *(property)* — Size relative to the parent (0-1).
- **sizeOffset**: Vec2 *(property)* — Extra size in pixels.
- **anchorPoint**: Vec2 *(property)* — Anchor point (0,0 corner; 0.5,0.5 centre).
- **backgroundColor**: Color *(property)* — Background colour.
- **backgroundTransparency**: number *(property)* — Background transparency.
- **borderColor**: Color *(property)* — Border colour.
- **borderSize**: number *(property)* — Border width (px).
- **cornerRadius**: number *(property)* — Esquinas redondeadas (px).
- **visible**: bool *(property)* — Visible.
- **zIndex**: number *(property)* — Order among siblings.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **mouseEnter**: Event *(event)* — The mouse entered.
- **mouseLeave**: Event *(event)* — The mouse left.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### Frame

Interface rectangle (container).

Inherits from **GuiObject**. Area: GUI. Created with `Frame(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec2 *(property)* — Position relative to the parent (0-1).
- **positionOffset**: Vec2 *(property)* — Offset in pixels.
- **size**: Vec2 *(property)* — Size relative to the parent (0-1).
- **sizeOffset**: Vec2 *(property)* — Extra size in pixels.
- **anchorPoint**: Vec2 *(property)* — Anchor point (0,0 corner; 0.5,0.5 centre).
- **backgroundColor**: Color *(property)* — Background colour.
- **backgroundTransparency**: number *(property)* — Background transparency.
- **borderColor**: Color *(property)* — Border colour.
- **borderSize**: number *(property)* — Border width (px).
- **cornerRadius**: number *(property)* — Esquinas redondeadas (px).
- **visible**: bool *(property)* — Visible.
- **zIndex**: number *(property)* — Order among siblings.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **mouseEnter**: Event *(event)* — The mouse entered.
- **mouseLeave**: Event *(event)* — The mouse left.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### TextLabel

On-screen text.

Inherits from **GuiObject**. Area: GUI. Created with `TextLabel(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec2 *(property)* — Position relative to the parent (0-1).
- **positionOffset**: Vec2 *(property)* — Offset in pixels.
- **size**: Vec2 *(property)* — Size relative to the parent (0-1).
- **sizeOffset**: Vec2 *(property)* — Extra size in pixels.
- **anchorPoint**: Vec2 *(property)* — Anchor point (0,0 corner; 0.5,0.5 centre).
- **backgroundColor**: Color *(property)* — Background colour.
- **backgroundTransparency**: number *(property)* — Background transparency.
- **borderColor**: Color *(property)* — Border colour.
- **borderSize**: number *(property)* — Border width (px).
- **cornerRadius**: number *(property)* — Esquinas redondeadas (px).
- **visible**: bool *(property)* — Visible.
- **zIndex**: number *(property)* — Order among siblings.
- **text**: text *(property)* — Texto.
- **textColor**: Color *(property)* — Text colour.
- **textSize**: number *(property)* — Font size (px).
- **textTransparency**: number *(property)* — Text transparency.
- **textXAlignment**: text *(property)* — Horizontal alignment.
- **textYAlignment**: text *(property)* — Vertical alignment.
- **textWrapped**: bool *(property)* — Split into several lines.
- **bold**: bool *(property)* — Negrita (simulada).
- **font**: text *(property)* — Imported font (TTF/OTF); empty = the engine font.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **mouseEnter**: Event *(event)* — The mouse entered.
- **mouseLeave**: Event *(event)* — The mouse left.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### TextButton

Button with text.

Inherits from **TextLabel**. Area: GUI. Created with `TextButton(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec2 *(property)* — Position relative to the parent (0-1).
- **positionOffset**: Vec2 *(property)* — Offset in pixels.
- **size**: Vec2 *(property)* — Size relative to the parent (0-1).
- **sizeOffset**: Vec2 *(property)* — Extra size in pixels.
- **anchorPoint**: Vec2 *(property)* — Anchor point (0,0 corner; 0.5,0.5 centre).
- **backgroundColor**: Color *(property)* — Background colour.
- **backgroundTransparency**: number *(property)* — Background transparency.
- **borderColor**: Color *(property)* — Border colour.
- **borderSize**: number *(property)* — Border width (px).
- **cornerRadius**: number *(property)* — Esquinas redondeadas (px).
- **visible**: bool *(property)* — Visible.
- **zIndex**: number *(property)* — Order among siblings.
- **text**: text *(property)* — Texto.
- **textColor**: Color *(property)* — Text colour.
- **textSize**: number *(property)* — Font size (px).
- **textTransparency**: number *(property)* — Text transparency.
- **textXAlignment**: text *(property)* — Horizontal alignment.
- **textYAlignment**: text *(property)* — Vertical alignment.
- **textWrapped**: bool *(property)* — Split into several lines.
- **bold**: bool *(property)* — Negrita (simulada).
- **font**: text *(property)* — Imported font (TTF/OTF); empty = the engine font.
- **autoButtonColor**: bool *(property)* — Darken on hover/press.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **mouseEnter**: Event *(event)* — The mouse entered.
- **mouseLeave**: Event *(event)* — The mouse left.
- **activated**: Event *(event)* — The button was pressed.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### TextBox

Text input box.

Inherits from **TextLabel**. Area: GUI. Created with `TextBox(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec2 *(property)* — Position relative to the parent (0-1).
- **positionOffset**: Vec2 *(property)* — Offset in pixels.
- **size**: Vec2 *(property)* — Size relative to the parent (0-1).
- **sizeOffset**: Vec2 *(property)* — Extra size in pixels.
- **anchorPoint**: Vec2 *(property)* — Anchor point (0,0 corner; 0.5,0.5 centre).
- **backgroundColor**: Color *(property)* — Background colour.
- **backgroundTransparency**: number *(property)* — Background transparency.
- **borderColor**: Color *(property)* — Border colour.
- **borderSize**: number *(property)* — Border width (px).
- **cornerRadius**: number *(property)* — Esquinas redondeadas (px).
- **visible**: bool *(property)* — Visible.
- **zIndex**: number *(property)* — Order among siblings.
- **text**: text *(property)* — Texto.
- **textColor**: Color *(property)* — Text colour.
- **textSize**: number *(property)* — Font size (px).
- **textTransparency**: number *(property)* — Text transparency.
- **textXAlignment**: text *(property)* — Horizontal alignment.
- **textYAlignment**: text *(property)* — Vertical alignment.
- **textWrapped**: bool *(property)* — Split into several lines.
- **bold**: bool *(property)* — Negrita (simulada).
- **font**: text *(property)* — Imported font (TTF/OTF); empty = the engine font.
- **placeholderText**: text *(property)* — Hint text when it is empty.
- **clearTextOnFocus**: bool *(property)* — Clear when typing starts.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **mouseEnter**: Event *(event)* — The mouse entered.
- **mouseLeave**: Event *(event)* — The mouse left.
- **focusLost**: Event *(event)* — Typing finished (enterPressed = Enter was pressed). Data: enterPressed: bool.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### ImageLabel

On-screen image.

Inherits from **GuiObject**. Area: GUI. Created with `ImageLabel(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec2 *(property)* — Position relative to the parent (0-1).
- **positionOffset**: Vec2 *(property)* — Offset in pixels.
- **size**: Vec2 *(property)* — Size relative to the parent (0-1).
- **sizeOffset**: Vec2 *(property)* — Extra size in pixels.
- **anchorPoint**: Vec2 *(property)* — Anchor point (0,0 corner; 0.5,0.5 centre).
- **backgroundColor**: Color *(property)* — Background colour.
- **backgroundTransparency**: number *(property)* — Background transparency.
- **borderColor**: Color *(property)* — Border colour.
- **borderSize**: number *(property)* — Border width (px).
- **cornerRadius**: number *(property)* — Esquinas redondeadas (px).
- **visible**: bool *(property)* — Visible.
- **zIndex**: number *(property)* — Order among siblings.
- **image**: text *(property)* — Image asset.
- **imageColor**: Color *(property)* — Tinte.
- **imageTransparency**: number *(property)* — Transparencia.
- **scaleType**: text *(property)* — Ajuste.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **mouseEnter**: Event *(event)* — The mouse entered.
- **mouseLeave**: Event *(event)* — The mouse left.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### ImageButton

Button with an image.

Inherits from **ImageLabel**. Area: GUI. Created with `ImageButton(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec2 *(property)* — Position relative to the parent (0-1).
- **positionOffset**: Vec2 *(property)* — Offset in pixels.
- **size**: Vec2 *(property)* — Size relative to the parent (0-1).
- **sizeOffset**: Vec2 *(property)* — Extra size in pixels.
- **anchorPoint**: Vec2 *(property)* — Anchor point (0,0 corner; 0.5,0.5 centre).
- **backgroundColor**: Color *(property)* — Background colour.
- **backgroundTransparency**: number *(property)* — Background transparency.
- **borderColor**: Color *(property)* — Border colour.
- **borderSize**: number *(property)* — Border width (px).
- **cornerRadius**: number *(property)* — Esquinas redondeadas (px).
- **visible**: bool *(property)* — Visible.
- **zIndex**: number *(property)* — Order among siblings.
- **image**: text *(property)* — Image asset.
- **imageColor**: Color *(property)* — Tinte.
- **imageTransparency**: number *(property)* — Transparencia.
- **scaleType**: text *(property)* — Ajuste.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **mouseEnter**: Event *(event)* — The mouse entered.
- **mouseLeave**: Event *(event)* — The mouse left.
- **activated**: Event *(event)* — The button was pressed.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### Node2D

Base of 2D objects: position, rotation, scale, draw order and visibility.

Inherits from **Instance**. Area: 2D. 

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec2 *(property)* — Position (pixels; Y grows downwards).
- **rotation**: number *(property)* — Rotation (degrees, clockwise).
- **scale**: Vec2 *(property)* — Scale (1 = normal size; negative flips).
- **zIndex**: number *(property)* — Drawing order (higher = in front).
- **visible**: bool *(property)* — Visible (also hides its children).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **getWorldPosition**(): Vec2 *(method)* — World position (adding those of its parents).
- **lookAt**(target: Vec2): void *(method)* — Rotates the object to face a point.

### Sprite2D

Image or 2D shape with optional physics (Box2D), frame animation, outline, flash, shadow, glow and lights.

Inherits from **Node2D**. Area: 2D. Created with `Sprite2D(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec2 *(property)* — Position (pixels; Y grows downwards).
- **rotation**: number *(property)* — Rotation (degrees, clockwise).
- **scale**: Vec2 *(property)* — Scale (1 = normal size; negative flips).
- **zIndex**: number *(property)* — Drawing order (higher = in front).
- **visible**: bool *(property)* — Visible (also hides its children).
- **size**: Vec2 *(property)* — Size (pixels).
- **pivot**: Vec2 *(property)* — Pivot inside the sprite (0,0 top left corner; 0.5,0.5 centre; 0.5,1 feet).
- **image**: text *(property)* — Image (empty = coloured shape).
- **color**: Color *(property)* — Colour (or image tint).
- **transparency**: number *(property)* — Transparencia (0 opaco, 1 invisible).
- **shape**: text *(property)* — Shape (drawing without an image and collision).
- **cornerRadius**: number *(property)* — Corner radius (RoundedBox).
- **sides**: number *(property)* — Lados o puntas (Polygon, Star).
- **innerRatio**: number *(property)* — Radio interior (Star, Ring).
- **flipX**: bool *(property)* — Voltear en horizontal.
- **flipY**: bool *(property)* — Voltear en vertical.
- **blendMode**: text *(property)* — Blends with what is behind.
- **filter**: text *(property)* — Image filtering (Pixel for pixel art).
- **regionPosition**: Vec2 *(property)* — Corner of the part of the image that is used (pixels).
- **regionSize**: Vec2 *(property)* — Size of the part of the image (0 = the whole image).
- **tiling**: Vec2 *(property)* — Times the image repeats (floors, walls).
- **lit**: bool *(property)* — Affected by 2D lights and ambient light.
- **emission**: number *(property)* — Self-illumination: glows with bloom (0 = none).
- **outlineColor**: Color *(property)* — Outline colour.
- **outlineSize**: number *(property)* — Outline width (0 = no outline).
- **flashColor**: Color *(property)* — Flash colour.
- **flash**: number *(property)* — Flash 0..1 (animate it with Tween or use flashOnce).
- **shadowOpacity**: number *(property)* — Drop shadow (0 = no shadow).
- **castShadow**: bool *(property)* — Blocks the light of Light2D: casts shadows.
- **normalMap**: text *(property)* — Normal map (relief with lighting); same grid as the image.
- **relief**: number *(property)* — Automatic relief derived from the image or shape (0 = flat).
- **shadowOffset**: Vec2 *(property)* — Shadow offset (pixels).
- **shadowColor**: Color *(property)* — Shadow colour.
- **frames**: number *(property)* — Sprite sheet frames.
- **columns**: number *(property)* — Sheet columns (0 = all in one row).
- **frameRate**: number *(property)* — Frames per second (0 = still). With SpriteAnimator it is controlled by the animator.
- **frame**: number *(property)* — Current frame.
- **body**: text *(property)* — Body type: Static (ground), Dynamic (falls and collides), Kinematic (moved by you).
- **collisionSize**: Vec2 *(property)* — Collision size (0 = the sprite size).
- **collisionOffset**: Vec2 *(property)* — Collision offset.
- **friction**: number *(property)* — Rozamiento.
- **restitution**: number *(property)* — Rebote.
- **density**: number *(property)* — Density (mass).
- **fixedRotation**: bool *(property)* — Does not rotate (characters).
- **gravityScale**: number *(property)* — Gravity multiplier (0 = floats).
- **isSensor**: bool *(property)* — Detects contacts without colliding (coins, zones).
- **oneWay**: bool *(property)* — One-way platform: you can jump through it from below.
- **collisionLayer**: number *(property)* — Collision layer (1..16).
- **collisionMask**: text *(property)* — Layers it collides with: "all" or a list ("1,3").
- **linearDamping**: number *(property)* — Movement drag (air, water).
- **angularDamping**: number *(property)* — Angular drag.
- **bullet**: bool *(property)* — Continuous detection for very fast objects (bullets).
- **velocity**: Vec2 *(property)* — Speed (px/s).
- **angularVelocity**: number *(property)* — Spin speed (degrees/s).
- **onGround**: bool *(property, read-only)* — (While playing) Is it resting on something?
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **touched**: Event *(event)* — Another 2D object started touching it. Data: other: any.
- **touchEnded**: Event *(event)* — Stopped touching it. Data: other: any.
- **clicked**: Event *(event)* — (While playing) The player clicked the sprite. Data: button: number.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **applyImpulse**(impulse: Vec2): void *(method)* — Pushes the sprite at once (dynamic body).
- **applyForce**(force: Vec2): void *(method)* — Pushes the sprite gradually (call it every frame).
- **applyTorque**(torque: number): void *(method)* — Makes it spin.
- **getTouching**(): list *(method)* — 2D objects touching it now (while playing).
- **isOnGround**(): bool *(method)* — Is it resting on something? (while playing)
- **flashOnce**(duration: number = 0.15, color?: Color): Task *(method)* — Quick flash (hits, picking up items).
- **playAnimation**(name?: text): void *(method)* — Plays an animation from its SpriteAnimator ("run", "jump"...).
- **getWorldPosition**(): Vec2 *(method)* — World position (adding those of its parents).
- **lookAt**(target: Vec2): void *(method)* — Rotates the object to face a point.

### SpriteAnimator

Plays named animations ("idle", "run"...) from a sprite animation asset on the parent Sprite2D.

Inherits from **Instance**. Area: 2D. Created with `SpriteAnimator(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **animations**: text *(property)* — Animation asset (sheet, grid and clips).
- **animation**: text *(property)* — Animation being played.
- **playing**: bool *(property)* — Reproduciendo.
- **speed**: number *(property)* — Speed (1 = normal).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **finished**: Event *(event)* — A non-looping animation finished. Data: animation: text.
- **frameChanged**: Event *(event)* — Changed frame (steps, hits, sounds). Data: frame: number.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **play**(name?: text): void *(method)* — Plays an animation (without a name: restarts the current one).
- **stop**(): void *(method)* — Stops and goes back to the first frame.
- **pause**(): void *(method)* — Pausa.

### ParticleEmitter2D

2D particle effects: fire, smoke, sparks, explosions, magic, rain, snow... Choose a ready-made effect in Properties.

Inherits from **Node2D**. Area: 2D. Created with `ParticleEmitter2D(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec2 *(property)* — Position (pixels; Y grows downwards).
- **rotation**: number *(property)* — Rotation (degrees, clockwise).
- **scale**: Vec2 *(property)* — Scale (1 = normal size; negative flips).
- **zIndex**: number *(property)* — Drawing order (higher = in front).
- **visible**: bool *(property)* — Visible (also hides its children).
- **emitting**: bool *(property)* — Emitting particles.
- **rate**: number *(property)* — Particles per second.
- **burst**: number *(property)* — Burst particles on start.
- **oneShot**: bool *(property)* — Only the initial burst (explosions).
- **emissionShape**: text *(property)* — Spawn area.
- **emissionSize**: Vec2 *(property)* — Zone size (radius or width and height).
- **maxParticles**: number *(property)* — Maximum live particles.
- **localSpace**: bool *(property)* — Particles move with the emitter.
- **lifetime**: Vec2 *(property)* — Minimum and maximum lifetime (s).
- **speed**: Vec2 *(property)* — Minimum and maximum speed (px/s).
- **direction**: number *(property)* — Direction (degrees: 0 right, 90 down, -90 up).
- **spread**: number *(property)* — Spray angle (degrees; 360 = every direction).
- **gravity**: Vec2 *(property)* — Particle gravity (px/s²).
- **drag**: number *(property)* — Air drag.
- **spin**: Vec2 *(property)* — Minimum and maximum spin (degrees/s).
- **alignToVelocity**: bool *(property)* — Point each particle where it goes (sparks, rain).
- **sizeRange**: Vec2 *(property)* — Size when born and when dying (px).
- **sizeRandom**: number *(property)* — Random size variation.
- **colorStart**: Color *(property)* — Colour when born.
- **colorEnd**: Color *(property)* — Colour when dying.
- **alphaStart**: number *(property)* — Opacity when born.
- **alphaEnd**: number *(property)* — Opacity when dying.
- **particleShape**: text *(property)* — Shape of particles without an image.
- **texture**: text *(property)* — Image of each particle (optional).
- **textureFrames**: number *(property)* — Horizontal frames in the image.
- **blendMode**: text *(property)* — Blending (Additive for fire and light).
- **emission**: number *(property)* — Glow (bloom).
- **lit**: bool *(property)* — Affected by 2D lights.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **emit**(count: number = 10): void *(method)* — Emits a burst of particles (explosions, impacts).
- **clear**(): void *(method)* — Clears the live particles.
- **applyPreset**(name: text): void *(method)* — Applies a ready-made effect: fire, smoke, sparks, explosion, magic, rain, snow, dust, confetti, bubbles, fireflies, heal.
- **getWorldPosition**(): Vec2 *(method)* — World position (adding those of its parents).
- **lookAt**(target: Vec2): void *(method)* — Rotates the object to face a point.

### Tilemap2D

Tile map: choose a tile set (an image laid out in a grid) and paint the level with the tile brush. Collisions are generated automatically.

Inherits from **Node2D**. Area: 2D. Created with `Tilemap2D(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec2 *(property)* — Position (pixels; Y grows downwards).
- **rotation**: number *(property)* — Rotation (degrees, clockwise).
- **scale**: Vec2 *(property)* — Scale (1 = normal size; negative flips).
- **zIndex**: number *(property)* — Drawing order (higher = in front).
- **visible**: bool *(property)* — Visible (also hides its children).
- **tileset**: text *(property)* — Image with the tiles laid out in a grid.
- **tileSize**: Vec2 *(property)* — Size of each tile in the image (px).
- **cellSize**: Vec2 *(property)* — Size of each tile in the world (0 = the image size).
- **color**: Color *(property)* — Tinte.
- **transparency**: number *(property)* — Transparencia.
- **lit**: bool *(property)* — Affected by 2D lights.
- **collision**: bool *(property)* — Solid tiles collide.
- **solidTiles**: text *(property)* — Solid tiles: "all", "none" or a list ("0-15,20").
- **friction**: number *(property)* — Rozamiento.
- **oneWay**: bool *(property)* — Can be passed through from below (platforms).
- **collisionLayer**: number *(property)* — Collision layer (1..16).
- **castShadows**: bool *(property)* — Solid tiles block the light of Light2D (shadows).
- **relief**: number *(property)* — Automatic relief with lighting (0 = flat).
- **autotile**: text *(property)* — Auto tiles: first tile of each block of 16 variants ("0" or "0,16"). The edge is chosen automatically while painting.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **getTile**(x: number, y: number): number *(method)* — Tile at (x, y) (-1 = empty).
- **setTile**(x: number, y: number, tile: number): void *(method)* — Places a tile (-1 erases it).
- **fillRect**(x: number, y: number, w: number, h: number, tile: number): void *(method)* — Fills a rectangle of tiles.
- **clearTiles**(): void *(method)* — Clears every tile.
- **worldToCell**(point: Vec2): Vec2 *(method)* — Tile (x, y) at a world point.
- **cellToWorld**(x: number, y: number): Vec2 *(method)* — Tile centre in the world.
- **getWorldPosition**(): Vec2 *(method)* — World position (adding those of its parents).
- **lookAt**(target: Vec2): void *(method)* — Rotates the object to face a point.

### Camera2D

2D camera: follows an object smoothly, with dead zone, level bounds, zoom and shake.

Inherits from **Node2D**. Area: 2D. Created with `Camera2D(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec2 *(property)* — Position (pixels; Y grows downwards).
- **rotation**: number *(property)* — Rotation (degrees, clockwise).
- **scale**: Vec2 *(property)* — Scale (1 = normal size; negative flips).
- **zIndex**: number *(property)* — Drawing order (higher = in front).
- **visible**: bool *(property)* — Visible (also hides its children).
- **current**: bool *(property)* — It is the camera used while playing.
- **zoom**: number *(property)* — Zoom (2 = twice as close).
- **follow**: any *(property)* — Object it follows (optional).
- **smoothing**: number *(property)* — Smoothing (0 = follows instantly).
- **offset**: Vec2 *(property)* — Offset from the target.
- **deadZone**: Vec2 *(property)* — Zone (width, height) where the target moves without moving the camera.
- **limitsEnabled**: bool *(property)* — Show nothing outside the level bounds.
- **limitMin**: Vec2 *(property)* — Top left corner of the level.
- **limitMax**: Vec2 *(property)* — Bottom right corner of the level.
- **pixelSnap**: bool *(property)* — Round to whole pixels (pixel art without jitter).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **shake**(intensity: number = 8, duration: number = 0.35): void *(method)* — Shakes the camera (hits, explosions).
- **getWorldPosition**(): Vec2 *(method)* — World position (adding those of its parents).
- **lookAt**(target: Vec2): void *(method)* — Rotates the object to face a point.

### Light2D

2D light (torches, street lamps, magic). Darken the scene with Workspace2D.ambientColor so it shows.

Inherits from **Node2D**. Area: 2D. Created with `Light2D(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec2 *(property)* — Position (pixels; Y grows downwards).
- **rotation**: number *(property)* — Rotation (degrees, clockwise).
- **scale**: Vec2 *(property)* — Scale (1 = normal size; negative flips).
- **zIndex**: number *(property)* — Drawing order (higher = in front).
- **visible**: bool *(property)* — Visible (also hides its children).
- **enabled**: bool *(property)* — Encendida.
- **color**: Color *(property)* — Color.
- **energy**: number *(property)* — Intensidad.
- **radius**: number *(property)* — Alcance (px).
- **falloff**: number *(property)* — Falloff towards the edge (higher = softer edge).
- **flicker**: number *(property)* — Parpadeo (antorchas, fuego).
- **lightType**: text *(property)* — Point, Spot (aimed by rotation) or Directional (sun, moon).
- **angle**: number *(property)* — Spotlight angle (degrees).
- **halo**: number *(property)* — Light visible in the air: dust, fog and rays between the shadows.
- **height**: number *(property)* — Height above the scene: lower shows more relief.
- **castShadows**: bool *(property)* — Objects with castShadow and tiles with castShadows cast shadows.
- **shadowSoftness**: number *(property)* — 0 = hard; 1 = very soft far from the object.
- **shadowStrength**: number *(property)* — 0 = no shadow; 1 = black.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **getWorldPosition**(): Vec2 *(method)* — World position (adding those of its parents).
- **lookAt**(target: Vec2): void *(method)* — Rotates the object to face a point.

### Layer2D

2D layer: groups objects to order (layer zIndex), hide or lock them together, with parallax, opacity and tint.

Inherits from **Node2D**. Area: 2D. Created with `Layer2D(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec2 *(property)* — Position (pixels; Y grows downwards).
- **rotation**: number *(property)* — Rotation (degrees, clockwise).
- **scale**: Vec2 *(property)* — Scale (1 = normal size; negative flips).
- **zIndex**: number *(property)* — Drawing order (higher = in front).
- **visible**: bool *(property)* — Visible (also hides its children).
- **opacity**: number *(property)* — Opacity of everything inside.
- **tint**: Color *(property)* — Tint of everything inside.
- **parallax**: Vec2 *(property)* — 1 = with the world; 0.5 = far (moves half as much); 1.3 = near. Visible while playing.
- **locked**: bool *(property)* — Locked: its objects cannot be selected in the 2D view in the editor.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **getWorldPosition**(): Vec2 *(method)* — World position (adding those of its parents).
- **lookAt**(target: Vec2): void *(method)* — Rotates the object to face a point.

### Water2D

2D water with waves, reflection and refraction of what is behind. Dynamic bodies float and slow down inside.

Inherits from **Node2D**. Area: 2D. Created with `Water2D(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec2 *(property)* — Position (pixels; Y grows downwards).
- **rotation**: number *(property)* — Rotation (degrees, clockwise).
- **scale**: Vec2 *(property)* — Scale (1 = normal size; negative flips).
- **zIndex**: number *(property)* — Drawing order (higher = in front).
- **visible**: bool *(property)* — Visible (also hides its children).
- **size**: Vec2 *(property)* — Width and depth (px). The surface is the top edge.
- **color**: Color *(property)* — Deep water colour.
- **surfaceColor**: Color *(property)* — Colour of the foam and surface shine.
- **transparency**: number *(property)* — How much of what is behind shows through.
- **reflectivity**: number *(property)* — Reflection of what is above.
- **waveHeight**: number *(property)* — Wave height (px).
- **waveLength**: number *(property)* — Distance between waves (px).
- **waveSpeed**: number *(property)* — Wave speed.
- **distortion**: number *(property)* — Refraction: how much what is seen through ripples (px).
- **foam**: number *(property)* — Foam on the surface.
- **buoyancy**: number *(property)* — Upward push (more than 1 = bodies float).
- **drag**: number *(property)* — Drag inside water.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **entered**: Event *(event)* — A 2D body enters the water (splashes, sound). Data: other: any.
- **exited**: Event *(event)* — A 2D body leaves the water. Data: other: any.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **getWorldPosition**(): Vec2 *(method)* — World position (adding those of its parents).
- **lookAt**(target: Vec2): void *(method)* — Rotates the object to face a point.

### Background2D

Repeating background with parallax (skies, mountains, clouds): moves slower than the camera.

Inherits from **Node2D**. Area: 2D. Created with `Background2D(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec2 *(property)* — Position (pixels; Y grows downwards).
- **rotation**: number *(property)* — Rotation (degrees, clockwise).
- **scale**: Vec2 *(property)* — Scale (1 = normal size; negative flips).
- **zIndex**: number *(property)* — Drawing order (higher = in front).
- **visible**: bool *(property)* — Visible (also hides its children).
- **image**: text *(property)* — Image.
- **color**: Color *(property)* — Tinte.
- **transparency**: number *(property)* — Transparencia.
- **scrollFactor**: Vec2 *(property)* — 0 = fixed on screen, 1 = moves with the world (0.2 far, 0.6 near).
- **repeatX**: bool *(property)* — Repetir en horizontal.
- **repeatY**: bool *(property)* — Repetir en vertical.
- **size**: Vec2 *(property)* — Size of each copy (0 = the image size).
- **autoScroll**: Vec2 *(property)* — Automatic scrolling (clouds): px/s.
- **lit**: bool *(property)* — Affected by 2D lights.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **getWorldPosition**(): Vec2 *(method)* — World position (adding those of its parents).
- **lookAt**(target: Vec2): void *(method)* — Rotates the object to face a point.

### Line2D

Line with several points (paths, ropes, rays, outlines). Edit the points by dragging them in the 2D view.

Inherits from **Node2D**. Area: 2D. Created with `Line2D(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec2 *(property)* — Position (pixels; Y grows downwards).
- **rotation**: number *(property)* — Rotation (degrees, clockwise).
- **scale**: Vec2 *(property)* — Scale (1 = normal size; negative flips).
- **zIndex**: number *(property)* — Drawing order (higher = in front).
- **visible**: bool *(property)* — Visible (also hides its children).
- **points**: text *(property)* — Points: "x,y; x,y; ..." (relative to the position).
- **width**: number *(property)* — Thickness.
- **widthEnd**: number *(property)* — Width at the end (-1 = the same).
- **color**: Color *(property)* — Colour at the start.
- **colorEnd**: Color *(property)* — Colour at the end.
- **transparency**: number *(property)* — Transparencia.
- **closed**: bool *(property)* — Close (join the last point to the first).
- **roundCaps**: bool *(property)* — Rounded ends and corners.
- **emission**: number *(property)* — Glow (bloom: lasers).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **getWorldPosition**(): Vec2 *(method)* — World position (adding those of its parents).
- **lookAt**(target: Vec2): void *(method)* — Rotates the object to face a point.

### Trail2D

Trail left by its parent while moving (swords, projectiles, cars, shooting stars).

Inherits from **Node2D**. Area: 2D. Created with `Trail2D(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec2 *(property)* — Position (pixels; Y grows downwards).
- **rotation**: number *(property)* — Rotation (degrees, clockwise).
- **scale**: Vec2 *(property)* — Scale (1 = normal size; negative flips).
- **zIndex**: number *(property)* — Drawing order (higher = in front).
- **visible**: bool *(property)* — Visible (also hides its children).
- **emitting**: bool *(property)* — Dejando estela.
- **lifetime**: number *(property)* — Trail duration (s).
- **width**: number *(property)* — Width at the start.
- **widthEnd**: number *(property)* — Width at the end.
- **color**: Color *(property)* — Colour at the start.
- **colorEnd**: Color *(property)* — Colour at the end.
- **alphaStart**: number *(property)* — Opacity at the start.
- **alphaEnd**: number *(property)* — Opacity at the end.
- **blendMode**: text *(property)* — Mezcla.
- **emission**: number *(property)* — Brillo.
- **minDistance**: number *(property)* — Minimum distance between points (px).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **getWorldPosition**(): Vec2 *(method)* — World position (adding those of its parents).
- **lookAt**(target: Vec2): void *(method)* — Rotates the object to face a point.

### Joint2D

Joins two sprites with physics: hinge, distance, spring, rope, weld or wheel. Put it inside one and choose the other in bodyB.

Inherits from **Instance**. Area: 2D. Created with `Joint2D(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **jointType**: text *(property)* — Joint type.
- **bodyA**: any *(property)* — First sprite (empty = the parent).
- **bodyB**: any *(property)* — Second sprite.
- **anchorA**: Vec2 *(property)* — Anchor point on the first one (px from its centre).
- **anchorB**: Vec2 *(property)* — Anchor point on the second one.
- **length**: number *(property)* — Longitud (Distance, Spring, Rope; 0 = la inicial).
- **stiffness**: number *(property)* — Spring stiffness (Hz).
- **damping**: number *(property)* — Spring damping.
- **collideConnected**: bool *(property)* — Both sprites collide with each other.
- **motor**: bool *(property)* — Motor (Revolute, Wheel).
- **motorSpeed**: number *(property)* — Motor speed (degrees/s).
- **maxMotorTorque**: number *(property)* — Maximum motor force.
- **limit**: bool *(property)* — Limit the rotation (Revolute).
- **lowerAngle**: number *(property)* — Minimum angle.
- **upperAngle**: number *(property)* — Maximum angle.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### PlatformerController2D

No-code platformer movement for the parent Sprite2D (Dynamic body): run, jump, double jump, coyote time and jump buffering. If the sprite has a SpriteAnimator, it switches animations by itself.

Inherits from **Instance**. Area: 2D. Created with `PlatformerController2D(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **enabled**: bool *(property)* — Activo.
- **speed**: number *(property)* — Maximum speed (px/s).
- **acceleration**: number *(property)* — Acceleration (px/s²).
- **deceleration**: number *(property)* — Braking when released (px/s²).
- **airControl**: number *(property)* — Air control (0..1).
- **jumpHeight**: number *(property)* — Jump height (px).
- **maxJumps**: number *(property)* — Consecutive jumps (2 = double jump).
- **coyoteTime**: number *(property)* — Time to jump after leaving a ledge (s).
- **jumpBuffer**: number *(property)* — Time a jump is remembered before touching the ground (s).
- **variableJump**: bool *(property)* — Releasing the key early cuts the jump.
- **fallMultiplier**: number *(property)* — Extra gravity when falling (weighty jumps).
- **leftKeys**: text *(property)* — Keys to go left.
- **rightKeys**: text *(property)* — Keys to go right.
- **jumpKeys**: text *(property)* — Keys to jump.
- **flipSprite**: bool *(property)* — Flip the sprite towards where it runs.
- **animIdle**: text *(property)* — Idle animation.
- **animRun**: text *(property)* — Running animation.
- **animJump**: text *(property)* — Rising animation.
- **animFall**: text *(property)* — Falling animation.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **jumped**: Event *(event)* — Jumped.
- **landed**: Event *(event)* — Touched the ground.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### TopDownController2D

Eight-direction top-down movement for the parent Sprite2D (RPG, adventures). With a Dynamic body it collides with walls.

Inherits from **Instance**. Area: 2D. Created with `TopDownController2D(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **enabled**: bool *(property)* — Activo.
- **speed**: number *(property)* — Maximum speed (px/s).
- **acceleration**: number *(property)* — Acceleration.
- **deceleration**: number *(property)* — Frenado.
- **upKeys**: text *(property)* — Arriba.
- **downKeys**: text *(property)* — Abajo.
- **leftKeys**: text *(property)* — Izquierda.
- **rightKeys**: text *(property)* — Derecha.
- **facing**: text *(property)* — How it faces where it goes.
- **animIdle**: text *(property)* — Idle animation.
- **animWalk**: text *(property)* — Walking animation.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

### Text2D

Text inside the 2D world (floating scores, signs, dialogues).

Inherits from **Node2D**. Area: 2D. Created with `Text2D(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **position**: Vec2 *(property)* — Position (pixels; Y grows downwards).
- **rotation**: number *(property)* — Rotation (degrees, clockwise).
- **scale**: Vec2 *(property)* — Scale (1 = normal size; negative flips).
- **zIndex**: number *(property)* — Drawing order (higher = in front).
- **visible**: bool *(property)* — Visible (also hides its children).
- **text**: text *(property)* — Texto.
- **textSize**: number *(property)* — Size (px).
- **color**: Color *(property)* — Color.
- **transparency**: number *(property)* — Transparencia.
- **alignment**: text *(property)* — Alignment.
- **bold**: bool *(property)* — Negrita.
- **font**: text *(property)* — Imported font (TTF/OTF); empty = the engine font.
- **outlineColor**: Color *(property)* — Outline colour.
- **outlineSize**: number *(property)* — Outline width (px).
- **shadowOpacity**: number *(property)* — Sombra.
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.
- **getWorldPosition**(): Vec2 *(method)* — World position (adding those of its parents).
- **lookAt**(target: Vec2): void *(method)* — Rotates the object to face a point.

### Note

Team note anchored to a point in the world: comments, tasks or ideas. Only visible in the editor.

Inherits from **Instance**. Area: Team. Created with `Note(parent)`.

- **name**: text *(property)* — Instance name.
- **className**: text *(property, read-only)* — Class name.
- **parent**: any *(property)* — Parent (assign another instance to move it; null to take it out of the game).
- **text**: text *(property)* — Note text.
- **author**: text *(property)* — Who wrote it.
- **position**: Vec3 *(property)* — World point where it is anchored.
- **color**: Color *(property)* — Marker colour.
- **resolved**: bool *(property)* — Resolved (shown dimmed).
- **createdAt**: number *(property)* — Creation date (seconds).
- **childAdded**: Event *(event)* — A direct child was added. Data: child: any.
- **childRemoved**: Event *(event)* — A direct child was removed. Data: child: any.
- **changed**: Event *(event)* — A property changed (receives its name). Data: property: text.
- **destroying**: Event *(event)* — La instancia va a destruirse.
- **find**(name: text): any *(method)* — Direct child with that name (or null).
- **findDescendant**(name: text): any *(method)* — First descendant with that name (or null).
- **findChildOfClass**(className: text): any *(method)* — First child of that class (or null).
- **findAncestorOfClass**(className: text): any *(method)* — First ancestor of that class (or null).
- **waitForChild**(name: text, timeout: number = 10): Task *(method)* — Task that finishes when the child exists (use it with await). Returns null when the time runs out.
- **children**(): list *(method)* — List of the direct children.
- **descendants**(): list *(method)* — List of every descendant.
- **isA**(className: text): bool *(method)* — Is it of that class or a derived one?
- **isDescendantOf**(other: any): bool *(method)* — Is it inside 'other'?
- **clone**(): any *(method)* — Copy (no parent).
- **destroy**(): void *(method)* — Destroys the instance and its children.
- **clearChildren**(): void *(method)* — Destroys every child.
- **getAttribute**(name: text): any *(method)* — Atributo personalizado (o null).
- **setAttribute**(name: text, value: any): void *(method)* — Stores a custom attribute.
- **getFullName**(): text *(method)* — Full path: Workspace.Model.Part.

## Enumerations (text values)

- **BlendMode2D**: `Normal`, `Additive`, `Multiply`, `Screen` — How it blends with what is behind: Normal, Additive (adds light: fire, magic), Multiply (darkens), Screen (lightens).
- **BodyType2D**: `None`, `Static`, `Dynamic`, `Kinematic` — 2D physics of a sprite.
- **CameraMode**: `Classic`, `LockFirstPerson` — Player camera mode.
- **CameraType**: `Custom`, `Scriptable`, `Fixed` — How the camera moves.
- **EmissionShape2D**: `Point`, `Circle`, `Rectangle`, `Ring`, `Line` — Zone where particles are born.
- **Facing2D**: `None`, `Flip`, `Rotate` — How the character faces the direction it moves.
- **JointType2D**: `Revolute`, `Distance`, `Spring`, `Rope`, `Weld`, `Wheel` — Joint type: hinge, fixed distance, spring, rope, weld or wheel (with suspension).
- **LightType2D**: `Point`, `Spot`, `Directional` — Point: lights a circle. Spot: a spotlight aimed by rotation (0 right, 90 down). Directional: a sun or moon lighting everything.
- **Material**: `Plastic`, `SmoothPlastic`, `Neon`, `Metal`, `Wood`, `Glass`, `Grass`, `Brick`, `Concrete`, `Ice`, `Sand`, `Fabric`, `Marble`, `Slate`, `ForceField` — Part material: changes the look (procedural texture, shine, reflections).
- **PartShape**: `Block`, `Ball`, `Cylinder`, `Wedge` — Shape of a part.
- **ParticleShape2D**: `Soft`, `Circle`, `Square`, `Spark`, `Star`, `Ring` — Shape of each particle (when it has no image).
- **RenderMode2D**: `Auto`, `Overlay`, `Exclusive`, `Off` — Auto: 2D only when there are no 3D parts; Overlay: on top of 3D; Exclusive: 2D only; Off: not drawn.
- **RigType**: `R15`, `R6` — Character skeleton: R15 (15 parts with elbows, knees, hands and feet) or R6 (6 parts).
- **ScaleType**: `Stretch`, `Fit` — How an image fits its box.
- **Shape2D**: `Box`, `Circle`, `RoundedBox`, `Capsule`, `Triangle`, `Polygon`, `Star`, `Ring` — 2D shape (drawing without an image and collision).
- **TextXAlignment**: `Left`, `Center`, `Right` — Horizontal text alignment.
- **TextYAlignment**: `Top`, `Center`, `Bottom` — Vertical text alignment.
- **TextureFilter2D**: `Auto`, `Pixel`, `Smooth` — Image filtering: Pixel (crisp pixel art), Smooth (smoothed) or Auto.
