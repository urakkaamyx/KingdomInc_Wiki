# Fire Resistance

Fire Resistance is a trait definition used by the game simulation.

## Behavior hooks

This definition changes get description. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@fire_resist\"",
  "GetDescription": "(ActiveTrait trait) => Translation.TranslateOnly(\"@fire_resist_desc\", GameMath.FormatPercentage(Resist(trait.Quality)))",
  "IconName": "\"Icons2_145\""
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:507`
