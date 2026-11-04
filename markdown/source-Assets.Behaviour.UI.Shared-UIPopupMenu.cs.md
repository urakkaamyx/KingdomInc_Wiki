# UIPopupMenu — source reference

Assets.Behaviour.UI.Shared/UIPopupMenu.cs · 22 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 5 | public class UIPopupMenu : UIBlocksZoom |
| 7 | public Action OnPopupClosed |
| 9 | public virtual bool CanCancel => true |
| 11 | public virtual bool CanEscape => true |
| 13 | public virtual void PopupClosed() |
| 18 | public void ClosePopup() |

## Documented by

| Wiki article |
| --- |
| [Tooltips, warnings, notifications, and tutorial cues](tooltips-warnings-and-tutorial.md) |

## Sources

- `Assets.Behaviour.UI.Shared/UIPopupMenu.cs:1`
