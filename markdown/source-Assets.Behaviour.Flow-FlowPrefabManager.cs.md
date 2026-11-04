# FlowPrefabManager — source reference

Assets.Behaviour.Flow/FlowPrefabManager.cs · 42 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class FlowPrefabManager : MonoBehaviour |
| 16 | public static FlowPrefabManager Instance { get; private set; } |
| 18 | public IReadOnlyList<FlowPrefabSet> Ordered => _orderedPrefabs |
| 32 | public FlowPrefabSet Get(string id) |
| 38 | public Sprite GetCategoryBorder(ElementCategory cat) |

## Documented by

| Wiki article |
| --- |
| [Map navigation and dragging](map-navigation-and-dragging.md) |

## Sources

- `Assets.Behaviour.Flow/FlowPrefabManager.cs:1`
