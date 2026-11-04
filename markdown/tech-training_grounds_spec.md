# Specialized Training

Unlocks Specialization paths to allow your adventurers to hone their skills in a particular direction.

Right-click an adventurer or conscript in the Training Grounds (or any other supported node) to learn more about available Specializations.

## Research effect

Unlocks Specialization paths to allow your adventurers to hone their skills in a particular direction.

Right-click an adventurer or conscript in the Training Grounds (or any other supported node) to learn more about available Specializations.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | training_grounds_spec |
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
  "RelativePosition": "new Vector2Int(45, 315)",
  "CostMultiplier": "1.0",
  "IconName": "\"Icons3_86\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:35`
- `Assets.Source.Player/TechNode.cs:1`
