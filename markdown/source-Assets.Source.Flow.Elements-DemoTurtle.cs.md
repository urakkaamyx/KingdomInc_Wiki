# DemoTurtle — source reference

Assets.Source.Flow.Elements/DemoTurtle.cs · 41 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class DemoTurtle : FlowElement |
| 9 | public override string Label => "@turtle_statue" |
| 11 | public override ElementCategory Category => ElementCategory.Consumption |
| 13 | public override string IconName => "Icons_131" |
| 15 | public override bool HasCraftButton => false |
| 17 | public DemoTurtle() |
| 30 | public override void Update(float delta) |
| 34 | protected override void DataToJson(JsonObject data) |
| 38 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Turtle Statue](building-DemoTurtle.md) |

## Sources

- `Assets.Source.Flow.Elements/DemoTurtle.cs:1`
