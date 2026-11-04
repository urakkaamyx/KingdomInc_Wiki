# Fighter

An adventurer that focuses on brute strength and protection.

## In the game

An adventurer that focuses on brute strength and protection.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | fighter |
| Item type | Adventurer |
| Resource Value | 2000 |
| Archetype | Fighter |
| Power Stat | Strength |
| Power Multiplier | 1.25 |
| Source Training | true |

## Class advancement

Requirements are evaluated against the individual adventurer. Exact predicates are shown for conditional equipment requirements.

| Result | Where | Requirement |
| --- | --- | --- |
| Guardian | Quest | See advancement implementation |
| Battlemaster | Quest | See advancement implementation |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_170\"",
  "ResourceValue": "2000L",
  "Archetype": "AdventurerArchetype.Fighter",
  "PowerStat": "EquipStat.Strength",
  "PowerMultiplier": "1.25f",
  "SourceTraining": "true",
  "Advancements": "new List<AdventurerAdvancement>\n\t\t\t{\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@guardian\",\n\t\t\t\t\tDescription = \"@guardian_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_95\",\n\t\t\t\t\tSource = AdvancementSource.Quest\n\t\t\t\t},\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@battlemaster\",\n\t\t\t\t\tDescription = \"@battlemaster_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_97\",\n\t\t\t\t\tSource = AdvancementSource.Quest\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:100`
