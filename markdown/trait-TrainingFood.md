# Rations

Rations is a trait definition used by the game simulation.

## Behavior hooks

This definition changes get description, calc training. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@rations\"",
  "GetDescription": "(ActiveTrait trait) => Translation.TranslateOnly(\"@rations_effect\", GameMath.FormatPercentage(0.25f * trait.Quality))",
  "IconName": "\"Icons_220\"",
  "CalcTraining": "(ActiveTrait trait, float added, object context) => added * (1f + 0.25f * trait.Quality)"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:499`
