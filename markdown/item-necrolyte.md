# Necrolyte

A warlock with a keen interest in death and decay.

## In the game

A warlock with a keen interest in death and decay.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | necrolyte |
| Item type | Adventurer |
| Resource Value | 8000 |
| Archetype | Mage |
| Power Stat | Magic |
| Power Multiplier | 2 |
| Override Recipe | cr_necrolyte |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_132\"",
  "ResourceValue": "8000L",
  "Archetype": "AdventurerArchetype.Mage",
  "PowerStat": "EquipStat.Magic",
  "PowerMultiplier": "2f",
  "OverrideRecipe": "\"cr_necrolyte\"",
  "ClassTraits": "new List<AdventurerTrait>\n\t\t\t{\n\t\t\t\tAdventurerTrait.ClassWarlock,\n\t\t\t\tAdventurerTrait.ClassNecrolyte\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:602`
