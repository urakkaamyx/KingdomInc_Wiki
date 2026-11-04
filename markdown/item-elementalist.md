# Elementalist

A mage that has specialized in harnessing the wild elements.

## In the game

A mage that has specialized in harnessing the wild elements.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | elementalist |
| Item type | Adventurer |
| Resource Value | 4000 |
| Archetype | Mage |
| Power Stat | Magic |
| Power Multiplier | 1.5 |
| Source Quest | true |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Pyromancy and You: An Introduction](recipe-cr_pyromancer.md) | 1 |
| [Rock Carving for Dummies](recipe-cr_lithomancer.md) | 1 |

## Class advancement

Requirements are evaluated against the individual adventurer. Exact predicates are shown for conditional equipment requirements.

| Result | Where | Requirement |
| --- | --- | --- |
| Pyromancer | Crafting | See advancement implementation |
| Lithomancer | Crafting | See advancement implementation |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_104\"",
  "ResourceValue": "4000L",
  "Archetype": "AdventurerArchetype.Mage",
  "PowerStat": "EquipStat.Magic",
  "PowerMultiplier": "1.5f",
  "AdvancementUnlocked": "(GamePlayer ply) => ply.HasTech(\"elemental_eradication\")",
  "SourceQuest": "true",
  "ClassTraits": "new List<AdventurerTrait> { AdventurerTrait.ClassElementalist }",
  "Advancements": "new List<AdventurerAdvancement>\n\t\t\t{\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@pyromancer\",\n\t\t\t\t\tDescription = \"@pyromancer_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_127\",\n\t\t\t\t\tSource = AdvancementSource.Crafting\n\t\t\t\t},\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@lithomancer\",\n\t\t\t\t\tDescription = \"@lithomancer_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_129\",\n\t\t\t\t\tSource = AdvancementSource.Crafting\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:337`
