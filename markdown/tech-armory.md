# Armory

A storage space for weapons and armor for a small fee. All armories are linked and contents can be accessed from anywhere.

## Research effect

A storage space for weapons and armor for a small fee. All armories are linked and contents can be accessed from anywhere.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | armory |
| Type | Flow Element |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Training Grounds](tech-training_grounds.md) |

## Leads to

| Research |
| --- |
| [Frugal Quartermaster](tech-armory_storage_cost.md) |
| [Extradimensional Storage Space](tech-armory_unlock_channels.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"training_grounds\"",
  "RelativePosition": "new Vector2Int(-450, 17)",
  "IconName": "\"Icons_138\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:102`
- `Assets.Source.Player/TechNode.cs:1`
