# Adventurer

A rookie fresh off the boat, ready to make their mark on the world.

## In the game

A rookie fresh off the boat, ready to make their mark on the world.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | adventurer |
| Item type | Adventurer |
| Resource Value | 1500 |
| Resource Cost | new CurrencyCollection().Add(Currency.Medal, 4L) |
| Quota Amount | 0.1 |
| Quota Base Cost | new CurrencyCollection().Add(ResourceItemType.DefaultResourceCost * 2.0).Add(Currency.Ring, 10L) |
| Tag | Guild |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Energy | 100 |
| Health | 100 |
| Strength | 40 |
| Dexterity | 40 |
| Magic | 40 |
| Wisdom | 40 |

## Gathering

| Building | Research | Quota step |
| --- | --- | --- |
| [Adventurer's Guild](building-AdventurersGuild.md) | [Recruit Adventurers](tech-recruit_adventurer.md) | 0.1 |

## Class advancement

Requirements are evaluated against the individual adventurer. Exact predicates are shown for conditional equipment requirements.

| Result | Where | Requirement |
| --- | --- | --- |
| [Fighter](item-fighter.md) | Training Grounds | (HumanItemData adv) => adv.HasWeaponStat(EquipStat.Strength) && adv.HasArmorType(ArmorType.Heavy) |
| [Rogue](item-rogue.md) | Training Grounds | (HumanItemData adv) => adv.HasWeaponStat(EquipStat.Dexterity) && adv.HasArmorType(ArmorType.Medium) |
| [Mage](item-mage.md) | Training Grounds | (HumanItemData adv) => adv.HasWeaponStat(EquipStat.Magic) && adv.HasArmorType(ArmorType.Light) |
| [Cleric](item-cleric.md) | Training Grounds | (HumanItemData adv) => adv.HasWeaponStat(EquipStat.Wisdom) |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_139\"",
  "ResourceValue": "1500L",
  "ResourceCost": "new CurrencyCollection().Add(Currency.Medal, 4L)",
  "QuotaAmount": "0.1",
  "QuotaBaseCost": "new CurrencyCollection().Add(ResourceItemType.DefaultResourceCost * 2.0).Add(Currency.Ring, 10L)",
  "Tag": "ResourceTag.Guild",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Energy,\n\t\t\t\t\t100\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Health,\n\t\t\t\t\t100\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Strength,\n\t\t\t\t\t40\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Dexterity,\n\t\t\t\t\t40\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Magic,\n\t\t\t\t\t40\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Wisdom,\n\t\t\t\t\t40\n\t\t\t\t}\n\t\t\t}",
  "Advancements": "new List<AdventurerAdvancement>\n\t\t\t{\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@fighter\",\n\t\t\t\t\tDescription = \"@fighter_adv_desc\",\n\t\t\t\t\tIconName = \"Icons_167\",\n\t\t\t\t\tSource = AdvancementSource.TrainingGrounds,\n\t\t\t\t\tAvailable = (HumanItemData adv) => adv.HasWeaponStat(EquipStat.Strength) && adv.HasArmorType(ArmorType.Heavy),\n\t\t\t\t\tApply = (HumanItemData adv) =>\n\t\t\t\t\t{\n\t\t\t\t\t\tadv.Item.ChangeItemType(\"fighter\");\n\t\t\t\t\t}\n\t\t\t\t},\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@rogue\",\n\t\t\t\t\tDescription = \"@rogue_adv_desc\",\n\t\t\t\t\tIconName = \"Icons_168\",\n\t\t\t\t\tSource = AdvancementSource.TrainingGrounds,\n\t\t\t\t\tAvailable = (HumanItemData adv) => adv.HasWeaponStat(EquipStat.Dexterity) && adv.HasArmorType(ArmorType.Medium),\n\t\t\t\t\tApply = (HumanItemData adv) =>\n\t\t\t\t\t{\n\t\t\t\t\t\tadv.Item.ChangeItemType(\"rogue\");\n\t\t\t\t\t}\n\t\t\t\t},\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@mage\",\n\t\t\t\t\tDescription = \"@mage_adv_desc\",\n\t\t\t\t\tIconName = \"Icons_165\",\n\t\t\t\t\tSource = AdvancementSource.TrainingGrounds,\n\t\t\t\t\tAvailable = (HumanItemData adv) => adv.HasWeaponStat(EquipStat.Magic) && adv.HasArmorType(ArmorType.Light),\n\t\t\t\t\tApply = (HumanItemData adv) =>\n\t\t\t\t\t{\n\t\t\t\t\t\tadv.Item.ChangeItemType(\"mage\");\n\t\t\t\t\t}\n\t\t\t\t},\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@cleric\",\n\t\t\t\t\tDescription = \"@cleric_adv_desc\",\n\t\t\t\t\tIconName = \"Icons_166\",\n\t\t\t\t\tSource = AdvancementSource.TrainingGrounds,\n\t\t\t\t\tAvailable = (HumanItemData adv) => adv.HasWeaponStat(EquipStat.Wisdom),\n\t\t\t\t\tApply = (HumanItemData adv) =>\n\t\t\t\t\t{\n\t\t\t\t\t\tadv.Item.ChangeItemType(\"cleric\");\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:13`
