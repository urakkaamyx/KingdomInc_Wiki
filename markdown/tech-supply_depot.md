# Supply Depot

Supplies a variety of raw materials in small quantities.

## Research effect

Supplies a variety of raw materials in small quantities.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | supply_depot |
| Type | Flow Element |
| Cost tier | 1 |

## Prerequisites

| Required research |
| --- |
| [Blacksmith](tech-blacksmith.md) |
| [Drudge Miners](tech-mine_automation.md) |

## Also grants research

| Unlocked automatically |
| --- |
| [Supply Wood Plank](tech-supply_wood_plank.md) |

## Leads to

| Research |
| --- |
| [Iron Sword](tech-iron_sword.md) |
| [Iron Dagger](tech-iron_dagger.md) |
| [Supply Wood Plank](tech-supply_wood_plank.md) |
| [Supply Linen Cloth](tech-supply_linen_cloth.md) |
| [Supply Rough Leather](tech-supply_rough_leather.md) |
| [Crate Carriers](tech-supply_depot_automation.md) |
| [Supply Depot · second add-on slot](tech-supply_depot_automation_2.md) |
| [Supply Depot · overseers](tech-supply_depot_productivity.md) |
| [Supply Depot · artisans](tech-supply_depot_quality.md) |
| [Supply Depot · third add-on slot](tech-supply_depot_automation_3.md) |
| [Supply Network](tech-unlock_supply_window.md) |
| [Distributor](tech-distributor.md) |
| [Requisition Office](tech-requisition_office.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"blacksmith\"",
  "AdditionalRequirements": "new List<string> { \"mine_automation\" }",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons_16\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddTech(\"supply_wood_plank\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1SupplyDepot.cs:11`
- `Assets.Source.Player/TechNode.cs:1`
