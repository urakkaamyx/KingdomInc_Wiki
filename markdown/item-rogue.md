# Rogue

An adventurer that specializes in subtlety, agility and ranged combat.

## In the game

An adventurer that specializes in subtlety, agility and ranged combat.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | rogue |
| Item type | Adventurer |
| Resource Value | 2000 |
| Archetype | Rogue |
| Power Stat | Dexterity |
| Power Multiplier | 1.25 |
| Source Training | true |

## Class advancement

Requirements are evaluated against the individual adventurer. Exact predicates are shown for conditional equipment requirements.

| Result | Where | Requirement |
| --- | --- | --- |
| Thief | Quest | See advancement implementation |
| Ranger | Quest | See advancement implementation |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_169\"",
  "ResourceValue": "2000L",
  "Archetype": "AdventurerArchetype.Rogue",
  "PowerStat": "EquipStat.Dexterity",
  "PowerMultiplier": "1.25f",
  "SourceTraining": "true",
  "Advancements": "new List<AdventurerAdvancement>\n\t\t\t{\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@thief\",\n\t\t\t\t\tDescription = \"@thief_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_99\",\n\t\t\t\t\tSource = AdvancementSource.Quest\n\t\t\t\t},\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@ranger\",\n\t\t\t\t\tDescription = \"@ranger_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_101\",\n\t\t\t\t\tSource = AdvancementSource.Quest\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:126`
