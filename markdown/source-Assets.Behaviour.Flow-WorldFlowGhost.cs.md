# WorldFlowGhost — source reference

Assets.Behaviour.Flow/WorldFlowGhost.cs · 349 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 14 | public class WorldFlowGhost : MonoBehaviour, IDragDropTarget |
| 55 | public void SetElement(FlowElement el, bool reopenBuyMenu) |
| 65 | public void SetDeco(FlowDeco deco, bool clone, bool reopenDecoMenu) |
| 92 | public void SetChildOffset(Vector2Int offset) |
| 98 | public Vector2Int GetGrabOffset(Vector2Int mousePosition) |
| 103 | public void OnDragDropMove(Vector2Int mousePosition, Vector2Int grabOffset) |
| 113 | public void OnDragDropEnd() |
| 303 | public void OnDragDropCancel() |
| 308 | public CurrencyCollection GetCopyCost() |
| 327 | public static CurrencyCollection GetCopyCost(IEnumerable<WorldFlowElement> elements, IEnumerable<WorldFlowDeco> decos) |

## Documented by

| Wiki article |
| --- |
| [Building, copying, and area movement](building-and-blueprints.md) |

## Sources

- `Assets.Behaviour.Flow/WorldFlowGhost.cs:1`
