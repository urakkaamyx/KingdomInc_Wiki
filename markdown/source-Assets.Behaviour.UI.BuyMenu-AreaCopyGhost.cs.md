# AreaCopyGhost — source reference

Assets.Behaviour.UI.BuyMenu/AreaCopyGhost.cs · 161 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 10 | public class AreaCopyGhost : MonoBehaviour, IDragDropTarget |
| 24 | public Vector2Int GetGrabOffset(Vector2Int mousePosition) |
| 49 | public void OnDragDropCancel() |
| 55 | public void OnDragDropEnd() |
| 80 | public void ToggleActive(bool toggleTo) |
| 144 | public void OnDragDropMove(Vector2Int mousePosition, Vector2Int grabOffset) |

## Documented by

| Wiki article |
| --- |
| [Building, copying, and area movement](building-and-blueprints.md) |

## Sources

- `Assets.Behaviour.UI.BuyMenu/AreaCopyGhost.cs:1`
