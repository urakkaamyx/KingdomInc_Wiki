# Resource Hoarder

Reduces the exponential cost increase of resource, forest, and farm upgrades by {0}.

## Effect

Reduces the exponential cost increase of resource, forest, and farm upgrades by {0}.

## Ranks

Rank 0 contributes no bonus. Buying rank n costs n distilled nightmares; total cost to reach rank n from zero is n × (n + 1) / 2. The listed values feed into the system formulas described in the prestige guide.

| Rank | Bonus / modifier | Total nightmares spent |
| --- | --- | --- |
| 1 | 5% | 1 |
| 2 | 7% | 3 |
| 3 | 9% | 6 |
| 5 | 13% | 15 |
| 10 | 23% | 55 |

## Behavior hooks

This definition changes calc value. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_16\"",
  "Position": "new Vector2Int(203, 242)",
  "CalcValue": "(int points) => 0.05f + 0.02f * (float)(points - 1)"
}
```

</details>

## Sources

- `Assets.Source.Player/PrestigeNode.cs:21`
