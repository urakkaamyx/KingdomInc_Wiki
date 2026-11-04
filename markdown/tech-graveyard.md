# Graveyard

Allows you to collect the remains of those who died fighting in your wars, and give them their eternal rest.

## Research effect

Allows you to collect the remains of those who died fighting in your wars, and give them their eternal rest.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | graveyard |
| Type | Flow Element |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Shrine](tech-shrine.md) |

## Also grants research

| Unlocked automatically |
| --- |
| [Simple Burial](tech-simple_burial.md) |
| [Fallen Heroes](tech-fallen_heroes.md) |

## Leads to

| Research |
| --- |
| [Coffin](tech-coffin.md) |
| [Gilded Coffin](tech-gilded_coffin.md) |
| [Relic of the Martyr](tech-martyr_relic.md) |
| [Fallen Heroes](tech-fallen_heroes.md) |
| [Simple Burial](tech-simple_burial.md) |
| [Officiated Burial](tech-officiated_burial.md) |
| [State Funeral](tech-state_funeral.md) |
| [Gravedigger](tech-graveyard_automation.md) |
| [Graveyard · second add-on slot](tech-graveyard_automation_2.md) |
| [Graveyard · overseers](tech-graveyard_productivity.md) |
| [Graveyard · artisans](tech-graveyard_quality.md) |
| [Graveyard · third add-on slot](tech-graveyard_automation_3.md) |
| [Necromancer](tech-necromancer.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"shrine\"",
  "RelativePosition": "new Vector2Int(-630, 0)",
  "IconName": "\"Icons2_43\"",
  "ForceRootNode": "true",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddTech(\"simple_burial\");\n\t\t\t\tply.AddTech(\"fallen_heroes\");\n\t\t\t\tforeach (WarEffort element in ply.GetElements<WarEffort>())\n\t\t\t\t{\n\t\t\t\t\telement.UpdateIO();\n\t\t\t\t\telement.World.UpdateIO();\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Graveyard.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
