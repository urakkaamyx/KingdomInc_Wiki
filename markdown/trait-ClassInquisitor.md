# Inquisitor

Inquisitor is a trait definition used by the game simulation.

## Behavior hooks

This definition changes get description, calc stat. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@inquisitor\"",
  "GetDescription": "(ActiveTrait trait) => Translation.TranslateOnly(\"@inquisitor_trait_desc\", (float)trait.Self.GetStat(EquipStat.Strength) * 0.5f * trait.Quality)",
  "IconName": "\"Icons2_137\"",
  "CalcStat": "(ActiveTrait trait, EquipStat stat, float current) => (stat == EquipStat.CombatPower) ? (current + (float)trait.Self.GetStat(EquipStat.Strength) * 0.5f * trait.Quality) : current"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:376`
