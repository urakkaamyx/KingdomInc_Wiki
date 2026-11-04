# Amulet of Fire Protection

Envelops the wearer and their allies in a protective shroud that wards off fire and extreme heat.

## In the game

Envelops the wearer and their allies in a protective shroud that wards off fire and extreme heat.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | amulet_of_fire_prot |
| Item type | Equipment |
| Slot | Amulet |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Strength | 20 |

## Traits

| Trait |
| --- |
| [Fire Resist](trait-FireResist.md) |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Amulet of Fire Protection](recipe-amulet_of_fire_prot.md) | [Jeweler](building-Jeweler.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_214\"",
  "Slot": "EquipmentSlot.Amulet",
  "BaseStats": "new StatSet { (stat: EquipStat.Strength, amt: 20) }",
  "EquipTrait": "new AdventurerTrait\n\t\t\t{\n\t\t\t\tDisplayName = \"@amulet_of_fire_prot\",\n\t\t\t\tGetDescription = (ActiveTrait trait) => Translation.TranslateOnly(\"@amulet_of_fire_prot_trait\", GameMath.FormatPercentage(AdventurerTrait.Resist(trait.Quality))),\n\t\t\t\tIconName = \"Icons2_214\",\n\t\t\t\tApplyGroupBuffs = (ActiveTrait trait, CombatantItemData target, object context) =>\n\t\t\t\t{\n\t\t\t\t\ttarget.ApplyBuff(AdventurerTrait.FireResist, trait.Quality);\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier8.cs:189`
