# Clone Tool

Press [C] to select and copy parts of your workflow.

## Research effect

Press [C] to select and copy parts of your workflow.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | clone_tool |
| Type | Utility |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Node Duplication](tech-unlock_picker.md) |
| [Requisition Office](tech-requisition_office.md) |

## Leads to

| Research |
| --- |
| [Container Duplication](tech-container_clone.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"unlock_picker\"",
  "AdditionalRequirements": "new List<string> { \"requisition_office\" }",
  "CostTier": "2",
  "CostMultiplier": "2.0",
  "RelativePosition": "new Vector2Int(180, 0)",
  "IconName": "\"Icons_64\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tGameUI.Instance.UpdateBuildBarButtons();\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:226`
- `Assets.Source.Player/TechNode.cs:1`
