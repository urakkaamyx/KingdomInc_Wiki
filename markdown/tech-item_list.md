# Item List View

Unlocks a list of all items that are available to you, as well as their associated sources and recipes.

## Research effect

Unlocks a list of all items that are available to you, as well as their associated sources and recipes.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | item_list |
| Type | Utility |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Requisition Office](tech-requisition_office.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"requisition_office\"",
  "RelativePosition": "new Vector2Int(315, -135)",
  "CostMultiplier": "3.0",
  "IconName": "\"Icons_164\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tif ((bool)GameUI.Instance)\n\t\t\t\t{\n\t\t\t\t\tGameUI.Instance.UpdateBuildBarButtons();\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:133`
- `Assets.Source.Player/TechNode.cs:1`
