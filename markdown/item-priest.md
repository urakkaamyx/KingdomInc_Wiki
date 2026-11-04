# Priest

A cleric that has specialized in healing the sick and helping the needy.

## In the game

A cleric that has specialized in healing the sick and helping the needy.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | priest |
| Item type | Adventurer |
| Resource Value | 4000 |
| Archetype | Cleric |
| Power Stat | Wisdom |
| Power Multiplier | 1.15 |
| Source Quest | true |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Preaching to the Choir](recipe-cr_evangelist.md) | 1 |
| [Prayer of Light](recipe-cr_lightbringer.md) | 1 |

## Class advancement

Requirements are evaluated against the individual adventurer. Exact predicates are shown for conditional equipment requirements.

| Result | Where | Requirement |
| --- | --- | --- |
| Evangelist | Crafting | See advancement implementation |
| Lightbringer | Crafting | See advancement implementation |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_110\"",
  "ResourceValue": "4000L",
  "Archetype": "AdventurerArchetype.Cleric",
  "PowerStat": "EquipStat.Wisdom",
  "PowerMultiplier": "1.15f",
  "AdvancementUnlocked": "(GamePlayer ply) => ply.HasTech(\"aid_refugees\")",
  "SourceQuest": "true",
  "ClassTraits": "new List<AdventurerTrait>\n\t\t\t{\n\t\t\t\tAdventurerTrait.ClassPriest,\n\t\t\t\tAdventurerTrait.Healer\n\t\t\t}",
  "Advancements": "new List<AdventurerAdvancement>\n\t\t\t{\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@evangelist\",\n\t\t\t\t\tDescription = \"@evangelist_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_139\",\n\t\t\t\t\tSource = AdvancementSource.Crafting\n\t\t\t\t},\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@lightbringer\",\n\t\t\t\t\tDescription = \"@lightbringer_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_141\",\n\t\t\t\t\tSource = AdvancementSource.Crafting\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:430`
