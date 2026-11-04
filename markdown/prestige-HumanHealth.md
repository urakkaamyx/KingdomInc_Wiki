# Heroes of Yensburg

Increases maximum health of all your human combatants by {0}.

## Effect

Increases maximum health of all your human combatants by {0}.

## Ranks

Rank 0 contributes no bonus. Buying rank n costs n distilled nightmares; total cost to reach rank n from zero is n × (n + 1) / 2. The listed values feed into the system formulas described in the prestige guide.

| Rank | Bonus / modifier | Total nightmares spent |
| --- | --- | --- |
| 1 | 5% | 1 |
| 2 | 10% | 3 |
| 3 | 15% | 6 |
| 5 | 25% | 15 |
| 10 | 50% | 55 |

## Behavior hooks

This definition changes calc value. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_151\"",
  "Position": "new Vector2Int(-311, 55)",
  "CalcValue": "(int points) => 0.05f * (float)points"
}
```

</details>

## Sources

- `Assets.Source.Player/PrestigeNode.cs:63`
