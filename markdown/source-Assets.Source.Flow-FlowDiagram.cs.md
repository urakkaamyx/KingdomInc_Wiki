# FlowDiagram — source reference

Assets.Source.Flow/FlowDiagram.cs · 103 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class FlowDiagram : IJsonSource |
| 9 | public string Label |
| 11 | public string IconName |
| 13 | public Vector2Int CameraPos |
| 15 | public readonly List<FlowElement> Elements = new List<FlowElement>() |
| 17 | public readonly List<FlowPipe> Pipes = new List<FlowPipe>() |
| 19 | public readonly List<FlowDeco> Decorations = new List<FlowDeco>() |
| 21 | public void Start() |
| 29 | public void Update(float delta) |
| 41 | public void DisconnectPipe(FlowPipe pipe) |
| 54 | public JsonValue ToJson() |
| 79 | public static FlowDiagram FromJson(JsonValue json) |

## Documented by

| Wiki article |
| --- |
| [Production simulation and bottlenecks](production-simulation.md) |

## Sources

- `Assets.Source.Flow/FlowDiagram.cs:1`
