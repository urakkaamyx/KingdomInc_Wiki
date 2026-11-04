# Pyromancer

An elementalist who has mastered the dangerous art of fire magic.

## In the game

An elementalist who has mastered the dangerous art of fire magic.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | pyromancer |
| Item type | Adventurer |
| Resource Value | 8000 |
| Archetype | Mage |
| Power Stat | Magic |
| Power Multiplier | 2 |
| Override Recipe | cr_pyromancer |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_128\"",
  "ResourceValue": "8000L",
  "Archetype": "AdventurerArchetype.Mage",
  "PowerStat": "EquipStat.Magic",
  "PowerMultiplier": "2f",
  "OverrideRecipe": "\"cr_pyromancer\"",
  "ClassTraits": "new List<AdventurerTrait>\n\t\t\t{\n\t\t\t\tAdventurerTrait.ClassElementalist,\n\t\t\t\tAdventurerTrait.ClassPyromancer\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:574`
