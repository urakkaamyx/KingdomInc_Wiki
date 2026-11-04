# Supply Network

Unlocks the Resources window, allowing you to purchase additional resource production capacity.

## Research effect

Unlocks the Resources window, allowing you to purchase additional resource production capacity.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | unlock_supply_window |
| Type | Utility |
| Cost tier | 1 |

## Prerequisites

| Required research |
| --- |
| [Supply Depot](tech-supply_depot.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"supply_depot\"",
  "RelativePosition": "new Vector2Int(405, -135)",
  "IconName": "\"Icons_16\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tGameUI.Instance.UpdateResourcesButton();\n\t\t\t\tTutorialUI.Instance?.ShowResourcesArrow(show: true);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1SupplyDepot.cs:58`
- `Assets.Source.Player/TechNode.cs:1`
