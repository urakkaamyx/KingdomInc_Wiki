# Supply Rough Leather

Provides a steady supply of Rough Leather from your Supply Depot.

## Research effect

Provides a steady supply of Rough Leather from your Supply Depot.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | supply_rough_leather |
| Type | Resource |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Supply Depot](tech-supply_depot.md) |
| [Leatherworker](tech-leatherworker.md) |

## Resource quota granted

| Resource | Amount |
| --- | --- |
| [Rough Leather](item-rough_leather.md) | 0.5 |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Resource",
  "Root": "\"supply_depot\"",
  "IconName": "\"Icons_45\"",
  "CostTier": "2",
  "AdditionalRequirements": "new List<string> { \"leatherworker\" }",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddResource(\"rough_leather\", 0.5);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1SupplyDepot.cs:45`
- `Assets.Source.Player/TechNode.cs:1`
