# Warlock

Warlock is a trait definition used by the game simulation.

## Behavior hooks

This definition changes get description, apply group buffs. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@warlock\"",
  "GetDescription": "(ActiveTrait trait) => Translation.TranslateOnly(\"@warlock_trait_desc\", GameMath.FormatPercentage(0.1f * trait.Quality))",
  "IconName": "\"Icons2_105\"",
  "ApplyGroupBuffs": "(ActiveTrait trait, CombatantItemData ally, object context) =>\n\t\t{\n\t\t\tally.ApplyBuff(_classWarlockBuff, trait.Quality);\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:178`
