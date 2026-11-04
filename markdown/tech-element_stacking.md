# Stacked Elements

Most Resource and Crafting elements can be stacked up to 5 high, to increase throughput without complicating your workflow. 

Control-click a supported element to stack a duplicate on top of it.

## Research effect

Most Resource and Crafting elements can be stacked up to 5 high, to increase throughput without complicating your workflow. 

Control-click a supported element to stack a duplicate on top of it.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | element_stacking |
| Type | Utility |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Additional Workspace](tech-add_diagrams.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"add_diagrams\"",
  "RelativePosition": "new Vector2Int(0, 180)",
  "IconName": "\"Icons_159\"",
  "CostMultiplier": "8.0"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5QuestBoard.cs:80`
- `Assets.Source.Player/TechNode.cs:1`
