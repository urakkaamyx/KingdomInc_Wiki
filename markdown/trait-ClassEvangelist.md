# Evangelist

Uses group healing magic while in a dungeon.

## Effect

Uses group healing magic while in a dungeon.

## Behavior hooks

This definition changes dungeon healing tick. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@evangelist\"",
  "Description": "\"@evangelist_trait_desc\"",
  "IconName": "\"Icons2_139\"",
  "DungeonHealingTick": "(ActiveTrait trait, DungeonProgress dp) =>\n\t\t{\n\t\t\tif (SeededRandom.Global.RandomBool(0.667f))\n\t\t\t{\n\t\t\t\treturn;\n\t\t\t}\n\t\t\tforeach (CombatantItemData combatant in dp.Combatants)\n\t\t\t{\n\t\t\t\tcombatant.Heal(trait.Self.GetBaseHealing(combatant) / 40, dp);\n\t\t\t}\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:384`
