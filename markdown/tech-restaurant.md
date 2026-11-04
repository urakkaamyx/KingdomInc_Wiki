# Restaurant

A place to sell food to the inhabitants of Yensburg. Earn Crowns from the Gastronomer's Union for selling high-quality food.

## Research effect

A place to sell food to the inhabitants of Yensburg. Earn Crowns from the Gastronomer's Union for selling high-quality food.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | restaurant |
| Type | Flow Element |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Kitchen](tech-kitchen.md) |

## Leads to

| Research |
| --- |
| [Tactical Waitstaff](tech-restaurant_automation.md) |
| [Restaurant · second add-on slot](tech-restaurant_automation_2.md) |
| [Restaurant · third add-on slot](tech-restaurant_automation_3.md) |
| [Big Tippers](tech-restaurant_big_tippers.md) |
| [Royal Assent](tech-restaurant_crowns.md) |
| [Pantry](tech-pantry.md) |
| [Luxury Shop](tech-luxury_shop.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"kitchen\"",
  "RelativePosition": "new Vector2Int(630, 0)",
  "IconName": "\"Icons_185\"",
  "ForceRootNode": "true",
  "CostMultiplier": "4.0"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Kitchen.cs:45`
- `Assets.Source.Player/TechNode.cs:1`
