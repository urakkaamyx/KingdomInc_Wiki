# Revitalizing Potion

A pale yellow potion that instantly re-energizes even the most tired soul.

## In the game

A pale yellow potion that instantly re-energizes even the most tired soul.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | energy_potion |
| Item type | Equipment |
| Slot | Potion |
| Resource Cost | new CurrencyCollection().Add(Currency.Ring, 6L) |
| Tag | Adventure Supplies |

## Traits

| Trait |
| --- |
| [Energy Potion](trait-EnergyPotion.md) |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Revitalizing Potion](recipe-energy_potion.md) | [Alchemist](building-Alchemist.md) | 2.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_194\"",
  "Slot": "EquipmentSlot.Potion",
  "ResourceCost": "new CurrencyCollection().Add(Currency.Ring, 6L)",
  "Tag": "ResourceTag.AdventureSupplies",
  "EquipTrait": "AdventurerTrait.EnergyPotion"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier5.cs:19`
