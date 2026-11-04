# Greater Healing Potion

Greater Healing Potion is a trait definition used by the game simulation.

## Behavior hooks

This definition changes get description, war tick, quest tick, arena tick, dungeon healing tick. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@greater_healing_potion\"",
  "IconName": "\"Icons2_155\"",
  "GetDescription": "(ActiveTrait trait) => Translation.TranslateOnly(\"@healing_potion_effect\", 180f * trait.Quality)",
  "WarTick": "(ActiveTrait trait, WarProgress war) =>\n\t\t{\n\t\t\t_healingPotion(trait, 180f, war);\n\t\t}",
  "QuestTick": "(ActiveTrait trait, QuestProgress q) =>\n\t\t{\n\t\t\t_healingPotion(trait, 180f, q);\n\t\t}",
  "ArenaTick": "(ActiveTrait trait, Arena a) =>\n\t\t{\n\t\t\t_healingPotion(trait, 180f, a);\n\t\t}",
  "DungeonHealingTick": "(ActiveTrait trait, DungeonProgress d) =>\n\t\t{\n\t\t\t_healingPotion(trait, 180f, d);\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:451`
