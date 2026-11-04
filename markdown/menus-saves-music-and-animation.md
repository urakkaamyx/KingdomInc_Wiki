# Menus, save selection, music, and visual feedback

Menu rows, rebinding restrictions, audio timing, and cosmetic animation behavior.

## Save and Load rows

Rows are sorted newest-first and display filename plus dd/MM/yyyy HH:mm:ss filesystem time. One click selects/highlights; double click executes the current save/load action. Save selection copies the name into the editable field; blank names do nothing; Enter saves and resumes. Load executes only after a selected file exists and routes to main-menu or in-game loading.

## Key rebinding restrictions

The listening row accepts keyboard controls, excluding mouse, AnyKey and standalone Shift/Ctrl/Alt variants. Escape cancels listening. Only one row listens at a time; a newly selected row cancels other listeners. Apply/Cancel behavior is handled by KeyBindingsUI.

## Music

Music volume defaults to 0.35 and sound volume to 1 in PlayerPrefs. MusicLibrary defines tracks per machine/scene. The manager shuffles its normal playlist, changes after about 300 simulated seconds, and supports fades and quiet gaps. Hovering machines queues their theme only after elapsed-time thresholds; it does not immediately restart every hovered song. Victory and prestige use dedicated tracks.

## Sound and cosmetic animation

UISounds caches audio sources, varies pitch slightly and suppresses the same clip for 0.1 unscaled seconds to limit repeated clicks. Releasing the sound slider previews a page sound. Floating messages rise and fade; falling menu item icons and the bobbing logo are cosmetic. Prestige background wobble and victory music contain no additional progression rules.

## Boot and new-game transition

Bootstrap initializes translation before scene load, keeps Bootstrap roots alive, applies settings and initializes Steam stats if Steam is available. New Game fades a transition, creates the player, sets zoom from screen height, loads Game, displays tutorial content, hides ordinary UI and disables controls until tutorial dismissal.

## Sources

- `SaveGameRow.cs:22`
- `SaveGameUI.cs:27`
- `Assets.Behaviour.UI.MainMenu/LoadGameUI.cs:9`
- `Assets.Behaviour.UI.MainMenu/KeyBindingRow.cs:26`
- `Assets.Behaviour.UI.MainMenu/MMFallingItem.cs:23`
- `Assets.Behaviour.UI.MainMenu/MMLogo.cs:15`
- `Assets.Behaviour.UI.MainMenu/OptionsSoundSlider.cs:9`
- `Assets.Behaviour.UI.Prestige/BackgroundWobble.cs:12`
- `Assets.Behaviour.UI.Prestige/VictoryPopup.cs:8`
- `Assets.Behaviour.Util/Bootstrap.cs:26`
- `Assets.Behaviour.Util/KeyBindingTooltip.cs:18`
- `Assets.Behaviour.Util/MusicLibrary.cs:3`
- `Assets.Behaviour.Util/MusicManager.cs:48`
- `Assets.Behaviour.Util/QueuedMusic.cs:3`
- `Assets.Behaviour.Util/Translatable.cs:13`
- `Assets.Behaviour.UI/UISounds.cs:60`
