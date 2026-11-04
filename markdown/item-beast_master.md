# Beast Master

A ranger who has befriended the animals of the forest and trains them for combat.

## In the game

A ranger who has befriended the animals of the forest and trains them for combat.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | beast_master |
| Item type | Adventurer |
| Resource Value | 8000 |
| Archetype | Rogue |
| Power Stat | Dexterity |
| Power Multiplier | 2 |
| Override Recipe | cr_beast_master |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_124\"",
  "ResourceValue": "8000L",
  "Archetype": "AdventurerArchetype.Rogue",
  "PowerStat": "EquipStat.Dexterity",
  "PowerMultiplier": "2f",
  "OverrideRecipe": "\"cr_beast_master\"",
  "ClassTraits": "new List<AdventurerTrait>\n\t\t\t{\n\t\t\t\tAdventurerTrait.ClassRanger,\n\t\t\t\tAdventurerTrait.ClassBeastMaster\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:546`
