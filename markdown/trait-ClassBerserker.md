# Berserker

Berserker is a trait definition used by the game simulation.

## Behavior hooks

This definition changes get description, calc damage done. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@berserker\"",
  "GetDescription": "(ActiveTrait trait) => Translation.TranslateOnly(\"@berserker_trait_desc\", GameMath.FormatPercentage(0.2f * trait.Quality))",
  "IconName": "\"Icons2_115\"",
  "CalcDamageDone": "(ActiveTrait trait, float current, object context) => (!((HumanItemData)trait.Self).HasArmorType(ArmorType.Heavy)) ? (current * (1f + 0.2f * trait.Quality)) : current"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:239`
