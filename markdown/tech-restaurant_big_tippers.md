# Big Tippers

Unlocks a new Upgrade for your Restaurant.

Increases Gold income by up to 50% if supplied food is above 120% quality.

## Research effect

Unlocks a new Upgrade for your Restaurant.

Increases Gold income by up to 50% if supplied food is above 120% quality.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | restaurant_big_tippers |
| Type | Upgrade Slot |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Restaurant](tech-restaurant.md) |
| [Tactical Waitstaff](tech-restaurant_automation.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.UpgradeSlot",
  "Previous": "\"restaurant_automation\"",
  "RelativePosition": "new Vector2Int(0, 180)",
  "IconName": "\"Icons_119\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddAvailableFlowUpgrade(\"Restaurant\", \"RestaurantBigTippers\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Kitchen.cs:57`
- `Assets.Source.Player/TechNode.cs:1`
