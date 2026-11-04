# Additional Workspace

Adds the ability to create and swap between multiple workspaces. Items can be transferred between workspaces using Armory-type nodes.

## Research effect

Adds the ability to create and swap between multiple workspaces. Items can be transferred between workspaces using Armory-type nodes.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | add_diagrams |
| Type | Utility |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Quest Board](tech-quest_board.md) |

## Leads to

| Research |
| --- |
| [Stacked Elements](tech-element_stacking.md) |
| [Filter](tech-filter.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"quest_board\"",
  "RelativePosition": "new Vector2Int(-315, 45)",
  "IconName": "\"Icons_161\"",
  "CostMultiplier": "5.0",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.Flows.Add(new FlowDiagram());\n\t\t\t\tGameUI.Instance.UpdateFlowMenu(isNew: true);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5QuestBoard.cs:67`
- `Assets.Source.Player/TechNode.cs:1`
