# FarmItemType — source reference

Assets.Source.Items.Type/FarmItemType.cs · 18 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 5 | public class FarmItemType : ResourceItemType |
| 7 | public double PlotYield = 1.0 |
| 9 | public CurrencyCollection HarvestCost |
| 11 | public override bool IsUnlocked => GamePlayer.Current.FarmSettings?.ItemUnlocked(this) ?? false |
| 13 | public FarmItemType(string id) |

## Documented by

| Wiki article |
| --- |
| [Farm plots and planting controls](farm-panel-controls.md) |

## Sources

- `Assets.Source.Items.Type/FarmItemType.cs:1`
