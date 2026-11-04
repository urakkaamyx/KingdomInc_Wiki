# Build Menu Search

Adds a search field to the Build Menu, to search for available nodes by name.

## Research effect

Adds a search field to the Build Menu, to search for available nodes by name.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | buy_menu_search |
| Type | Utility |
| Cost tier | 4 |
| Visibility | Hidden by code |

## Prerequisites

| Required research |
| --- |
| [Manifold](tech-manifold.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"manifold\"",
  "Hidden": "(GamePlayer ply) => true",
  "RelativePosition": "new Vector2Int(-45, 207)",
  "IconName": "\"Icons_37\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T4Forest.cs:179`
- `Assets.Source.Player/TechNode.cs:1`
