# Critical Hit

Critical Hit is a trait definition used by the game simulation.

## Behavior hooks

This definition changes get description, calc damage done. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@crit_chance\"",
  "GetDescription": "(ActiveTrait trait) => Translation.TranslateOnly(\"@crit_chance_desc\", GameMath.FormatPercentage(0.05f * trait.Quality, FormatPercentageMode.Default, 1))",
  "IconName": "\"Icons2_181\"",
  "CalcDamageDone": "(ActiveTrait trait, float current, object context) => SeededRandom.Global.RandomBool(0.05f * trait.Quality) ? (current * 2f) : current"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:528`
