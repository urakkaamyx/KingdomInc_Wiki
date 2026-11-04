# Ranger

Ranger is a trait definition used by the game simulation.

## Behavior hooks

This definition changes get description, calc damage done. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@ranger\"",
  "GetDescription": "(ActiveTrait trait) => Translation.TranslateOnly(\"@ranger_trait_desc\", GameMath.FormatPercentage(0.1f * trait.Quality))",
  "IconName": "\"Icons2_101\"",
  "CalcDamageDone": "(ActiveTrait trait, float val, object context) => (trait.Self is HumanItemData humanItemData && humanItemData.HasWeaponType(WeaponType.Bow)) ? (val * (1f + 0.1f * trait.Quality)) : val"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:154`
