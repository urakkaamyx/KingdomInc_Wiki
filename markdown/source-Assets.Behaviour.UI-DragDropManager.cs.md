# DragDropManager — source reference

Assets.Behaviour.UI/DragDropManager.cs · 107 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 6 | public class DragDropManager : MonoBehaviour |
| 14 | public static DragDropManager Instance { get; private set; } |
| 16 | public bool Busy |
| 28 | public IDragDropTarget Target => _currentTarget |
| 51 | public void UpdateDragPosition() |
| 69 | public bool SetDragDropTarget(IDragDropTarget target, bool holdMode) |
| 90 | public void ClearDragDrop() |
| 96 | public bool CancelDragDrop() |

## Documented by

| Wiki article |
| --- |
| [Map navigation and dragging](map-navigation-and-dragging.md) |

## Sources

- `Assets.Behaviour.UI/DragDropManager.cs:1`
