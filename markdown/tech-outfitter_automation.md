# Self Service

Outfitters no longer require your input to function.

## Research effect

Outfitters no longer require your input to function.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | outfitter_automation |
| Type | Utility |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Outfitter](tech-outfitter.md) |

## Leads to

| Research |
| --- |
| [No Waiting Around](tech-outfitter_timeout.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"outfitter\"",
  "RelativePosition": "new Vector2Int(-225, -154)",
  "IconName": "\"Icons_98\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tforeach (Outfitter element in ply.GetElements<Outfitter>())\n\t\t\t\t{\n\t\t\t\t\telement.CheckAutomated();\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3Barracks.cs:41`
- `Assets.Source.Player/TechNode.cs:1`
