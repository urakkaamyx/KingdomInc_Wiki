# Barracks — source reference

Assets.Source.Flow.Elements/Barracks.cs · 30 lines · 3 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 6 | public class Barracks : ResourceElement |
| 8 | public override string DefaultLabel => "@barracks" |
| 10 | public override string DefaultIconName => "Icons_60" |
| 12 | public override string ActionLabel => "@barracks_resource_action" |
| 14 | public override string MusicTrack => "Deep Dungeon LOOP BPM90" |
| 16 | public override string Label => DefaultLabel |
| 18 | public override float OutputPerSecond => 0.5f * Speed |
| 20 | public override float QualityResourceCost => 2f |
| 22 | public Barracks() |

## Documented by

| Wiki article |
| --- |
| [Barracks](building-Barracks.md) |
| [Barracks, Adventurers Guilds, and mercenaries](production-recruitment.md) |
| [War Effort combat, medals, and defense](war-effort-mechanics.md) |

## Sources

- `Assets.Source.Flow.Elements/Barracks.cs:1`
