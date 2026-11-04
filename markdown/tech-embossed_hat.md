# Embossed Mask

Serves to obscure the wearer's identity and improve their lethality at the same time.

## Research effect

Serves to obscure the wearer's identity and improve their lethality at the same time.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | embossed_hat |
| Type | Recipe |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Leatherworker](tech-leatherworker.md) |
| [Embossed Leather](tech-embossed_leather.md) |

## Related item

| Item |
| --- |
| [Embossed Mask](item-embossed_hat.md) |

## Related recipe

| Recipe |
| --- |
| [Embossed Mask](recipe-embossed_hat.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"leatherworker\"",
  "IconName": "\"Icons2_35\"",
  "CostTier": "7",
  "AdditionalRequirements": "new List<string> { \"embossed_leather\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Leatherworker.cs:62`
- `Assets.Source.Player/TechNode.cs:1`
