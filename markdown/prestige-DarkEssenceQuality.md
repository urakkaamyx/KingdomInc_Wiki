# Darkest Essence

The Imbue Dark Essence enchantment grants an additional +{0} quality.

## Effect

The Imbue Dark Essence enchantment grants an additional +{0} quality.

## Ranks

Rank 0 contributes no bonus. Buying rank n costs n distilled nightmares; total cost to reach rank n from zero is n × (n + 1) / 2. The listed values feed into the system formulas described in the prestige guide.

| Rank | Bonus / modifier | Total nightmares spent |
| --- | --- | --- |
| 1 | 10% | 1 |
| 2 | 15% | 3 |
| 3 | 20% | 6 |
| 5 | 30% | 15 |
| 10 | 55% | 55 |

## Behavior hooks

This definition changes calc value. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_221\"",
  "Position": "new Vector2Int(-274, -158)",
  "CalcValue": "(int points) => 0.1f + 0.05f * (float)(points - 1)"
}
```

</details>

## Sources

- `Assets.Source.Player/PrestigeNode.cs:56`
