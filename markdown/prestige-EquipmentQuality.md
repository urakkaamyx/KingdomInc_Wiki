# Mark of Quality

Increases the base quality of crafted equipment by {0}.

## Effect

Increases the base quality of crafted equipment by {0}.

## Ranks

Rank 0 contributes no bonus. Buying rank n costs n distilled nightmares; total cost to reach rank n from zero is n × (n + 1) / 2. The listed values feed into the system formulas described in the prestige guide.

| Rank | Bonus / modifier | Total nightmares spent |
| --- | --- | --- |
| 1 | 2% | 1 |
| 2 | 4% | 3 |
| 3 | 6% | 6 |
| 5 | 10% | 15 |
| 10 | 20% | 55 |

## Behavior hooks

This definition changes calc value. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_91\"",
  "Position": "new Vector2Int(274, -158)",
  "CalcValue": "(int points) => 0.02f * (float)points"
}
```

</details>

## Sources

- `Assets.Source.Player/PrestigeNode.cs:35`
