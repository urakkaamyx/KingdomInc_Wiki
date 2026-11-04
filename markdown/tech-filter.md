# Filter

Sorts incoming items by type to disentangle mixed inputs.

## Research effect

Sorts incoming items by type to disentangle mixed inputs.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | filter |
| Type | Flow Element |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Additional Workspace](tech-add_diagrams.md) |

## Leads to

| Research |
| --- |
| [Appraiser](tech-appraiser.md) |
| [Accountant](tech-accountant.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"add_diagrams\"",
  "RelativePosition": "new Vector2Int(-225, 28)",
  "IconName": "\"Icons_150\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5QuestBoard.cs:88`
- `Assets.Source.Player/TechNode.cs:1`
