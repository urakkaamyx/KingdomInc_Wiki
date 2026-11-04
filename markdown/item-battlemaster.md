# Battlemaster

A fighter that has specialized in brutal combat.

## In the game

A fighter that has specialized in brutal combat.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | battlemaster |
| Item type | Adventurer |
| Resource Value | 4000 |
| Archetype | Fighter |
| Power Stat | Strength |
| Power Multiplier | 1.5 |
| Source Quest | true |

## Class advancement

Requirements are evaluated against the individual adventurer. Exact predicates are shown for conditional equipment requirements.

| Result | Where | Requirement |
| --- | --- | --- |
| [Berserker](item-berserker.md) | Arena | (HumanItemData adv) => !adv.HasArmorType(ArmorType.Heavy) |
| [Reaver](item-reaver.md) | Arena | (HumanItemData adv) => adv.HasDualWield |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_98\"",
  "ResourceValue": "4000L",
  "Archetype": "AdventurerArchetype.Fighter",
  "PowerStat": "EquipStat.Strength",
  "PowerMultiplier": "1.5f",
  "AdvancementUnlocked": "(GamePlayer ply) => ply.HasTech(\"farmstead_liberator\")",
  "SourceQuest": "true",
  "ClassTraits": "new List<AdventurerTrait> { AdventurerTrait.ClassBattlemaster }",
  "Advancements": "new List<AdventurerAdvancement>\n\t\t\t{\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@berserker\",\n\t\t\t\t\tDescription = \"@berserker_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_115\",\n\t\t\t\t\tSource = AdvancementSource.Arena,\n\t\t\t\t\tAvailable = (HumanItemData adv) => !adv.HasArmorType(ArmorType.Heavy),\n\t\t\t\t\tApply = (HumanItemData adv) =>\n\t\t\t\t\t{\n\t\t\t\t\t\tadv.Item.ChangeItemType(\"berserker\");\n\t\t\t\t\t}\n\t\t\t\t},\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@reaver\",\n\t\t\t\t\tDescription = \"@reaver_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_117\",\n\t\t\t\t\tSource = AdvancementSource.Arena,\n\t\t\t\t\tAvailable = (HumanItemData adv) => adv.HasDualWield,\n\t\t\t\t\tApply = (HumanItemData adv) =>\n\t\t\t\t\t{\n\t\t\t\t\t\tadv.Item.ChangeItemType(\"reaver\");\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:238`
