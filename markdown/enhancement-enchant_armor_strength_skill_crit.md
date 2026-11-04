# Enchant Armor - Giant Strength

Enchants any piece of Head or Chest armor to increase success chance on any Strength checks in combat. Also provides a small amount of Strength.

## Effect

Enchants any piece of Head or Chest armor to increase success chance on any Strength checks in combat. Also provides a small amount of Strength.

## Base stat modifiers

Enhancement quality and application rules determine the final contribution.

| Stat | Amount at definition quality |
| --- | --- |
| Strength | 16 |

## Properties

| Property | Value |
| --- | --- |
| Type | Enchant |
| Equip Trait | Strength Skill Crit |

## Applied traits

| Trait |
| --- |
| [Strength Skill Crit](trait-StrengthSkillCrit.md) |

## Application recipes

| Recipe | Station |
| --- | --- |
| [Enchant Armor - Giant Strength](recipe-enchant_armor_strength_skill_crit.md) | [Enchanter](building-Enchanter.md) |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_184\"",
  "Type": "EnhancementType.Enchant",
  "Stats": "new StatSet { \n\t\t\t{\n\t\t\t\tEquipStat.Strength,\n\t\t\t\t16\n\t\t\t} }",
  "EquipTrait": "AdventurerTrait.StrengthSkillCrit"
}
```

</details>

## Sources

- `Assets.Source.Items.Enhancements/Enchanter.cs:91`
