# Carpenter

Crafts wooden weapons and intermediate components.

## Research effect

Crafts wooden weapons and intermediate components.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | carpenter |
| Type | Flow Element |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Tailor](tech-tailor.md) |

## Also grants research

| Unlocked automatically |
| --- |
| [Simple Wooden Shield](tech-simple_wooden_shield.md) |

## Leads to

| Research |
| --- |
| [Softwood Bow](tech-softwood_bow.md) |
| [Initiate's Staff](tech-initiate_staff.md) |
| [Softwood Warstaff](tech-softwood_warstaff.md) |
| [Simple Wooden Shield](tech-simple_wooden_shield.md) |
| [Reinforced Wooden Shield](tech-reinforced_wooden_shield.md) |
| [Softwood Plank](tech-wood_plank.md) |
| [Staff of the Wild](tech-wild_staff.md) |
| [Ancient Wood Plank](tech-ancient_wood_plank.md) |
| [Ancient Wood Staff](tech-ancient_wood_staff.md) |
| [Ancient Wood Longbow](tech-ancient_wood_bow.md) |
| [Bulwark of Ancients](tech-ancient_shield.md) |
| [Crystalline Staff](tech-ancient_int_staff.md) |
| [Staff of Sages](tech-ancient_wis_staff.md) |
| [Trueshot Bow](tech-trueshot_bow.md) |
| [Petrified Shield](tech-petrified_shield.md) |
| [Archmage's Staff](tech-archmage_staff.md) |
| [Archbishop's Staff](tech-archbishop_staff.md) |
| [Coffin](tech-coffin.md) |
| [Only Hammers](tech-carpenter_automation.md) |
| [Carpenter · second add-on slot](tech-carpenter_automation_2.md) |
| [Carpenter · overseers](tech-carpenter_productivity.md) |
| [Carpenter · artisans](tech-carpenter_quality.md) |
| [Carpenter · third add-on slot](tech-carpenter_automation_3.md) |
| [Barracks](tech-barracks.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"tailor\"",
  "RelativePosition": "new Vector2Int(-630, 0)",
  "IconName": "\"Icons_40\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddTech(\"simple_wooden_shield\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Carpenter.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
