# Berserker

A battlemaster who has abandoned all reason in favor of full-on savage combat.

## In the game

A battlemaster who has abandoned all reason in favor of full-on savage combat.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | berserker |
| Item type | Adventurer |
| Resource Value | 8000 |
| Archetype | Fighter |
| Power Stat | Strength |
| Power Multiplier | 2 |
| Source Arena | true |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_116\"",
  "ResourceValue": "8000L",
  "Archetype": "AdventurerArchetype.Fighter",
  "PowerStat": "EquipStat.Strength",
  "PowerMultiplier": "2f",
  "SourceArena": "true",
  "ClassTraits": "new List<AdventurerTrait>\n\t\t\t{\n\t\t\t\tAdventurerTrait.ClassBattlemaster,\n\t\t\t\tAdventurerTrait.ClassBerserker\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:490`
