# SaveGameUI — source reference

SaveGameUI.cs · 109 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public class SaveGameUI : MonoBehaviour |
| 25 | protected List<SaveGameRow> _rows = new List<SaveGameRow>() |
| 62 | public virtual void ShowSaveGame(SaveGameFile file) |
| 71 | public virtual void DoExecuteAction() |
| 89 | public void CancelSaveGame() |
| 97 | public void EndEdit() |
| 106 | public void OnInputFieldSelected() |

## Documented by

| Wiki article |
| --- |
| [Menus, save selection, music, and visual feedback](menus-saves-music-and-animation.md) |

## Sources

- `SaveGameUI.cs:1`
