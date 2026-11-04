# Lithomancer

Lithomancer is a trait definition used by the game simulation.

## Behavior hooks

This definition changes get description, calc stat. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@lithomancer\"",
  "GetDescription": "(ActiveTrait trait) => Translation.TranslateOnly(\"@lithomancer_trait_desc_2\", GameMath.FormatPercentage(50f * trait.Quality))",
  "IconName": "\"Icons2_129\"",
  "CalcStat": "(ActiveTrait trait, EquipStat stat, float current) => (stat == EquipStat.Armor) ? (current + 50f * trait.Quality) : current"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:341`
