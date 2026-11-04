# Survivalist

A ranger who has devoted themselves to the study of natural hazards, and how to defend against them.

## In the game

A ranger who has devoted themselves to the study of natural hazards, and how to defend against them.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | survivalist |
| Item type | Adventurer |
| Resource Value | 8000 |
| Archetype | Rogue |
| Power Stat | Dexterity |
| Power Multiplier | 2 |
| Override Recipe | cr_survivalist |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_126\"",
  "ResourceValue": "8000L",
  "Archetype": "AdventurerArchetype.Rogue",
  "PowerStat": "EquipStat.Dexterity",
  "PowerMultiplier": "2f",
  "OverrideRecipe": "\"cr_survivalist\"",
  "ClassTraits": "new List<AdventurerTrait>\n\t\t\t{\n\t\t\t\tAdventurerTrait.ClassRanger,\n\t\t\t\tAdventurerTrait.ClassSurvivalist\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:560`
