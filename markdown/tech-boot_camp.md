# Boot Camp Heroics

Whenever a Conscript enters the Training Grounds for the first time there is a 10% chance of immediately gaining a medal.

## Research effect

Whenever a Conscript enters the Training Grounds for the first time there is a 10% chance of immediately gaining a medal.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | boot_camp |
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
  "RelativePosition": "new Vector2Int(405, 45)",
  "CostMultiplier": "4.0",
  "IconName": "\"Icons2_37\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:94`
- `Assets.Source.Player/TechNode.cs:1`
