# Supply Linen Cloth

Provides a steady supply of Linen Cloth from your Supply Depot.

## Research effect

Provides a steady supply of Linen Cloth from your Supply Depot.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | supply_linen_cloth |
| Type | Resource |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Supply Depot](tech-supply_depot.md) |
| [Tailor](tech-tailor.md) |

## Resource quota granted

| Resource | Amount |
| --- | --- |
| [Linen Cloth](item-linen_cloth.md) | 0.5 |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Resource",
  "Root": "\"supply_depot\"",
  "IconName": "\"Icons_49\"",
  "CostTier": "2",
  "AdditionalRequirements": "new List<string> { \"tailor\" }",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddResource(\"linen_cloth\", 0.5);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1SupplyDepot.cs:33`
- `Assets.Source.Player/TechNode.cs:1`
