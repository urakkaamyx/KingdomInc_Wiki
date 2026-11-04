# Elixir of Alacrity

A highly concentrated emerald liquid. It hones the drinker's quick wit and reflexes, making rapid actions easier to execute.

## In the game

A highly concentrated emerald liquid. It hones the drinker's quick wit and reflexes, making rapid actions easier to execute.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | swiftness_potion |
| Item type | Equipment |
| Slot | Potion |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Dexterity | 12 |

## Traits

| Trait |
| --- |
| [Dexterity Skill Crit](trait-DexteritySkillCrit.md) |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Elixir of Alacrity](recipe-swiftness_potion.md) | [Alchemist](building-Alchemist.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_158\"",
  "Slot": "EquipmentSlot.Potion",
  "BaseStats": "new StatSet { \n\t\t\t{\n\t\t\t\tEquipStat.Dexterity,\n\t\t\t\t12\n\t\t\t} }",
  "EquipTrait": "AdventurerTrait.DexteritySkillCrit"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier9.cs:83`
