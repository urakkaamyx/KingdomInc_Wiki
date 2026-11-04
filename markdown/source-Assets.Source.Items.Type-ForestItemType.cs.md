# ForestItemType — source reference

Assets.Source.Items.Type/ForestItemType.cs · 23 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 5 | public class ForestItemType : ItemType |
| 7 | public ForestWorker WorkerType |
| 9 | public double WorkersPerItem = 1.0 |
| 11 | public long ResourceValue |
| 13 | public CurrencyCollection HarvestCost |
| 15 | public override long BaseValue => ResourceValue |
| 17 | public override bool IsUnlocked => GamePlayer.Current.ForestSettings?.ItemUnlocked(this) ?? false |
| 19 | public ForestItemType(string id) |

## Documented by

| Wiki article |
| --- |
| [Farm plots and planting controls](farm-panel-controls.md) |

## Sources

- `Assets.Source.Items.Type/ForestItemType.cs:1`
