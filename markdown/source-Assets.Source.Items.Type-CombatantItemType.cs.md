# CombatantItemType — source reference

Assets.Source.Items.Type/CombatantItemType.cs · 64 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public class CombatantItemType(string id) : ResourceItemType(id) |
| 13 | public StatSet BaseStats = new StatSet() |
| 15 | public float PowerMultiplier = 1f |
| 17 | public List<AdventurerTrait> ClassTraits |
| 19 | public WeaponType WeaponTypeOverride |
| 21 | public override ItemData CreateItemData(InventoryItem item) |
| 26 | public override int GetAppraiserStat(InventoryItem item, AppraiserStat stat) |
| 45 | public override void AddToTooltip(InventoryItem item, UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Filters, Appraisers, and Accountants](routing-filter-appraiser-accountant.md) |

## Sources

- `Assets.Source.Items.Type/CombatantItemType.cs:1`
