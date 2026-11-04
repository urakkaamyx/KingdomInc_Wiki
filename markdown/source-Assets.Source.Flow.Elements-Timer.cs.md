# Timer — source reference

Assets.Source.Flow.Elements/Timer.cs · 74 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class Timer : FlowElement |
| 9 | public float MaxTime = 2f |
| 11 | public float TimeLeft = 2f |
| 13 | public override string Label => "@timer_node" |
| 15 | public override ElementCategory Category => ElementCategory.Utility |
| 17 | public override string IconName => "Icons_75" |
| 19 | public override bool HasCraftButton => false |
| 21 | public Timer() |
| 39 | public override void Update(float delta) |
| 56 | protected override void CopySettingsTo(FlowElement copy) |
| 63 | protected override void DataToJson(JsonObject data) |
| 69 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Timer](building-Timer.md) |
| [Track switches, timers, and release buttons](production-gates.md) |

## Sources

- `Assets.Source.Flow.Elements/Timer.cs:1`
