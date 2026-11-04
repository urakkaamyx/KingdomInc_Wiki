# Paladin

A guardian that has devoted themselves to the service of the Divine.

## In the game

A guardian that has devoted themselves to the service of the Divine.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | paladin |
| Item type | Adventurer |
| Resource Value | 8000 |
| Archetype | Fighter |
| Power Stat | Strength |
| Power Multiplier | 2 |
| Override Recipe | cr_paladin |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_112\"",
  "ResourceValue": "8000L",
  "Archetype": "AdventurerArchetype.Fighter",
  "PowerStat": "EquipStat.Strength",
  "PowerMultiplier": "2f",
  "OverrideRecipe": "\"cr_paladin\"",
  "ClassTraits": "new List<AdventurerTrait>\n\t\t\t{\n\t\t\t\tAdventurerTrait.ClassGuardian,\n\t\t\t\tAdventurerTrait.ClassPaladin\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:462`
