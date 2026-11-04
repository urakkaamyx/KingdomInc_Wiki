# TrainingArtisan — source reference

Assets.Source.Flow.Upgrades/TrainingArtisan.cs · 22 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 5 | public class TrainingArtisan : Artisan |
| 7 | public const float SpeedBonus = -0.2f |
| 9 | public override string DisplayName => "@training_artisan" |
| 11 | public override string IconName => "Icons2_160" |
| 13 | public override string GetDescription(FlowElement forElement, int nthUpgrade) |
| 18 | public override float GetSpeedBonus(FlowElement forElement, int nthUpgrade) |

## Documented by

| Wiki article |
| --- |
| [Workers, upgrades, stacking, and refunds](production-upgrades.md) |
| [Weight Rack](upgrade-TrainingArtisan.md) |

## Sources

- `Assets.Source.Flow.Upgrades/TrainingArtisan.cs:1`
