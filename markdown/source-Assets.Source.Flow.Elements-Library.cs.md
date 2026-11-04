# Library — source reference

Assets.Source.Flow.Elements/Library.cs · 33 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class Library : Armory |
| 9 | public override string Label => "@library" |
| 11 | public override string IconName => "Icons2_40" |
| 13 | public override string TooltipDescription => "@LibraryTTDesc" |
| 15 | public override int MaxItems => 5 |
| 17 | public Library() |
| 25 | public override bool CanAcceptItem(ItemType i) |

## Documented by

| Wiki article |
| --- |
| [Library](building-Library.md) |
| [Armories and shared item storage](production-global-storage.md) |

## Sources

- `Assets.Source.Flow.Elements/Library.cs:1`
