# Workout Snack

Entering the Training Grounds with food equipped will consume the food, but reduces energy consumption and training time by 50%.

## Research effect

Entering the Training Grounds with food equipped will consume the food, but reduces energy consumption and training time by 50%.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | training_grounds_food |
| Type | Utility |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Training Grounds](tech-training_grounds.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Root": "\"training_grounds\"",
  "RelativePosition": "new Vector2Int(225, 225)",
  "CostMultiplier": "6.0",
  "IconName": "\"Icons_193\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:27`
- `Assets.Source.Player/TechNode.cs:1`
