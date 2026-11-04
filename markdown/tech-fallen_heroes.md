# Fallen Heroes

Adds a new output to all War Effort nodes. Here, the remains of slain combatants are available to be transferred to a Graveyard (but will not block the War Effort if left unconnected).

## Research effect

Adds a new output to all War Effort nodes. Here, the remains of slain combatants are available to be transferred to a Graveyard (but will not block the War Effort if left unconnected).

## Research data

| Property | Value |
| --- | --- |
| Internal ID | fallen_heroes |
| Type | Utility |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Graveyard](tech-graveyard.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Root": "\"graveyard\"",
  "RelativePosition": "new Vector2Int(45, 225)",
  "CostCurrency": "CurrencyCollection.GoldFaith",
  "IconName": "\"Icons2_81\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Graveyard.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
