# Mage

An adventurer that has begun to unlock the magical secrets of the world.

## In the game

An adventurer that has begun to unlock the magical secrets of the world.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | mage |
| Item type | Adventurer |
| Resource Value | 2000 |
| Archetype | Mage |
| Power Stat | Magic |
| Power Multiplier | 1.25 |
| Source Training | true |

## Class advancement

Requirements are evaluated against the individual adventurer. Exact predicates are shown for conditional equipment requirements.

| Result | Where | Requirement |
| --- | --- | --- |
| Elementalist | Quest | See advancement implementation |
| Warlock | Quest | See advancement implementation |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_171\"",
  "ResourceValue": "2000L",
  "Archetype": "AdventurerArchetype.Mage",
  "PowerStat": "EquipStat.Magic",
  "PowerMultiplier": "1.25f",
  "SourceTraining": "true",
  "Advancements": "new List<AdventurerAdvancement>\n\t\t\t{\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@elementalist\",\n\t\t\t\t\tDescription = \"@elementalist_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_103\",\n\t\t\t\t\tSource = AdvancementSource.Quest\n\t\t\t\t},\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@warlock\",\n\t\t\t\t\tDescription = \"@warlock_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_105\",\n\t\t\t\t\tSource = AdvancementSource.Quest\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:152`
