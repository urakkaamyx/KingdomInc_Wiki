# Lightbringer

Lightbringer is a trait definition used by the game simulation.

## Behavior hooks

This definition changes get description, calc healing taken. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@lightbringer\"",
  "GetDescription": "(ActiveTrait trait) => Translation.TranslateOnly(\"@lightbringer_trait_desc_2\", GameMath.FormatPercentage(0.1f * trait.Quality))",
  "IconName": "\"Icons2_141\"",
  "CalcHealingTaken": "(ActiveTrait trait, float current, object context) => (context is DungeonProgress dungeonProgress && dungeonProgress.Stage.IsBoss) ? (current * (1f + 0.1f * trait.Quality)) : current"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:416`
