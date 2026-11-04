# Offshore Tax Account

Reduces the Currency Exchange tax by {0}.

## Effect

Reduces the Currency Exchange tax by {0}.

## Ranks

Rank 0 contributes no bonus. Buying rank n costs n distilled nightmares; total cost to reach rank n from zero is n × (n + 1) / 2. The listed values feed into the system formulas described in the prestige guide.

| Rank | Bonus / modifier | Total nightmares spent |
| --- | --- | --- |
| 1 | 25% | 1 |
| 2 | 30% | 3 |
| 3 | 35% | 6 |
| 5 | 45% | 15 |
| 10 | 70% | 55 |

## Behavior hooks

This definition changes calc value. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_149\"",
  "Position": "new Vector2Int(311, 55)",
  "CalcValue": "(int points) => 0.25f + 0.05f * (float)(points - 1)"
}
```

</details>

## Sources

- `Assets.Source.Player/PrestigeNode.cs:28`
