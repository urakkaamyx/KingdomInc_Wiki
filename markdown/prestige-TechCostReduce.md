# Techno-wizard

Reduces Tech purchase cost by {0}.

## Effect

Reduces Tech purchase cost by {0}.

## Ranks

Rank 0 contributes no bonus. Buying rank n costs n distilled nightmares; total cost to reach rank n from zero is n × (n + 1) / 2. The listed values feed into the system formulas described in the prestige guide.

| Rank | Bonus / modifier | Total nightmares spent |
| --- | --- | --- |
| 1 | 50% | 1 |
| 2 | 55% | 3 |
| 3 | 60% | 6 |
| 5 | 70% | 15 |
| 10 | 95% | 55 |

## Behavior hooks

This definition changes calc value. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_4\"",
  "Position": "new Vector2Int(0, 316)",
  "CalcValue": "(int points) => 0.5f + 0.05f * (float)(points - 1)"
}
```

</details>

## Sources

- `Assets.Source.Player/PrestigeNode.cs:14`
