# DungeonLimitBreak2 — source reference

Assets.Source.Flow.Upgrades/DungeonLimitBreak2.cs · 20 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 6 | public class DungeonLimitBreak2 : DungeonLimitBreak |
| 8 | public const float FaithPerEnergy = 5f |
| 10 | public override string DisplayName => "@dungeon_limit_break_2" |
| 12 | public override string IconName => "Icons2_50" |
| 14 | public override IEnumerable<Currency> CostCurrency => CurrencyCollection.GoldFaith |
| 16 | public override string GetDescription(FlowElement forElement, int nthUpgrade) |

## Documented by

| Wiki article |
| --- |
| [Energy, death, and dungeon limit breaks](energy-death-and-limit-break.md) |
| [Unshakable Devotion](upgrade-DungeonLimitBreak2.md) |

## Sources

- `Assets.Source.Flow.Upgrades/DungeonLimitBreak2.cs:1`
