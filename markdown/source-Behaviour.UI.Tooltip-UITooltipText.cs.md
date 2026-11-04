# UITooltipText — source reference

Behaviour.UI.Tooltip/UITooltipText.cs · 27 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 6 | public class UITooltipText : UITooltipContent |
| 9 | protected TMP_Text _text |
| 11 | public float? overrideHeight |
| 13 | protected float _spacing |
| 15 | public override float Height => overrideHeight ?? (_text.preferredHeight + _spacing) |
| 17 | public override float Spacing => _spacing |
| 19 | public TMP_Text Text => _text |
| 21 | public void SetText(string text, int size, float margin) |

## Documented by

| Wiki article |
| --- |
| [Tooltips, warnings, notifications, and tutorial cues](tooltips-warnings-and-tutorial.md) |

## Sources

- `Behaviour.UI.Tooltip/UITooltipText.cs:1`
