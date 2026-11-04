# FlowUpgrade — source reference

Assets.Source.Flow/FlowUpgrade.cs · 90 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 9 | public abstract class FlowUpgrade : IJsonSource |
| 15 | public abstract string DisplayName { get; } |
| 17 | public abstract string IconName { get; } |
| 19 | public virtual string UpgradeType => GetType().Name |
| 21 | public virtual double CostMultiplier => 1.0 |
| 23 | public virtual IEnumerable<Currency> CostCurrency => null |
| 25 | public virtual int MinCostTier => 0 |
| 27 | public abstract string GetDescription(FlowElement forElement, int nthUpgrade) |
| 29 | public virtual float GetSpeedBonus(FlowElement forElement, int nthUpgrade) |
| 34 | public virtual float GetProductivityBonus(FlowElement forElement, int nthUpgrade) |
| 39 | public virtual float GetQualityBonus(FlowElement forElement, int nthUpgrade) |
| 44 | public virtual CurrencyCollection GetPurchaseCost(FlowElement element, int nthUpgrade = -1) |
| 53 | public virtual CurrencyCollection GetRefund(FlowElement element, int alreadyRefunded = 0) |
| 58 | public virtual FlowUpgrade CreateCopy() |
| 63 | public virtual bool IsAvailableFor(FlowElement flowElement) |
| 68 | protected abstract void DataToJson(JsonObject data) |
| 70 | protected abstract void DataFromJson(JsonObject data) |
| 72 | public JsonValue ToJson() |
| 79 | public static FlowUpgrade FromJson(JsonValue json) |
| 86 | public static FlowUpgrade Create(string name) |

## Documented by

| Wiki article |
| --- |
| [Workers, upgrades, stacking, and refunds](production-upgrades.md) |

## Sources

- `Assets.Source.Flow/FlowUpgrade.cs:1`
