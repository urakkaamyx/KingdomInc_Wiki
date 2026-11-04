# Assassin

Assassin is a trait definition used by the game simulation.

## Behavior hooks

This definition changes get description, calc damage done. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@assassin\"",
  "GetDescription": "(ActiveTrait trait) => Translation.TranslateOnly(\"@assassin_trait_desc_2\", GameMath.FormatPercentage(0.03f * trait.Quality))",
  "IconName": "\"Icons2_119\"",
  "CalcDamageDone": "(ActiveTrait trait, float current, object context) => (context is DungeonProgress dungeonProgress && dungeonProgress.Stage.IsBoss) ? (current * (1f + 0.03f * trait.Quality)) : current"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:269`
