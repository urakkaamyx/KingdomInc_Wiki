# Saves, autosaves, pause, and offline behavior

Storage, recovery behavior, persisted state, timing, and offline progression evidence.

## Storage and format

Files are stored in Application.persistentDataPath + /Saves. New saves use .save and gzip-compressed UTF-8 JSON. Recall tries gzip then plain JSON after IOException. The browser accepts .json and .save. Each save stores Application.version, Player, and a hash-derived Secret; the inspected LoadState does not validate Secret.

Store uses FileMode.Create, so saving over a name replaces it. Saving rejects a player with zero workflows. Errors show a persistent status and log the exception. File modification time is filesystem metadata, not a simulated elapsed-time field.

## Autosaves

Default frequency is 300 simulated seconds (5 minutes). Three rotating files are autosave-0 through autosave-2. Missing slots are filled first; otherwise the oldest file by last-write time is replaced. Option 0 disables timed autosaves.

Extra checkpoints are autosave-exit on quitting, autosave-rtt on return to menu, and autosave-prestige before prestige. Continue selects the latest file across all recognized saves.

## Persisted player state

Player JSON includes workflows and contents, balances and earned totals, exchange data, research, resources and upgrade counts, camera/zoom/current workflow, upgrade counts and availability, requisition types, wars, unlocked dungeons, game time, Forest/Farm settings, quest/dungeon metadata, Armory, Portal, Register, ascension/nightmare state, and perks. Options and bindings are in separate PlayerPrefs.

## Loading older saves

LoadState restores the prior in-memory player if loading throws. Before version 0.9.6, patches grant training_grounds_spec when Training Grounds is unlocked and set NightmareProgress=1 and NightmareActive=true. This does not establish compatibility with arbitrary future/edited formats.

## Pause and offline behavior

WorldFlowManager advances the player with Time.deltaTime. Autosave timers also use Time.deltaTime. In-game menu sets timescale=0 and disables controls; closing restores timescale=1. Steam overlay pauses similarly and restores only when the in-game menu is closed.

No wall-clock catch-up calculation was found in the inspected load path. Filesystem time orders saves; it is not fed into workflow/resource simulation. This build therefore has no verified offline progression in the examined code. Loading reconstructs saved state and resumes delta-time simulation.

## Sources

- `Assets.Source.Util/SaveGame.cs:31`
- `Assets.Source.Util/SaveGame.cs:42`
- `Assets.Source.Util/SaveGame.cs:57`
- `Assets.Source.Util/SaveGame.cs:120`
- `Assets.Source.Util/SaveGame.cs:137`
- `Assets.Source.Util/SaveGameFile.cs:28`
- `Assets.Source.Player/GamePlayer.cs:701`
- `Assets.Behaviour.UI/GameUI.cs:273`
- `Assets.Behaviour.UI.MainMenu/InGameMenuUI.cs:31`
- `Assets.Behaviour.Flow/WorldFlowManager.cs:129`
- `Assets.Behaviour.Util/SteamStatsManager.cs:43`
- `Assets.Behaviour/GameManager.cs:31`
