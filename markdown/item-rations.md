# Rations

Uninteresting but nutritious.

## In the game

Uninteresting but nutritious.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | rations |
| Item type | Equipment |
| Slot | Food |
| Resource Value | 1100 |
| Resource Cost | new CurrencyCollection().Add(Currency.Ring, 2L) |
| Tag | Adventure Supplies |

## Traits

| Trait |
| --- |
| [Training Food](trait-TrainingFood.md) |

## Gathering

| Building | Research | Quota step |
| --- | --- | --- |
| [Adventure Supplies](building-AdventureSupplies.md) | [Supply rations](tech-supply_rations.md) | 1.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_220\"",
  "Slot": "EquipmentSlot.Food",
  "ResourceValue": "1100L",
  "ResourceCost": "new CurrencyCollection().Add(Currency.Ring, 2L)",
  "Tag": "ResourceTag.AdventureSupplies",
  "EquipTrait": "AdventurerTrait.TrainingFood"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier5.cs:27`
