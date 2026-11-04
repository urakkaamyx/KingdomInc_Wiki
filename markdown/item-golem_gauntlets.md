# Golem Gauntlets

Enhances the wearer's natural strength, allowing them to lift heavy boulders with ease.

## In the game

Enhances the wearer's natural strength, allowing them to lift heavy boulders with ease.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | golem_gauntlets |
| Item type | Equipment |
| Slot | Trinket |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Strength | 20 |

## Traits

| Trait |
| --- |
| [Strength Skill Crit](trait-StrengthSkillCrit.md) |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Golem Gauntlets](recipe-golem_gauntlets.md) | [Inventor](building-Inventor.md) | 2.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_51\"",
  "Slot": "EquipmentSlot.Trinket",
  "BaseStats": "new StatSet { (stat: EquipStat.Strength, amt: 20) }",
  "EquipTrait": "AdventurerTrait.StrengthSkillCrit"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:227`
