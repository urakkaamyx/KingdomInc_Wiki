# Assassin

A thief who has deepened their knowledge of unfair tactics and unseen strikes.

## In the game

A thief who has deepened their knowledge of unfair tactics and unseen strikes.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | assassin |
| Item type | Adventurer |
| Resource Value | 8000 |
| Archetype | Rogue |
| Power Stat | Dexterity |
| Power Multiplier | 2 |
| Override Recipe | cr_assassin |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_120\"",
  "ResourceValue": "8000L",
  "Archetype": "AdventurerArchetype.Rogue",
  "PowerStat": "EquipStat.Dexterity",
  "PowerMultiplier": "2f",
  "OverrideRecipe": "\"cr_assassin\"",
  "ClassTraits": "new List<AdventurerTrait>\n\t\t\t{\n\t\t\t\tAdventurerTrait.ClassThief,\n\t\t\t\tAdventurerTrait.ClassAssassin\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:518`
