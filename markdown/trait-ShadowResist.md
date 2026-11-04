# Shadow Resistance

Shadow Resistance is a trait definition used by the game simulation.

## Behavior hooks

This definition changes get description. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@shadow_resist\"",
  "GetDescription": "(ActiveTrait trait) => Translation.TranslateOnly(\"@shadow_resist_desc\", GameMath.FormatPercentage(Resist(trait.Quality)))",
  "IconName": "\"Icons2_169\""
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:514`
