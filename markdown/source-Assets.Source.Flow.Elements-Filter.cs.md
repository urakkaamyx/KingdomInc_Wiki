# Filter — source reference

Assets.Source.Flow.Elements/Filter.cs · 93 lines · 3 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 9 | public class Filter : FlowElement |
| 11 | public const int BaseCapacity = 10 |
| 13 | public override string Label => "@filter" |
| 15 | public override ElementCategory Category => ElementCategory.Utility |
| 17 | public override string IconName => "Icons_150" |
| 19 | public override bool HasCraftButton => false |
| 21 | public ItemType FilterType { get; private set; } |
| 23 | public override Sprite Icon => FilterType?.GetIcon() ?? base.Icon |
| 25 | public Filter() |
| 49 | public override bool HandleReopenBuyMenu() |
| 55 | public void SetFilterType(ItemType type) |
| 61 | public override void Update(float delta) |
| 73 | protected override void CopySettingsTo(FlowElement copy) |
| 78 | protected override void DataToJson(JsonObject data) |
| 86 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Filter](building-Filter.md) |
| [Filters, Appraisers, Inspectors, and Accountants](production-filters.md) |
| [Filters, Appraisers, and Accountants](routing-filter-appraiser-accountant.md) |

## Sources

- `Assets.Source.Flow.Elements/Filter.cs:1`
