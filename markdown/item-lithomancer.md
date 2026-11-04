# Lithomancer

An elementalist who has mastered control over rock and stone.

## In the game

An elementalist who has mastered control over rock and stone.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | lithomancer |
| Item type | Adventurer |
| Resource Value | 8000 |
| Archetype | Mage |
| Power Stat | Magic |
| Power Multiplier | 2 |
| Override Recipe | cr_lithomancer |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_130\"",
  "ResourceValue": "8000L",
  "Archetype": "AdventurerArchetype.Mage",
  "PowerStat": "EquipStat.Magic",
  "PowerMultiplier": "2f",
  "OverrideRecipe": "\"cr_lithomancer\"",
  "ClassTraits": "new List<AdventurerTrait>\n\t\t\t{\n\t\t\t\tAdventurerTrait.ClassElementalist,\n\t\t\t\tAdventurerTrait.ClassLithomancer\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:588`
