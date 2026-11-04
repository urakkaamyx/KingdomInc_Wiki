# Frugal Quartermaster

Reduces the cost of storing items in global storage nodes by 50%.

## Research effect

Reduces the cost of storing items in global storage nodes by 50%.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | armory_storage_cost |
| Type | Utility |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Armory](tech-armory.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"armory\"",
  "RelativePosition": "new Vector2Int(135, -242)",
  "CostMultiplier": "8.0",
  "IconName": "\"Icons_119\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:109`
- `Assets.Source.Player/TechNode.cs:1`
