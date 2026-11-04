# Ranger

A rogue that has specialized in ranged combat.

## In the game

A rogue that has specialized in ranged combat.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | ranger |
| Item type | Adventurer |
| Resource Value | 4000 |
| Archetype | Rogue |
| Power Stat | Dexterity |
| Power Multiplier | 1.5 |
| Source Quest | true |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Feeding the Wildlife](recipe-cr_beast_master.md) | 1 |
| [Study on Phytotoxins](recipe-cr_survivalist.md) | 1 |

## Class advancement

Requirements are evaluated against the individual adventurer. Exact predicates are shown for conditional equipment requirements.

| Result | Where | Requirement |
| --- | --- | --- |
| Beast Master | Crafting | See advancement implementation |
| Survivalist | Crafting | See advancement implementation |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_102\"",
  "ResourceValue": "4000L",
  "Archetype": "AdventurerArchetype.Rogue",
  "PowerStat": "EquipStat.Dexterity",
  "PowerMultiplier": "1.5f",
  "AdvancementUnlocked": "(GamePlayer ply) => ply.HasTech(\"byrgenwald_expedition\")",
  "SourceQuest": "true",
  "ClassTraits": "new List<AdventurerTrait> { AdventurerTrait.ClassRanger }",
  "Advancements": "new List<AdventurerAdvancement>\n\t\t\t{\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@beast_master\",\n\t\t\t\t\tDescription = \"@beast_master_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_123\",\n\t\t\t\t\tSource = AdvancementSource.Crafting\n\t\t\t\t},\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@survivalist\",\n\t\t\t\t\tDescription = \"@survivalist_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_125\",\n\t\t\t\t\tSource = AdvancementSource.Crafting\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:309`
