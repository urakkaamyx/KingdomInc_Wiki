# Reaver

Reaver is a trait definition used by the game simulation.

## Behavior hooks

This definition changes get description, calc damage done. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@reaver\"",
  "GetDescription": "(ActiveTrait trait) => Translation.TranslateOnly(\"@reaver_trait_desc\", GameMath.FormatPercentage(0.1f * trait.Quality))",
  "IconName": "\"Icons2_117\"",
  "CalcDamageDone": "(ActiveTrait trait, float current, object context) => ((HumanItemData)trait.Self).HasDualWield ? (current * (1f + 0.1f * trait.Quality)) : current"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:247`
