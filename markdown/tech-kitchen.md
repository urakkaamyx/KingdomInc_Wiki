# Kitchen

Prepares high-quality food for your army, your adventurers, and the wealthy elite of the city.

## Research effect

Prepares high-quality food for your army, your adventurers, and the wealthy elite of the city.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | kitchen |
| Type | Flow Element |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Farm](tech-farm.md) |

## Leads to

| Research |
| --- |
| [Harvest Wild Onion](tech-forest_wild_onion.md) |
| [Sous Chef](tech-kitchen_automation.md) |
| [Kitchen · second add-on slot](tech-kitchen_automation_2.md) |
| [Kitchen · overseers](tech-kitchen_productivity.md) |
| [Kitchen · artisans](tech-kitchen_quality.md) |
| [Kitchen · third add-on slot](tech-kitchen_automation_3.md) |
| [Hamburger](tech-hamburger.md) |
| [Salamander Skewer](tech-salamander_skewer.md) |
| [Stalker Stew](tech-stalker_stew.md) |
| [Restaurant](tech-restaurant.md) |
| [Butcher](tech-butcher.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"farm\"",
  "RelativePosition": "new Vector2Int(630, 0)",
  "IconName": "\"Icons_184\"",
  "ForceRootNode": "true",
  "CostMultiplier": "4.0"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Kitchen.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
