# Scholar's Robe

A robe worn by seasoned mages and clerics. The delicate symbols woven into the fabric enhance the wearer's magic.

## Research effect

A robe worn by seasoned mages and clerics. The delicate symbols woven into the fabric enhance the wearer's magic.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | cotton_robe |
| Type | Recipe |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Tailor](tech-tailor.md) |
| [Embroidered Cotton](tech-embroidered_cotton.md) |

## Related item

| Item |
| --- |
| [Scholar's Robe](item-cotton_robe.md) |

## Related recipe

| Recipe |
| --- |
| [Scholar's Robe](recipe-cotton_robe.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"tailor\"",
  "IconName": "\"Icons2_32\"",
  "CostTier": "7",
  "AdditionalRequirements": "new List<string> { \"embroidered_cotton\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Tailor.cs:53`
- `Assets.Source.Player/TechNode.cs:1`
