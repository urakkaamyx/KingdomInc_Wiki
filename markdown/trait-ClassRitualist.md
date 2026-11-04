# Ritualist

Ritualist is a trait definition used by the game simulation.

## Behavior hooks

This definition changes get description, calc damage done. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@ritualist\"",
  "GetDescription": "(ActiveTrait trait) => Translation.TranslateOnly(\"@ritualist_trait_desc\", GameMath.FormatPercentage(0.2f * trait.Quality))",
  "IconName": "\"Icons2_107\"",
  "CalcDamageDone": "(ActiveTrait trait, float val, object target) => val * (1f + 0.2f * trait.Quality)"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:189`
