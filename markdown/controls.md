# Controls and rebinding

Factory keyboard and mouse bindings decoded from the actual action-map asset.

## Factory bindings

PlayerPrefs overrides can replace these defaults. Generated InputActions stores its JSON on one physical source line, cited for this complete table.

| Action | Default path |
| --- | --- |
| Interact | <Mouse>/leftButton |
| Cancel | <Mouse>/rightButton |
| TraverseHold | <Mouse>/middleButton |
| TraverseHold | <Mouse>/rightButton |
| TraverseHold | <Mouse>/leftButton |
| TogglePurchaseMenu | <Keyboard>/b |
| ToggleItemMenu | <Keyboard>/i |
| ToggleDeconstruct | <Keyboard>/x |
| ToggleTech | <Keyboard>/t |
| Escape | <Keyboard>/escape |
| ToggleMap | <Keyboard>/m |
| ToggleResources | <Keyboard>/r |
| Picker | <Keyboard>/q |
| ToggleDeco | <Keyboard>/e |
| Clone | <Keyboard>/c |
| AreaMove | <Keyboard>/v |
| ToggleSearch | <Keyboard>/f |
| Hotkey1 | <Keyboard>/1 |
| Hotkey2 | <Keyboard>/2 |
| Hotkey3 | <Keyboard>/3 |
| Hotkey4 | <Keyboard>/4 |
| Hotkey5 | <Keyboard>/5 |
| Hotkey6 | <Keyboard>/6 |
| Hotkey7 | <Keyboard>/7 |
| Hotkey8 | <Keyboard>/8 |
| Hotkey9 | <Keyboard>/9 |
| Hotkey0 | <Keyboard>/0 |

## Combinations

Alt+V is the ToggleUI composite; V alone is AreaMove. Shift plus mouse wheel cycles workflows while the world is visible and more than one workflow exists. Ordinary wheel changes camera zoom when UI does not block it. Ctrl bypasses blueprint grid snapping. Shift keeps a blueprint ready after placement.

Mouse traversal binds middle, right, and left buttons. Left-button traversal rejects most UI interactions and busy drag/drop. Right click also cancels, so behavior depends on context.

## Rebinding

Rebindable actions are Purchase, Tech, Deco, Resources, Picker, Deconstruct, Clone, AreaMove, Search, Map, ItemMenu, and hotkeys 1–0. Escape, traversal, ordinary mouse interaction, and Alt+V are not in that exposed rebind list. Apply writes InputBindingOverrides JSON in PlayerPrefs; Reset removes overrides; closing without Apply restores the captured original settings.

## Technology gates

Clone requires clone_tool, area move requires unlock_area_move, and ItemMenu requires item_list. Numeric keys call GameUI.DoHotkey and operate contextually in the current interface; a shortcut does not bypass research gates.

## Sources

- `Assets.Behaviour.Input/InputActions.cs:583`
- `Assets.Behaviour.Input/PlayerInput.cs:166`
- `Assets.Behaviour.Input/PlayerInput.cs:271`
- `Assets.Behaviour.Input/PlayerInput.cs:245`
- `Assets.Behaviour.UI.MainMenu/KeyBindingsUI.cs:68`
- `Assets.Behaviour.UI.MainMenu/KeyBindingsUI.cs:41`
- `Assets.Behaviour.UI/GameUI.cs:594`
- `Assets.Behaviour.UI/GameUI.cs:1006`
