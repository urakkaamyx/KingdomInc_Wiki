# Priest

Priest is a trait definition used by the game simulation.

## Behavior hooks

This definition changes get description, calc healing done. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@priest\"",
  "GetDescription": "(ActiveTrait trait) => Translation.TranslateOnly(\"@priest_trait_desc\", GameMath.FormatPercentage(0.1f * trait.Quality))",
  "IconName": "\"Icons2_109\"",
  "CalcHealingDone": "(ActiveTrait trait, float val, object target) => val * (1f + 0.1f * trait.Quality)"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:197`
