# Incinerator — source reference

Assets.Source.Flow.Elements/Incinerator.cs · 54 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public class Incinerator : FlowElement |
| 10 | public InventoryItem LastItem |
| 12 | public override string Label => "@incinerator" |
| 14 | public override ElementCategory Category => ElementCategory.Utility |
| 16 | public override string IconName => "Icons_57" |
| 18 | public override bool HasCraftButton => false |
| 20 | public Incinerator() |
| 33 | public override void Update(float delta) |
| 42 | protected override void DataToJson(JsonObject data) |
| 47 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Incinerator](building-Incinerator.md) |
| [Incineration and nightmare distillation](production-disposal-nightmare.md) |

## Sources

- `Assets.Source.Flow.Elements/Incinerator.cs:1`
