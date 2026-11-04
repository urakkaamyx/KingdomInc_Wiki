# Elixir of Fire Resistance

A vial of swirling orange liquid. Looks like you're drinking liquid fire, but the taste is surprisingly pleasant.

## In the game

A vial of swirling orange liquid. Looks like you're drinking liquid fire, but the taste is surprisingly pleasant.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | fire_resist_potion |
| Item type | Equipment |
| Slot | Potion |
| Resource Cost | new CurrencyCollection().Add(Currency.Ring, 12L) |
| Tag | Adventure Supplies |

## Traits

| Trait |
| --- |
| [Fire Resist](trait-FireResist.md) |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Elixir of Fire Resistance](recipe-fire_resist_potion.md) | [Alchemist](building-Alchemist.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_146\"",
  "Slot": "EquipmentSlot.Potion",
  "ResourceCost": "new CurrencyCollection().Add(Currency.Ring, 12L)",
  "Tag": "ResourceTag.AdventureSupplies",
  "EquipTrait": "AdventurerTrait.FireResist"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier9.cs:21`
