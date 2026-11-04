# Elementalist

Elementalist is a trait definition used by the game simulation.

## Behavior hooks

This definition changes get description, calc damage done. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@elementalist\"",
  "GetDescription": "(ActiveTrait trait) => Translation.TranslateOnly(\"@elementalist_trait_desc\", GameMath.FormatPercentage(0.05f * trait.Quality))",
  "IconName": "\"Icons2_103\"",
  "CalcDamageDone": "(ActiveTrait trait, float val, object context) => val * (1f + 0.05f * trait.Quality)"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:162`
