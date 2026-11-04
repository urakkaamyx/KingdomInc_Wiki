# Tank

Reduces damage taken by 25%, and enemies are more likely to target this adventurer in group encounters.

## Effect

Reduces damage taken by 25%, and enemies are more likely to target this adventurer in group encounters.

## Behavior hooks

This definition changes calc damage taken. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@trait_tank\"",
  "Description": "\"@trait_tank_desc\"",
  "IconName": "\"Icons_174\"",
  "CalcDamageTaken": "(ActiveTrait data, float dmg, object context) => dmg * 0.75f"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:94`
