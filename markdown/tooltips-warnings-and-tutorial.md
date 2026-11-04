# Tooltips, warnings, notifications, and tutorial cues

How contextual details, text input, progress bars, and alert messages behave.

## Tooltips

TooltipSource obtains title, body and custom content from its configured object or parent interfaces. Hover shows a tooltip only when the component is enabled and drag/drop is not busy. Exiting hides it or forwards to the newly hovered tooltip source. Tooltips follow the mouse, flip horizontally/vertically near screen edges and include text, item rows, prices, values, separators and progress bars.

## Live content and layout

TinyProgressBar refreshes its callbacks every 0.5 seconds. ItemCountCell provides an item tooltip only for actual item entries; arbitrary icon/text cells disable it. TextContainer sizes itself to preferred text plus padding. FontFilteringSwitch selects point-font rendering when effective size rounds to 16, otherwise the filtered font; changes propagate separately to world and screen-space text.

## Warnings and status

A disabled craft button reports Output Full when progress≥1, otherwise No Ingredients. Status notifications last five simulated seconds unless persistent, slide/fade in and fade out, and can invoke a click action. Persistent notifications expose a close control. General alerts support Okay or Yes/No with supplied callbacks and resize around localized message text.

## Input helpers

Focused text fields repeatedly delay player input. HoverAction and RightClickAction invoke configured UI events, HoverHighlight toggles artwork, and DepressButton shifts button children down two pixels while pressed. UIBlocksZoom prevents world zoom while hovering registered menus/popups. These are presentation/input wrappers rather than extra game systems.

## Tutorial sequence

Initial blackout prevents normal dragging and recipe selection. Dismissing it re-enables controls/UI and fades the overlay. Tutorial arrows direct construction, Mine upgrade slots, output-to-Forge connection, research and the Shop unlock. Opening the relevant crew/resource/build panel clears its cue. FinishTutorial disables the tutorial component; arrow blinking/motion is visual guidance.

## Sources

- `Behaviour.UI/UITooltip.cs:77`
- `Behaviour.UI.Tooltip/ITooltipCustomSource.cs:3`
- `Behaviour.UI.Tooltip/ITooltipTextSource.cs:3`
- `Behaviour.UI.Tooltip/ITooltipTitleSource.cs:3`
- `Behaviour.UI.Tooltip/TooltipSource.cs:43`
- `Behaviour.UI.Tooltip/UITooltipContent.cs:5`
- `Behaviour.UI.Tooltip/UITooltipLine.cs:19`
- `Behaviour.UI.Tooltip/UITooltipParent.cs:12`
- `Behaviour.UI.Tooltip/UITooltipSpacer.cs:3`
- `Behaviour.UI.Tooltip/UITooltipText.cs:21`
- `Assets.Behaviour.UI.Shared/ItemCountCell.cs:23`
- `Assets.Behaviour.UI.Shared/TinyProgressBar.cs:24`
- `Assets.Behaviour.UI.Shared/TextContainer.cs:16`
- `Assets.Behaviour.UI.Shared/FontFilteringSwitch.cs:24`
- `Assets.Behaviour.UI.Shared/HoverAction.cs:15`
- `Assets.Behaviour.UI.Shared/HoverHighlight.cs:14`
- `Assets.Behaviour.UI.Shared/RightClickAction.cs:12`
- `Assets.Behaviour.UI.Shared/UIBlocksZoom.cs:13`
- `Assets.Behaviour.UI.Shared/UIPopupMenu.cs:13`
- `Assets.Behaviour.UI/DepressButton.cs:17`
- `Assets.Behaviour.UI/UIHelper.cs:12`
- `Assets.Behaviour.UI/UIFloatingText.cs:23`
- `Assets.Behaviour.UI/UIStatusMessage.cs:31`
- `Assets.Behaviour.UI/UIAlertWindow.cs:38`
- `Assets.Behaviour.UI/TutorialUI.cs:53`
- `Assets.Behaviour.UI.Shared/UITutorialArrow.cs:16`
