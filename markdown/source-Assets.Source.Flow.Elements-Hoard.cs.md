# Hoard — source reference

Assets.Source.Flow.Elements/Hoard.cs · 41 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class Hoard : Armory |
| 9 | public override string Label => "@hoard" |
| 11 | public override string IconName => "Icons2_65" |
| 13 | public override int BaseInputCost => 0 |
| 15 | public override int MaxItems => 80 |
| 17 | public override string TooltipDescription => "@HoardTTDesc" |
| 19 | public override TechNode ChannelTech => null |
| 21 | public Hoard() |
| 29 | public override bool CanAcceptItem(ItemType i) |

## Documented by

| Wiki article |
| --- |
| [Hoard](building-Hoard.md) |
| [Armories and shared item storage](production-global-storage.md) |

## Sources

- `Assets.Source.Flow.Elements/Hoard.cs:1`
