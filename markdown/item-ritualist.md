# Ritualist

A cleric that has specialized in the offensive side of religion.

## In the game

A cleric that has specialized in the offensive side of religion.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | ritualist |
| Item type | Adventurer |
| Resource Value | 4000 |
| Archetype | Cleric |
| Power Stat | Wisdom |
| Power Multiplier | 1.15 |
| Source Quest | true |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Commune with Nature](recipe-cr_shaman.md) | 1 |

## Class advancement

Requirements are evaluated against the individual adventurer. Exact predicates are shown for conditional equipment requirements.

| Result | Where | Requirement |
| --- | --- | --- |
| Shaman | Crafting | See advancement implementation |
| [Inquisitor](item-inquisitor.md) | Arena | (HumanItemData adv) => (adv.GetEquippedItem(EquipmentSlot.MainHand)?.GetAppraiserStat(AppraiserStat.Strength) ?? 0) > 0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_108\"",
  "ResourceValue": "4000L",
  "Archetype": "AdventurerArchetype.Cleric",
  "PowerStat": "EquipStat.Wisdom",
  "PowerMultiplier": "1.15f",
  "AdvancementUnlocked": "(GamePlayer ply) => ply.HasTech(\"extinguish_ritual\")",
  "SourceQuest": "true",
  "ClassTraits": "new List<AdventurerTrait>\n\t\t\t{\n\t\t\t\tAdventurerTrait.ClassRitualist,\n\t\t\t\tAdventurerTrait.Healer\n\t\t\t}",
  "Advancements": "new List<AdventurerAdvancement>\n\t\t\t{\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@shaman\",\n\t\t\t\t\tDescription = \"@shaman_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_135\",\n\t\t\t\t\tSource = AdvancementSource.Crafting\n\t\t\t\t},\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@inquisitor\",\n\t\t\t\t\tDescription = \"@inquisitor_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_137\",\n\t\t\t\t\tSource = AdvancementSource.Arena,\n\t\t\t\t\tAvailable = (HumanItemData adv) => (adv.GetEquippedItem(EquipmentSlot.MainHand)?.GetAppraiserStat(AppraiserStat.Strength) ?? 0) > 0,\n\t\t\t\t\tApply = (HumanItemData adv) =>\n\t\t\t\t\t{\n\t\t\t\t\t\tadv.Item.ChangeItemType(\"inquisitor\");\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:393`
