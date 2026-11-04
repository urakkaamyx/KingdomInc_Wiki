# Area Move

Unlocks the ability to select, move and deconstruct any number of nodes at once.

## Research effect

Unlocks the ability to select, move and deconstruct any number of nodes at once.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | unlock_area_move |
| Type | Utility |
| Cost tier | 1 |

## Prerequisites

| Required research |
| --- |
| [Node Duplication](tech-unlock_picker.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"unlock_picker\"",
  "CostMultiplier": "2.0",
  "RelativePosition": "new Vector2Int(0, 180)",
  "IconName": "\"Icons_130\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tGameUI.Instance.UpdateBuildBarButtons();\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:240`
- `Assets.Source.Player/TechNode.cs:1`
