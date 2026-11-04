# ManaPassive — source reference

Assets.Source.Flow.Upgrades/ManaPassive.cs · 36 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public class ManaPassive : FlowUpgrade |
| 10 | public const int ProfitPerTick = 3 |
| 12 | public const float TickTime = 1f |
| 14 | public override string DisplayName => "@disenchanter_passive" |
| 16 | public override string IconName => "Icons_162" |
| 18 | public override int MinCostTier => 3 |
| 20 | public override double CostMultiplier => 1.5 |
| 22 | public override IEnumerable<Currency> CostCurrency => CurrencyCollection.GoldMana |
| 24 | public override string GetDescription(FlowElement forElement, int nthUpgrade) |
| 29 | protected override void DataToJson(JsonObject data) |
| 33 | protected override void DataFromJson(JsonObject data) |

## Documented by

| Wiki article |
| --- |
| [Aether Collector](upgrade-ManaPassive.md) |

## Sources

- `Assets.Source.Flow.Upgrades/ManaPassive.cs:1`
