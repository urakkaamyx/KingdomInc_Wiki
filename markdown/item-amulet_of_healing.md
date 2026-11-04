# Amulet of Vitality

A brilliant red ruby pendant that invigorates the wearer.

## In the game

A brilliant red ruby pendant that invigorates the wearer.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | amulet_of_healing |
| Item type | Equipment |
| Slot | Amulet |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Health | 50 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Amulet of Vitality](recipe-amulet_of_healing.md) | [Jeweler](building-Jeweler.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_215\"",
  "Slot": "EquipmentSlot.Amulet",
  "BaseStats": "new StatSet { (stat: EquipStat.Health, amt: 50) }",
  "EquipTrait": "new AdventurerTrait\n\t\t\t{\n\t\t\t\tDisplayName = \"@lifebearer\",\n\t\t\t\tGetDescription = (ActiveTrait trait) => Translation.TranslateOnly(\"@lifebearer_desc\", GameMath.FormatPercentage(0.2f * trait.Quality)),\n\t\t\t\tIconName = \"Icons_216\",\n\t\t\t\tCalcHealingTaken = (ActiveTrait trait, float heal, object target) => heal * (1f + 0.2f * trait.Quality)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier8.cs:131`
