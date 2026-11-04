# FlowCollider — source reference

Assets.Behaviour.Flow/FlowCollider.cs · 57 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 5 | public class FlowCollider : MonoBehaviour |
| 13 | public WorldFlowElement Element { get; private set; } |
| 15 | public WorldFlowDeco Deco { get; private set; } |
| 17 | public Vector2 Center => (Vector2)transform.position + _collider.offset |
| 19 | public void SetElement(WorldFlowElement element) |
| 25 | public void SetDeco(WorldFlowDeco deco) |
| 31 | public void UpdateSize() |
| 53 | public void SetDragMode(bool dragging) |

## Documented by

| Wiki article |
| --- |
| [Map navigation and dragging](map-navigation-and-dragging.md) |

## Sources

- `Assets.Behaviour.Flow/FlowCollider.cs:1`
