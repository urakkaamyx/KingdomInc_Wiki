# Guildhouse — source reference

Assets.Source.Flow.Elements/Guildhouse.cs · 41 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class Guildhouse : Armory |
| 11 | public override string Label => "@guildhouse" |
| 13 | public override string IconName => "Icons_196" |
| 15 | public override int BaseInputCost => 200 |
| 17 | public override int MaxItems => 5 |
| 19 | public override string TooltipDescription => "@GuildhouseTTDesc" |
| 21 | public Guildhouse() |
| 33 | public override bool CanAcceptItem(ItemType i) |

## Documented by

| Wiki article |
| --- |
| [Guildhouse](building-Guildhouse.md) |
| [Armories and shared item storage](production-global-storage.md) |

## Sources

- `Assets.Source.Flow.Elements/Guildhouse.cs:1`
