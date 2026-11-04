# ResourceItemType — source reference

Assets.Source.Items/ResourceItemType.cs · 54 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 5 | public class ResourceItemType : ItemType |
| 7 | public static CurrencyCollection DefaultResourceCost = new CurrencyCollection().Add(Currency.Gold, 1950L) |
| 9 | public long ResourceValue |
| 11 | public CurrencyCollection ResourceCost |
| 13 | public double QuotaAmount = 1.0 |
| 15 | public double QuotaCostMultiplier = 1.2 |
| 17 | public CurrencyCollection QuotaBaseCost = DefaultResourceCost |
| 19 | public ResourceTag Tag |
| 21 | public override long BaseValue |
| 33 | public override bool IsUnlocked |
| 45 | public ResourceItemType(string id) |
| 50 | public static implicit operator ResourceItemType(string id) |

## Documented by

| Wiki article |
| --- |
| [Data records, serialization, and implementation limits](implementation-data-and-serialization.md) |

## Sources

- `Assets.Source.Items/ResourceItemType.cs:1`
