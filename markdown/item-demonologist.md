# Demonologist

A warlock who has devoted their time to the study of controlling demons.

## In the game

A warlock who has devoted their time to the study of controlling demons.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | demonologist |
| Item type | Adventurer |
| Resource Value | 8000 |
| Archetype | Mage |
| Power Stat | Magic |
| Power Multiplier | 2 |
| Override Recipe | cr_demonologist |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_134\"",
  "ResourceValue": "8000L",
  "Archetype": "AdventurerArchetype.Mage",
  "PowerStat": "EquipStat.Magic",
  "PowerMultiplier": "2f",
  "OverrideRecipe": "\"cr_demonologist\"",
  "ClassTraits": "new List<AdventurerTrait>\n\t\t\t{\n\t\t\t\tAdventurerTrait.ClassWarlock,\n\t\t\t\tAdventurerTrait.ClassDemonologist\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:616`
