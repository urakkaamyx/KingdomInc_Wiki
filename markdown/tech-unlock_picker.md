# Node Duplication

[Q] or [Middle-click] to copy a node and all of its settings.

## Research effect

[Q] or [Middle-click] to copy a node and all of its settings.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | unlock_picker |
| Type | Utility |
| Cost tier | 1 |

## Prerequisites

| Required research |
| --- |
| [Blacksmith](tech-blacksmith.md) |

## Leads to

| Research |
| --- |
| [Clone Tool](tech-clone_tool.md) |
| [Area Move](tech-unlock_area_move.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"blacksmith\"",
  "CostMultiplier": "2.0",
  "RelativePosition": "new Vector2Int(405, -45)",
  "IconName": "\"Icons_64\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:218`
- `Assets.Source.Player/TechNode.cs:1`
