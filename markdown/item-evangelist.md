# Evangelist

A priest who has dedicated their life to spreading the message of Saint Ilonia.

## In the game

A priest who has dedicated their life to spreading the message of Saint Ilonia.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | evangelist |
| Item type | Adventurer |
| Resource Value | 8000 |
| Archetype | Cleric |
| Power Stat | Wisdom |
| Power Multiplier | 1.3 |
| Override Recipe | cr_evangelist |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_140\"",
  "ResourceValue": "8000L",
  "Archetype": "AdventurerArchetype.Cleric",
  "PowerStat": "EquipStat.Wisdom",
  "PowerMultiplier": "1.3f",
  "OverrideRecipe": "\"cr_evangelist\"",
  "ClassTraits": "new List<AdventurerTrait>\n\t\t\t{\n\t\t\t\tAdventurerTrait.ClassPriest,\n\t\t\t\tAdventurerTrait.ClassEvangelist,\n\t\t\t\tAdventurerTrait.Healer\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:660`
