# Battlemaster

Battlemaster is a trait definition used by the game simulation.

## Behavior hooks

This definition changes get description, calc stat. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@battlemaster\"",
  "GetDescription": "(ActiveTrait trait) => Translation.TranslateOnly(\"@battlemaster_trait_desc\", GameMath.FormatPercentage(0.05f * trait.Quality))",
  "IconName": "\"Icons2_97\"",
  "CalcStat": "(ActiveTrait trait, EquipStat stat, float val) => (stat == EquipStat.CombatPower) ? (val * (1f + 0.05f * trait.Quality)) : val"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:138`
