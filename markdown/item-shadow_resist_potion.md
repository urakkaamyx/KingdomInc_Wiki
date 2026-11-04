# Elixir of Shadow Resistance

A dark purple brew. Trying to drink it evokes an almost primal fear in most people.

## In the game

A dark purple brew. Trying to drink it evokes an almost primal fear in most people.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | shadow_resist_potion |
| Item type | Equipment |
| Slot | Potion |
| Resource Cost | new CurrencyCollection().Add(Currency.Ring, 12L) |
| Tag | Adventure Supplies |

## Traits

| Trait |
| --- |
| [Shadow Resist](trait-ShadowResist.md) |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Elixir of Shadow Resistance](recipe-shadow_resist_potion.md) | [Alchemist](building-Alchemist.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_183\"",
  "Slot": "EquipmentSlot.Potion",
  "ResourceCost": "new CurrencyCollection().Add(Currency.Ring, 12L)",
  "Tag": "ResourceTag.AdventureSupplies",
  "EquipTrait": "AdventurerTrait.ShadowResist"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier9.cs:29`
