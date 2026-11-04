# Campfire

Provides consistent heat to cook simple meals for your soldiers and adventurers.

## Research effect

Provides consistent heat to cook simple meals for your soldiers and adventurers.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | campfire |
| Type | Flow Element |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Forest](tech-forest.md) |

## Also grants research

| Unlocked automatically |
| --- |
| [Hardboiled Egg](tech-cooked_egg.md) |

## Leads to

| Research |
| --- |
| [Bring A Snack](tech-outfitter_2.md) |
| [Hardboiled Egg](tech-cooked_egg.md) |
| [Simple Salad](tech-salad.md) |
| [Seared Boar Steak](tech-boar_steak.md) |
| [Mushroom Stew](tech-mushroom_stew.md) |
| [Feeding the Wildlife](tech-cr_beast_master.md) |
| [Wilderness Cookery](tech-campfire_automation.md) |
| [Campfire · second add-on slot](tech-campfire_automation_2.md) |
| [Campfire · overseers](tech-campfire_productivity.md) |
| [Campfire · artisans](tech-campfire_quality.md) |
| [Campfire · third add-on slot](tech-campfire_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"forest\"",
  "RelativePosition": "new Vector2Int(-630, 0)",
  "IconName": "\"Icons_76\"",
  "ForceRootNode": "true",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddTech(\"cooked_egg\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T4Campfire.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
