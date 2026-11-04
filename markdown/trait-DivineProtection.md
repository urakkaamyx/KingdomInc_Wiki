# Divine Protection

Protects the adventurer from a single fatal attack, and restores them to full health. The source of the protection is consumed once triggered.

## Effect

Protects the adventurer from a single fatal attack, and restores them to full health. The source of the protection is consumed once triggered.

## Behavior hooks

This definition changes calc damage taken. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@divine_protection\"",
  "Description": "\"@divine_protection_desc\"",
  "IconName": "\"Icons3_77\"",
  "CalcDamageTaken": "(ActiveTrait trait, float current, object context) => _divineProtection(trait, current, context)"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:579`
