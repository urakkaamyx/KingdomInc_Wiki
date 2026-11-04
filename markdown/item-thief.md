# Thief

A rogue that has specialized in sneaky, underhanded tactics.

## In the game

A rogue that has specialized in sneaky, underhanded tactics.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | thief |
| Item type | Adventurer |
| Resource Value | 4000 |
| Archetype | Rogue |
| Power Stat | Dexterity |
| Power Multiplier | 1.5 |
| Source Quest | true |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Anatomy Lesson](recipe-cr_assassin.md) | 1 |

## Class advancement

Requirements are evaluated against the individual adventurer. Exact predicates are shown for conditional equipment requirements.

| Result | Where | Requirement |
| --- | --- | --- |
| Assassin | Crafting | See advancement implementation |
| [Swashbuckler](item-swashbuckler.md) | Arena | (HumanItemData adv) => adv.HasDualWield |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_100\"",
  "ResourceValue": "4000L",
  "Archetype": "AdventurerArchetype.Rogue",
  "PowerStat": "EquipStat.Dexterity",
  "PowerMultiplier": "1.5f",
  "AdvancementUnlocked": "(GamePlayer ply) => ply.HasTech(\"bank_heist\")",
  "SourceQuest": "true",
  "ClassTraits": "new List<AdventurerTrait> { AdventurerTrait.ClassThief }",
  "Advancements": "new List<AdventurerAdvancement>\n\t\t\t{\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@assassin\",\n\t\t\t\t\tDescription = \"@assassin_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_119\",\n\t\t\t\t\tSource = AdvancementSource.Crafting\n\t\t\t\t},\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@swashbuckler\",\n\t\t\t\t\tDescription = \"@swashbuckler_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_121\",\n\t\t\t\t\tSource = AdvancementSource.Arena,\n\t\t\t\t\tAvailable = (HumanItemData adv) => adv.HasDualWield,\n\t\t\t\t\tApply = (HumanItemData adv) =>\n\t\t\t\t\t{\n\t\t\t\t\t\tadv.Item.ChangeItemType(\"swashbuckler\");\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:276`
