# Triune Protector

A portable anti-magic shield that protects the wearer from Fire, Shadow and Poison damage all at the same time.

## In the game

A portable anti-magic shield that protects the wearer from Fire, Shadow and Poison damage all at the same time.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | triune_shield |
| Item type | Equipment |
| Slot | Trinket |

## Traits

| Trait |
| --- |
| [Fire Resist](trait-FireResist.md) |
| [Shadow Resist](trait-ShadowResist.md) |
| [Poison Resist](trait-PoisonResist.md) |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Triune Protector](recipe-triune_shield.md) | [Inventor](building-Inventor.md) | 2.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_55\"",
  "Slot": "EquipmentSlot.Trinket",
  "EquipTrait": "new AdventurerTrait\n\t\t\t{\n\t\t\t\tIconName = \"Icons3_55\",\n\t\t\t\tDisplayName = \"@triune_shield\",\n\t\t\t\tDescription = \"@triune_shield_desc\",\n\t\t\t\tApplyGroupBuffs = (ActiveTrait trait, CombatantItemData target, object context) =>\n\t\t\t\t{\n\t\t\t\t\tif (target == trait.Self)\n\t\t\t\t\t{\n\t\t\t\t\t\ttarget.ApplyBuff(AdventurerTrait.FireResist, trait.Quality);\n\t\t\t\t\t\ttarget.ApplyBuff(AdventurerTrait.ShadowResist, trait.Quality);\n\t\t\t\t\t\ttarget.ApplyBuff(AdventurerTrait.PoisonResist, trait.Quality);\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:260`
