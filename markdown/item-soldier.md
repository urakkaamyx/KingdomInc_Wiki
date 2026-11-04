# Soldier

The backbone of any professional army.

## In the game

The backbone of any professional army.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | soldier |
| Item type | Human |
| Resource Value | 1500 |
| Power Multiplier | 1.25 |

## Class advancement

Requirements are evaluated against the individual adventurer. Exact predicates are shown for conditional equipment requirements.

| Result | Where | Requirement |
| --- | --- | --- |
| [Crusader](item-crusader.md) | Arena Win | (HumanItemData adv) => adv.HasWeapon && adv.GetEquippedItem(EquipmentSlot.Head) != null && adv.GetEquippedItem(EquipmentSlot.Chest) != null |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_181\"",
  "ResourceValue": "1500L",
  "PowerMultiplier": "1.25f",
  "Advancements": "new List<AdventurerAdvancement>\n\t\t\t{\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@crusader\",\n\t\t\t\t\tDescription = \"@crusader_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_63\",\n\t\t\t\t\tSource = AdvancementSource.ArenaWin,\n\t\t\t\t\tAvailable = (HumanItemData adv) => adv.HasWeapon && adv.GetEquippedItem(EquipmentSlot.Head) != null && adv.GetEquippedItem(EquipmentSlot.Chest) != null,\n\t\t\t\t\tApply = (HumanItemData adv) =>\n\t\t\t\t\t{\n\t\t\t\t\t\tadv.Item.ChangeItemType(\"crusader\");\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier3.cs:56`
