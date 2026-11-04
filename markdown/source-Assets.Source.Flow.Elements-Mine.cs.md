# Mine — source reference

Assets.Source.Flow.Elements/Mine.cs · 41 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 6 | public class Mine : ResourceElement |
| 8 | public override string DefaultLabel => "@mine" |
| 10 | public override string DefaultIconName => "Icons_1" |
| 12 | public override string ActionLabel => "@mine_resource_action" |
| 14 | public override string MusicTrack => "Adventure Puzzle LOOP BPM120" |
| 16 | public override string Label => Resource?.Identifier switch |
| 25 | public Mine() |
| 33 | public override CurrencyCollection GetPurchaseCost(int numElements) |

## Documented by

| Wiki article |
| --- |
| [Mine](building-Mine.md) |
| [Mines and supply depots](production-mines-suppliers.md) |

## Sources

- `Assets.Source.Flow.Elements/Mine.cs:1`
