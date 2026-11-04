# Shaman

A ritualist who has devoted their life to the study of the natural elements.

## In the game

A ritualist who has devoted their life to the study of the natural elements.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | shaman |
| Item type | Adventurer |
| Resource Value | 8000 |
| Archetype | Cleric |
| Power Stat | Wisdom |
| Power Multiplier | 1.3 |
| Override Recipe | cr_shaman |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_136\"",
  "ResourceValue": "8000L",
  "Archetype": "AdventurerArchetype.Cleric",
  "PowerStat": "EquipStat.Wisdom",
  "PowerMultiplier": "1.3f",
  "OverrideRecipe": "\"cr_shaman\"",
  "ClassTraits": "new List<AdventurerTrait>\n\t\t\t{\n\t\t\t\tAdventurerTrait.ClassRitualist,\n\t\t\t\tAdventurerTrait.ClassShaman,\n\t\t\t\tAdventurerTrait.Healer\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:630`
