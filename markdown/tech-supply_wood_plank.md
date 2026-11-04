# Supply Wood Plank

Provides a steady supply of Wood Plank from your Supply Depot.

## Research effect

Provides a steady supply of Wood Plank from your Supply Depot.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | supply_wood_plank |
| Type | Resource |
| Cost tier | 1 |

## Prerequisites

| Required research |
| --- |
| [Supply Depot](tech-supply_depot.md) |

## Resource quota granted

| Resource | Amount |
| --- | --- |
| [Softwood Plank](item-wood_plank.md) | 0.5 |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Resource",
  "Root": "\"supply_depot\"",
  "IconName": "\"Icons_14\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddResource(\"wood_plank\", 0.5);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1SupplyDepot.cs:23`
- `Assets.Source.Player/TechNode.cs:1`
