# Inquisitor

A ritualist who has specialized in seeking out and destroying heresies of any kind.

## In the game

A ritualist who has specialized in seeking out and destroying heresies of any kind.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | inquisitor |
| Item type | Adventurer |
| Resource Value | 8000 |
| Archetype | Cleric |
| Power Stat | Wisdom |
| Power Multiplier | 1.3 |
| Source Arena | true |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_138\"",
  "ResourceValue": "8000L",
  "Archetype": "AdventurerArchetype.Cleric",
  "PowerStat": "EquipStat.Wisdom",
  "PowerMultiplier": "1.3f",
  "SourceArena": "true",
  "ClassTraits": "new List<AdventurerTrait>\n\t\t\t{\n\t\t\t\tAdventurerTrait.ClassRitualist,\n\t\t\t\tAdventurerTrait.ClassInquisitor,\n\t\t\t\tAdventurerTrait.MinorHealer\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:645`
