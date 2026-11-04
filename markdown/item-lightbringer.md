# Lightbringer

A priest who focuses on powerful single-target healing magic.

## In the game

A priest who focuses on powerful single-target healing magic.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | lightbringer |
| Item type | Adventurer |
| Resource Value | 8000 |
| Archetype | Cleric |
| Power Stat | Wisdom |
| Power Multiplier | 1.3 |
| Override Recipe | cr_lightbringer |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_142\"",
  "ResourceValue": "8000L",
  "Archetype": "AdventurerArchetype.Cleric",
  "PowerStat": "EquipStat.Wisdom",
  "PowerMultiplier": "1.3f",
  "OverrideRecipe": "\"cr_lightbringer\"",
  "ClassTraits": "new List<AdventurerTrait>\n\t\t\t{\n\t\t\t\tAdventurerTrait.ClassPriest,\n\t\t\t\tAdventurerTrait.ClassLightbringer,\n\t\t\t\tAdventurerTrait.Healer\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:675`
