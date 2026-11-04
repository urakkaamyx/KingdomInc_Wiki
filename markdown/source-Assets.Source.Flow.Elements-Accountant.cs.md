# Accountant — source reference

Assets.Source.Flow.Elements/Accountant.cs · 113 lines · 3 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 10 | public class Accountant : FlowElement |
| 12 | public const int BaseCapacity = 10 |
| 14 | public Currency? CurrType |
| 16 | public AppraiserType AppraiseType |
| 18 | public long CurrAmount |
| 20 | public override string Label => "@accountant" |
| 22 | public override ElementCategory Category => ElementCategory.Utility |
| 24 | public override bool HasCraftButton => false |
| 26 | public override string IconName => "Icons_149" |
| 28 | public override Sprite Icon => CurrType?.GetIcon() ?? base.Icon |
| 30 | public Accountant() |
| 49 | public override bool HandleReopenBuyMenu() |
| 55 | public override void Update(float delta) |
| 63 | public bool AppraiseItem() |
| 86 | protected override void CopySettingsTo(FlowElement copy) |
| 94 | protected override void DataToJson(JsonObject data) |
| 104 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Accountant](building-Accountant.md) |
| [Filters, Appraisers, Inspectors, and Accountants](production-filters.md) |
| [Filters, Appraisers, and Accountants](routing-filter-appraiser-accountant.md) |

## Sources

- `Assets.Source.Flow.Elements/Accountant.cs:1`
