# Workflow tabs, names, icons, and ordering

Switch diagrams, buy additional diagrams, rename them, and swap their positions.

## Switch and reorder

Left click another workflow tab to switch. Ctrl-left-click another tab swaps its position with the currently active workflow, updating indices and selection. Right click opens its name/icon options. First ten workflows show the corresponding configurable numeric hotkey when its label fits.

## Scroll and overflow

Mouse wheel over the workflow bar cycles the current diagram with wraparound. Left/right overflow buttons move the visible tab window. Available width depends on screen width and UI scale and caps at ten buttons, including the Add button. Hover slides the tab bar into view; an open options popup postpones that motion.

## Names and icons

Type a label in options; PopupClosed writes it to the workflow. Icon selection applies immediately and refreshes the bar. Search matches icon names case-insensitively, using icons from items, nondeveloper technologies and currencies. Enter saves/closes; double click an icon selects it and saves.

## Buy a workflow

The Add button shows GetExtraWorkflowCost in its tooltip. Buying spends it, appends a new FlowDiagram, refreshes tabs, and immediately switches to the new one. All workflows still simulate through GamePlayer.Update when not selected.

## Sources

- `Assets.Behaviour.UI.SwapFlow/FlowOptionsIcon.cs:18`
- `Assets.Behaviour.UI.SwapFlow/FlowOptionsPopup.cs:35`
- `Assets.Behaviour.UI.SwapFlow/SwapFlowAddButton.cs:12`
- `Assets.Behaviour.UI.SwapFlow/SwapFlowItem.cs:33`
- `Assets.Behaviour.UI.SwapFlow/SwapFlowMenu.cs:46`
- `SpriteLibrary.cs:21`
