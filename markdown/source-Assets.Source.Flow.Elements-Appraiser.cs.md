# Appraiser — source reference

Assets.Source.Flow.Elements/Appraiser.cs · 116 lines · 3 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 9 | public class Appraiser : FlowElement |
| 11 | public const int BaseCapacity = 10 |
| 13 | public AppraiserStat? StatAppraised |
| 15 | public AppraiserType AppraiseType = AppraiserType.GreaterThanOrEqual |
| 17 | public int StatAmount |
| 19 | public override string Label => "@appraiser" |
| 21 | public override ElementCategory Category => ElementCategory.Utility |
| 23 | public override bool HasCraftButton => false |
| 25 | public override string IconName => StatAppraised?.GetIconName() ?? "Icons_148" |
| 27 | public Appraiser() |
| 51 | public override bool HandleReopenBuyMenu() |
| 57 | public override void Update(float delta) |
| 70 | public bool AppraiseItem(InventoryItem item) |
| 89 | protected override void CopySettingsTo(FlowElement copy) |
| 97 | protected override void DataToJson(JsonObject data) |
| 107 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Appraiser](building-Appraiser.md) |
| [Filters, Appraisers, Inspectors, and Accountants](production-filters.md) |
| [Filters, Appraisers, and Accountants](routing-filter-appraiser-accountant.md) |

## Sources

- `Assets.Source.Flow.Elements/Appraiser.cs:1`
