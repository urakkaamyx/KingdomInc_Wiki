# Healing Potion

A brilliant red potion that can instantly restore minor wounds.

## In the game

A brilliant red potion that can instantly restore minor wounds.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | healing_potion |
| Item type | Equipment |
| Slot | Potion |
| Resource Cost | new CurrencyCollection().Add(Currency.Ring, 4L) |
| Tag | Adventure Supplies |

## Traits

| Trait |
| --- |
| [Healing Potion](trait-HealingPotion.md) |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Healing Potion](recipe-healing_potion.md) | [Alchemist](building-Alchemist.md) | 2.5 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Scroll of Healing](recipe-scroll_of_healing.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_219\"",
  "Slot": "EquipmentSlot.Potion",
  "ResourceCost": "new CurrencyCollection().Add(Currency.Ring, 4L)",
  "Tag": "ResourceTag.AdventureSupplies",
  "EquipTrait": "AdventurerTrait.HealingPotion"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier5.cs:11`
