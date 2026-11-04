# UITooltipLine — source reference

Behaviour.UI.Tooltip/UITooltipLine.cs · 27 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 6 | public class UITooltipLine : UITooltipContent |
| 9 | protected Image _image |
| 11 | protected float _top |
| 13 | protected float _bottom |
| 15 | public override float Height => _top + _image.rectTransform.sizeDelta.y + _bottom |
| 17 | public override float Spacing => _bottom |
| 19 | public void SetLine(Color c, float lineHeight, float top, float bottom) |

## Documented by

| Wiki article |
| --- |
| [Tooltips, warnings, notifications, and tutorial cues](tooltips-warnings-and-tutorial.md) |

## Sources

- `Behaviour.UI.Tooltip/UITooltipLine.cs:1`
