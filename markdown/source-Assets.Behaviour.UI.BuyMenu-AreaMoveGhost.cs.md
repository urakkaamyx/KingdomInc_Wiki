# AreaMoveGhost — source reference

Assets.Behaviour.UI.BuyMenu/AreaMoveGhost.cs · 114 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 9 | public class AreaMoveGhost : MonoBehaviour, IDragDropTarget |
| 15 | public Vector2Int GetGrabOffset(Vector2Int mousePosition) |
| 29 | public void OnDragDropCancel() |
| 35 | public void OnDragDropEnd() |
| 70 | public void ToggleActive(bool toggleTo) |
| 97 | public void OnDragDropMove(Vector2Int mousePosition, Vector2Int grabOffset) |

## Documented by

| Wiki article |
| --- |
| [Building, copying, and area movement](building-and-blueprints.md) |

## Sources

- `Assets.Behaviour.UI.BuyMenu/AreaMoveGhost.cs:1`
