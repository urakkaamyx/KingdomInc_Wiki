# FlowPrefabSet — source reference

Assets.Behaviour.Flow/FlowPrefabSet.cs · 30 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class FlowPrefabSet : MonoBehaviour |
| 9 | public static IReadOnlyList<FlowPrefabSet> Ordered => FlowPrefabManager.Instance.Ordered |
| 12 | public WorldFlowElement Prefab { get; private set; } |
| 15 | public Sprite DetailSprite { get; private set; } |
| 17 | public Sprite PurchaseBackground => Prefab.BackgroundSprite |
| 19 | public string Identifier { get; set; } |
| 21 | public static FlowPrefabSet Get(string id) |
| 26 | public static FlowPrefabSet Get(FlowElement el) |

## Documented by

| Wiki article |
| --- |
| [Map navigation and dragging](map-navigation-and-dragging.md) |

## Sources

- `Assets.Behaviour.Flow/FlowPrefabSet.cs:1`
