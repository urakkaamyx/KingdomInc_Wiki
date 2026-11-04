# Conscript

An untrained, unremarkable footsoldier in the war against Yensburg's enemies.

Can be equipped with any type of weapons and armor.

## In the game

An untrained, unremarkable footsoldier in the war against Yensburg's enemies.

Can be equipped with any type of weapons and armor.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | conscript |
| Item type | Human |
| Resource Value | 1000 |
| Resource Cost | new CurrencyCollection().Add(Currency.Requisition, 2L) |
| Quota Amount | 0.1 |
| Quota Base Cost | new CurrencyCollection().Add(ResourceItemType.DefaultResourceCost * 2.0).Add(Currency.Medal, 10L) |
| Tag | Barracks |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Health | 100 |
| Strength | 40 |
| Dexterity | 40 |
| Magic | 40 |

## Gathering

| Building | Research | Quota step |
| --- | --- | --- |
| [Barracks](building-Barracks.md) | [Recruit Conscripts](tech-recruit_conscript.md) | 0.1 |

## Class advancement

Requirements are evaluated against the individual adventurer. Exact predicates are shown for conditional equipment requirements.

| Result | Where | Requirement |
| --- | --- | --- |
| [Soldier](item-soldier.md) | Training Grounds | (HumanItemData adv) => adv.HasWeapon && adv.GetEquippedItem(EquipmentSlot.Head) != null && adv.GetEquippedItem(EquipmentSlot.Chest) != null |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_61\"",
  "ResourceValue": "1000L",
  "ResourceCost": "new CurrencyCollection().Add(Currency.Requisition, 2L)",
  "QuotaAmount": "0.1",
  "QuotaBaseCost": "new CurrencyCollection().Add(ResourceItemType.DefaultResourceCost * 2.0).Add(Currency.Medal, 10L)",
  "Tag": "ResourceTag.Barracks",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Health,\n\t\t\t\t\t100\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Strength,\n\t\t\t\t\t40\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Dexterity,\n\t\t\t\t\t40\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Magic,\n\t\t\t\t\t40\n\t\t\t\t}\n\t\t\t}",
  "Advancements": "new List<AdventurerAdvancement>\n\t\t\t{\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@soldier\",\n\t\t\t\t\tDescription = \"@soldier_adv_desc\",\n\t\t\t\t\tIconName = \"Icons_181\",\n\t\t\t\t\tAvailable = (HumanItemData adv) => adv.HasWeapon && adv.GetEquippedItem(EquipmentSlot.Head) != null && adv.GetEquippedItem(EquipmentSlot.Chest) != null,\n\t\t\t\t\tSource = AdvancementSource.TrainingGrounds,\n\t\t\t\t\tApply = (HumanItemData adv) =>\n\t\t\t\t\t{\n\t\t\t\t\t\tadv.Item.ChangeItemType(\"soldier\");\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier3.cs:13`
