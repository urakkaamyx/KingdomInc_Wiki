# Softwood Plank

Freshly sawn from a softwood log, ready for further processing.

## In the game

Freshly sawn from a softwood log, ready for further processing.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | wood_plank |
| Item type | Resource |
| Resource Value | 100 |
| Quota Amount | 0.5 |
| Quota Base Cost | ResourceItemType.DefaultResourceCost * 1.2 |
| Tag | Supply |

## Gathering

| Building | Research | Quota step |
| --- | --- | --- |
| [Supply Depot](building-SupplyDepot.md) | [Supply Wood Plank](tech-supply_wood_plank.md) | 0.5 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Softwood Plank](recipe-wood_plank.md) | [Carpenter](building-Carpenter.md) | 2.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Iron Sword](recipe-iron_sword.md) | 1 |
| [Iron Dagger](recipe-iron_dagger.md) | 1 |
| [Iron Greatsword](recipe-iron_greatsword.md) | 1 |
| [Iron Battleaxe](recipe-iron_battleaxe.md) | 2 |
| [Softwood Bow](recipe-softwood_bow.md) | 2 |
| [Initiate's Staff](recipe-initiate_staff.md) | 3 |
| [Softwood Warstaff](recipe-softwood_warstaff.md) | 2 |
| [Simple Wooden Shield](recipe-simple_wooden_shield.md) | 3 |
| [Staff of the Wild](recipe-wild_staff.md) | 3 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_14\"",
  "ResourceValue": "100L",
  "QuotaAmount": "0.5",
  "QuotaBaseCost": "ResourceItemType.DefaultResourceCost * 1.2",
  "Tag": "ResourceTag.Supply"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier1.cs:16`
