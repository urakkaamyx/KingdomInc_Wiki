# Worker — source reference

Assets.Source.Flow.Upgrades/Worker.cs · 49 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class Worker : FlowUpgrade |
| 9 | public const float SpeedBonus = 0.5f |
| 11 | public override string DisplayName => "@worker" |
| 13 | public override string IconName => "Icons_17" |
| 15 | public override float GetSpeedBonus(FlowElement forElement, int nthUpgrade) |
| 24 | public override string GetDescription(FlowElement forElement, int nthUpgrade) |
| 33 | public override bool IsAvailableFor(FlowElement flowElement) |
| 42 | protected override void DataToJson(JsonObject data) |
| 46 | protected override void DataFromJson(JsonObject data) |

## Documented by

| Wiki article |
| --- |
| [Workers, upgrades, stacking, and refunds](production-upgrades.md) |
| [Worker](upgrade-Worker.md) |

## Sources

- `Assets.Source.Flow.Upgrades/Worker.cs:1`
