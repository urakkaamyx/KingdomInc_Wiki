# I'll Do It Myself

Items you craft by hand have a base productivity of +{0}.

## Effect

Items you craft by hand have a base productivity of +{0}.

## Ranks

Rank 0 contributes no bonus. Buying rank n costs n distilled nightmares; total cost to reach rank n from zero is n × (n + 1) / 2. The listed values feed into the system formulas described in the prestige guide.

| Rank | Bonus / modifier | Total nightmares spent |
| --- | --- | --- |
| 1 | 100% | 1 |
| 2 | 125% | 3 |
| 3 | 150% | 6 |
| 5 | 200% | 15 |
| 10 | 325% | 55 |

## Behavior hooks

This definition changes calc value. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_2\"",
  "Position": "new Vector2Int(-108, -297)",
  "CalcValue": "(int points) => 1f + 0.25f * (float)(points - 1)"
}
```

</details>

## Sources

- `Assets.Source.Player/PrestigeNode.cs:49`
