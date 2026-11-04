# SingleButton — source reference

Assets.Source.Flow.Elements/SingleButton.cs · 59 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class SingleButton : FlowElement |
| 9 | public int ClickCount |
| 11 | public override string Label => "@single_button" |
| 13 | public override ElementCategory Category => ElementCategory.Utility |
| 15 | public override string IconName => "Icons_74" |
| 17 | public override bool HasCraftButton => false |
| 19 | public SingleButton() |
| 37 | public override void Update(float delta) |
| 50 | protected override void DataToJson(JsonObject data) |
| 55 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Button](building-SingleButton.md) |
| [Track switches, timers, and release buttons](production-gates.md) |

## Sources

- `Assets.Source.Flow.Elements/SingleButton.cs:1`
