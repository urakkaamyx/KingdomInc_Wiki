# Treasury — source reference

Assets.Source.Flow.Elements/Treasury.cs · 37 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class Treasury : Armory |
| 9 | public override string Label => "@treasury" |
| 11 | public override string IconName => "Icons2_41" |
| 13 | public override string TooltipDescription => "@TreasuryTTDesc" |
| 15 | public override int MaxItems => 5 |
| 17 | public Treasury() |
| 25 | public override bool CanAcceptItem(ItemType i) |

## Documented by

| Wiki article |
| --- |
| [Treasury](building-Treasury.md) |
| [Armories and shared item storage](production-global-storage.md) |

## Sources

- `Assets.Source.Flow.Elements/Treasury.cs:1`
