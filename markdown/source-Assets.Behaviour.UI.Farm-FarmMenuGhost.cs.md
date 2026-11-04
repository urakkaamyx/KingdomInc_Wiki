# FarmMenuGhost — source reference

Assets.Behaviour.UI.Farm/FarmMenuGhost.cs · 58 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public class FarmMenuGhost : MonoBehaviour, IDragDropTarget |
| 13 | public FarmItemType _item |
| 15 | public static FarmMenuGhost Instance { get; private set; } |
| 22 | public Vector2Int GetGrabOffset(Vector2Int mousePosition) |
| 27 | public void OnDragDropCancel() |
| 33 | public void OnDragDropEnd() |
| 48 | public void OnDragDropMove(Vector2Int mousePosition, Vector2Int grabOffset) |
| 53 | public void SetItem(FarmItemType item) |

## Documented by

| Wiki article |
| --- |
| [Farm plots and planting controls](farm-panel-controls.md) |

## Sources

- `Assets.Behaviour.UI.Farm/FarmMenuGhost.cs:1`
