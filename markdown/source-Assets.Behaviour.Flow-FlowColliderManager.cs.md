# FlowColliderManager — source reference

Assets.Behaviour.Flow/FlowColliderManager.cs · 55 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 6 | public class FlowColliderManager : MonoBehaviour |
| 10 | public static FlowColliderManager Instance { get; private set; } |
| 18 | public bool Overlaps(WorldFlowElement element) |
| 32 | public bool Overlaps(Vector2Int position, Vector2Int size) |
| 46 | public IEnumerable<Collider2D> GetOverlap(Vector2Int position, Vector2Int size) |
| 51 | public IEnumerable<Collider2D> GetOverlapCircle(Vector2Int position, int radius) |

## Documented by

| Wiki article |
| --- |
| [Map navigation and dragging](map-navigation-and-dragging.md) |

## Sources

- `Assets.Behaviour.Flow/FlowColliderManager.cs:1`
