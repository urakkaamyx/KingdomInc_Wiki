# Paladin

Casts a weak healing spell on low-health party members while in a dungeon. Healing scales based on Wisdom.

## Effect

Casts a weak healing spell on low-health party members while in a dungeon. Healing scales based on Wisdom.

## Behavior hooks

This definition changes dungeon healing tick. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@paladin\"",
  "Description": "\"@paladin_trait_desc\"",
  "IconName": "\"Icons2_111\"",
  "DungeonHealingTick": "(ActiveTrait trait, DungeonProgress dp) =>\n\t\t{\n\t\t\tif (!SeededRandom.Global.RandomBool())\n\t\t\t{\n\t\t\t\tCombatantItemData healingTarget = dp.GetHealingTarget(trait.Self);\n\t\t\t\thealingTarget?.Heal(trait.Self.GetBaseHealing(healingTarget) / 20, dp);\n\t\t\t}\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:205`
