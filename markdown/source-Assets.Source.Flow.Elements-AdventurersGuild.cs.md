# AdventurersGuild — source reference

Assets.Source.Flow.Elements/AdventurersGuild.cs · 45 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 6 | public class AdventurersGuild : ResourceElement |
| 12 | public override string DefaultLabel => "@adventurers_guild" |
| 14 | public override string DefaultIconName => "Icons_67" |
| 16 | public override string ActionLabel => "@guild_resource_action" |
| 18 | public override string MusicTrack => "Kingdom Wonder LOOP BPM70" |
| 20 | public override string Label => DefaultLabel |
| 22 | public override float OutputPerSecond => (_warProgressed ? 0.5f : 0f) * Speed |
| 24 | public override float QualityResourceCost => 2f |
| 26 | public AdventurersGuild() |
| 35 | public override void Update(float delta) |

## Documented by

| Wiki article |
| --- |
| [Adventurer's Guild](building-AdventurersGuild.md) |
| [Barracks, Adventurers Guilds, and mercenaries](production-recruitment.md) |

## Sources

- `Assets.Source.Flow.Elements/AdventurersGuild.cs:1`
