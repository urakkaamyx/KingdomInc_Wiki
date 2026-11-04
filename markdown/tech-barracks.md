# Barracks

Recruits Conscripts in service of the struggle against the many enemies that threaten Yensburg.

## Research effect

Recruits Conscripts in service of the struggle against the many enemies that threaten Yensburg.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | barracks |
| Type | Flow Element |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Carpenter](tech-carpenter.md) |

## Also grants research

| Unlocked automatically |
| --- |
| [Recruit Conscripts](tech-recruit_conscript.md) |

## Resource quota granted

| Resource | Amount |
| --- | --- |
| [Conscript](item-conscript.md) | 0.20000000298023224 |

## Leads to

| Research |
| --- |
| [Recruitment Officer](tech-barracks_automation.md) |
| [Barracks · second add-on slot](tech-barracks_automation_2.md) |
| [Barracks · overseers](tech-barracks_productivity.md) |
| [Barracks · artisans](tech-barracks_quality.md) |
| [Barracks · third add-on slot](tech-barracks_automation_3.md) |
| [Recruit Conscripts](tech-recruit_conscript.md) |
| [Outfitter](tech-outfitter.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"carpenter\"",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons_60\"",
  "CostTier": "3",
  "CostMultiplier": "8.0",
  "CostCurrency": "CurrencyCollection.GoldRequisition",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddResource(\"conscript\", 0.20000000298023224);\n\t\t\t\tply.AddTech(\"recruit_conscript\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3Barracks.cs:11`
- `Assets.Source.Player/TechNode.cs:1`
