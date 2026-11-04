# Winged Boots

A wondrous invention that allows the wearer to fly over short distances, making feats of dexterity more manageable.

## In the game

A wondrous invention that allows the wearer to fly over short distances, making feats of dexterity more manageable.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | winged_boots |
| Item type | Equipment |
| Slot | Trinket |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Dexterity | 20 |

## Traits

| Trait |
| --- |
| [Dexterity Skill Crit](trait-DexteritySkillCrit.md) |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Winged Boots](recipe-winged_boots.md) | [Inventor](building-Inventor.md) | 2.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_50\"",
  "Slot": "EquipmentSlot.Trinket",
  "BaseStats": "new StatSet { (stat: EquipStat.Dexterity, amt: 20) }",
  "EquipTrait": "AdventurerTrait.DexteritySkillCrit"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:220`
