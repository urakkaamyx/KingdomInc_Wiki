# Minor Healing

Some proficiency in healing magic, but not enough to serve as a party's main healer.

## Effect

Some proficiency in healing magic, but not enough to serve as a party's main healer.

## Behavior hooks

This definition changes dungeon healing tick, war tick. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@trait_minor_healer\"",
  "Description": "\"@trait_minor_healer_desc\"",
  "IconName": "\"Icons3_94\"",
  "DungeonHealingTick": "(ActiveTrait trait, DungeonProgress dp) =>\n\t\t{\n\t\t\tif (!SeededRandom.Global.RandomBool())\n\t\t\t{\n\t\t\t\tCombatantItemData healingTarget = dp.GetHealingTarget(trait.Self);\n\t\t\t\thealingTarget?.Heal(trait.Self.GetBaseHealing(healingTarget) / 25, dp);\n\t\t\t}\n\t\t}",
  "WarTick": "(ActiveTrait trait, WarProgress war) =>\n\t\t{\n\t\t\tif (!SeededRandom.Global.RandomBool())\n\t\t\t{\n\t\t\t\tCombatantItemData healingTarget = war.GetHealingTarget(trait.Self);\n\t\t\t\thealingTarget?.Heal(trait.Self.GetBaseHealing(healingTarget) / 25, war);\n\t\t\t}\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:71`
