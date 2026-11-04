# Inspector — source reference

Assets.Source.Flow.Elements/Inspector.cs · 68 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public class Inspector : FlowElement |
| 10 | public InventoryItem LastItem |
| 12 | public InventoryItem LiveItem |
| 14 | public override string Label => "@inspector" |
| 16 | public override ElementCategory Category => ElementCategory.Utility |
| 18 | public override string IconName => "Icons_37" |
| 20 | public override bool HasCraftButton => false |
| 22 | public override Sprite Icon => LastItem?.Icon ?? base.Icon |
| 24 | public Inspector() |
| 42 | public override void Update(float delta) |
| 56 | protected override void DataToJson(JsonObject data) |
| 61 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Inspector](building-Inspector.md) |
| [Filters, Appraisers, Inspectors, and Accountants](production-filters.md) |

## Sources

- `Assets.Source.Flow.Elements/Inspector.cs:1`
