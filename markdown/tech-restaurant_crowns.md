# Royal Assent

Unlocks a new Upgrade for your Restaurant.

Increases the number of Crowns collected by 10%.

## Research effect

Unlocks a new Upgrade for your Restaurant.

Increases the number of Crowns collected by 10%.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | restaurant_crowns |
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
  "RelativePosition": "new Vector2Int(0, -180)",
  "IconName": "\"Icons_188\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddAvailableFlowUpgrade(\"Restaurant\", \"RestaurantCrowns\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Kitchen.cs:68`
- `Assets.Source.Player/TechNode.cs:1`
