# FlowPipe — source reference

Assets.Source.Flow/FlowPipe.cs · 130 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 9 | public class FlowPipe : IJsonSource |
| 11 | public readonly List<Vector2Int> Nodes = new List<Vector2Int>() |
| 13 | public WorldFlowPipe World |
| 15 | public bool ItemRejected |
| 17 | public FlowOutput ConnectedOutput { get; private set; } |
| 19 | public FlowInput ConnectedInput { get; private set; } |
| 21 | public void Update(float delta) |
| 48 | public void Connect(FlowOutput output, FlowInput input, bool ghost = false) |
| 59 | public JsonValue ToJson() |
| 94 | public static FlowPipe FromJson(JsonValue data, FlowDiagram parent, Dictionary<string, FlowElement> elements) |

## Documented by

| Wiki article |
| --- |
| [Production simulation and bottlenecks](production-simulation.md) |

## Sources

- `Assets.Source.Flow/FlowPipe.cs:1`
