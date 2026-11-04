# ArenaBloodSport — source reference

Assets.Source.Flow.Upgrades/ArenaBloodSport.cs · 30 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 5 | public class ArenaBloodSport : FlowUpgrade |
| 7 | public override string DisplayName => "@arena_blood_sport_2" |
| 9 | public override string IconName => "Icons2_56" |
| 11 | public override double CostMultiplier => 1.5 |
| 13 | public override string GetDescription(FlowElement forElement, int nthUpgrade) |
| 18 | public override bool IsAvailableFor(FlowElement flowElement) |
| 23 | protected override void DataFromJson(JsonObject data) |
| 27 | protected override void DataToJson(JsonObject data) |

## Documented by

| Wiki article |
| --- |
| [Blood Sport](upgrade-ArenaBloodSport.md) |

## Sources

- `Assets.Source.Flow.Upgrades/ArenaBloodSport.cs:1`
