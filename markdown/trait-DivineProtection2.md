# Divine Protection

Protects the bearer from a single fatal attack.

## Effect

Protects the bearer from a single fatal attack.

## Behavior hooks

This definition changes calc damage taken. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@divine_protection\"",
  "Description": "\"@martyr_relic_trait\"",
  "IconName": "\"Icons3_78\"",
  "CalcDamageTaken": "(ActiveTrait trait, float current, object context) => _divineProtection(trait, current, context)"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:587`
