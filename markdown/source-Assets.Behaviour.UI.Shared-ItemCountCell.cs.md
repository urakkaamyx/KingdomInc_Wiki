# ItemCountCell — source reference

Assets.Behaviour.UI.Shared/ItemCountCell.cs · 56 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public class ItemCountCell : UITooltipContent, ITooltipTitleSource, ITooltipCustomSource |
| 21 | public override float Height => _icon.rectTransform.sizeDelta.y |
| 23 | public void SetItem(InventoryItem item, int count, bool showName, string nameOverride = null) |
| 30 | public void SetCustomItem(Sprite icon, string text, Color c, bool tooltip = false) |
| 47 | public string GetTooltipTitle() |
| 52 | public void AddTooltipCustomContent(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Tooltips, warnings, notifications, and tutorial cues](tooltips-warnings-and-tutorial.md) |

## Sources

- `Assets.Behaviour.UI.Shared/ItemCountCell.cs:1`
