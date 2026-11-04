# Scholar's Hat

The mark of a true intellectual, and a symbol of authority in wizarding cliques.

## Research effect

The mark of a true intellectual, and a symbol of authority in wizarding cliques.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | cotton_hat |
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
| [Scholar's Hat](item-cotton_hat.md) |

## Related recipe

| Recipe |
| --- |
| [Scholar's Hat](recipe-cotton_hat.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"tailor\"",
  "IconName": "\"Icons2_33\"",
  "CostTier": "7",
  "AdditionalRequirements": "new List<string> { \"embroidered_cotton\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Tailor.cs:61`
- `Assets.Source.Player/TechNode.cs:1`
