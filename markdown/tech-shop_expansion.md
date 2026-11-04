# Future Proofing

Increases gold accumulation limit to 5 gold.

## Research effect

Increases gold accumulation limit to 5 gold.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | shop_expansion |
| Type | Utility |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Item Shop](tech-shop.md) |
| [Enchanter](tech-enchanter.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Root": "\"shop\"",
  "RelativePosition": "new Vector2Int(45, 225)",
  "CostTier": "7",
  "AdditionalRequirements": "new List<string> { \"enchanter\" }",
  "IconName": "\"Icons2_193\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tforeach (Shop element in ply.GetElements<Shop>())\n\t\t\t\t{\n\t\t\t\t\telement.UpdateUpgrades();\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Shop.cs:20`
- `Assets.Source.Player/TechNode.cs:1`
