# Panacea Amulet

Creates a detoxifying aura that protects the wearer and their allies from even the most vile poisons.

## In the game

Creates a detoxifying aura that protects the wearer and their allies from even the most vile poisons.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | amulet_of_poison_prot |
| Item type | Equipment |
| Slot | Amulet |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Dexterity | 20 |

## Traits

| Trait |
| --- |
| [Poison Resist](trait-PoisonResist.md) |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Panacea Amulet](recipe-amulet_of_poison_prot.md) | [Jeweler](building-Jeweler.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_218\"",
  "Slot": "EquipmentSlot.Amulet",
  "BaseStats": "new StatSet { (stat: EquipStat.Dexterity, amt: 20) }",
  "EquipTrait": "new AdventurerTrait\n\t\t\t{\n\t\t\t\tDisplayName = \"@amulet_of_poison_prot\",\n\t\t\t\tGetDescription = (ActiveTrait trait) => Translation.TranslateOnly(\"@amulet_of_poison_prot_trait\", GameMath.FormatPercentage(AdventurerTrait.Resist(trait.Quality))),\n\t\t\t\tIconName = \"Icons2_218\",\n\t\t\t\tApplyGroupBuffs = (ActiveTrait trait, CombatantItemData target, object context) =>\n\t\t\t\t{\n\t\t\t\t\ttarget.ApplyBuff(AdventurerTrait.PoisonResist, trait.Quality);\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier8.cs:221`
