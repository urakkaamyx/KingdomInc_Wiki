# Cleric

An adventurer that has devoted themselves to the greater powers above.

## In the game

An adventurer that has devoted themselves to the greater powers above.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | cleric |
| Item type | Adventurer |
| Resource Value | 2000 |
| Archetype | Cleric |
| Power Stat | Wisdom |
| Power Multiplier | 0.75 |
| Source Training | true |

## Class advancement

Requirements are evaluated against the individual adventurer. Exact predicates are shown for conditional equipment requirements.

| Result | Where | Requirement |
| --- | --- | --- |
| Ritualist | Quest | See advancement implementation |
| Priest | Quest | See advancement implementation |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_172\"",
  "ResourceValue": "2000L",
  "Archetype": "AdventurerArchetype.Cleric",
  "PowerStat": "EquipStat.Wisdom",
  "PowerMultiplier": "0.75f",
  "SourceTraining": "true",
  "ClassTraits": "new List<AdventurerTrait> { AdventurerTrait.Healer }",
  "Advancements": "new List<AdventurerAdvancement>\n\t\t\t{\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@ritualist\",\n\t\t\t\t\tDescription = \"@ritualist_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_107\",\n\t\t\t\t\tSource = AdvancementSource.Quest\n\t\t\t\t},\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@priest\",\n\t\t\t\t\tDescription = \"@priest_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_109\",\n\t\t\t\t\tSource = AdvancementSource.Quest\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:178`
