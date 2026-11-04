# Inn

Allows your citizens a moment of rest, restoring their health to full over time. Also serves as a minor source of income.

## Research effect

Allows your citizens a moment of rest, restoring their health to full over time. Also serves as a minor source of income.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | inn |
| Type | Flow Element |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Quest Board](tech-quest_board.md) |

## Leads to

| Research |
| --- |
| [Bed and Breakfast](tech-inn_add_food.md) |
| [Enchanter](tech-enchanter.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"quest_board\"",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons_154\"",
  "ForceRootNode": "true",
  "CostTier": "6",
  "CostMultiplier": "4.0"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T6Inn.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
