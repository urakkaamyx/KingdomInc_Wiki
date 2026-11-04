# Amulet of Dark Tidings

Projects an aura of death and hopelessness in an attempt to protect the wearer and their allies from dark magic.

## In the game

Projects an aura of death and hopelessness in an attempt to protect the wearer and their allies from dark magic.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | amulet_of_shadow_prot |
| Item type | Equipment |
| Slot | Amulet |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Magic | 20 |

## Traits

| Trait |
| --- |
| [Shadow Resist](trait-ShadowResist.md) |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Amulet of Dark Tidings](recipe-amulet_of_shadow_prot.md) | [Jeweler](building-Jeweler.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_217\"",
  "Slot": "EquipmentSlot.Amulet",
  "BaseStats": "new StatSet { (stat: EquipStat.Magic, amt: 20) }",
  "EquipTrait": "new AdventurerTrait\n\t\t\t{\n\t\t\t\tDisplayName = \"@amulet_of_shadow_prot\",\n\t\t\t\tGetDescription = (ActiveTrait trait) => Translation.TranslateOnly(\"@amulet_of_shadow_prot_trait\", GameMath.FormatPercentage(AdventurerTrait.Resist(trait.Quality))),\n\t\t\t\tIconName = \"Icons2_217\",\n\t\t\t\tApplyGroupBuffs = (ActiveTrait trait, CombatantItemData target, object context) =>\n\t\t\t\t{\n\t\t\t\t\ttarget.ApplyBuff(AdventurerTrait.ShadowResist, trait.Quality);\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier8.cs:205`
