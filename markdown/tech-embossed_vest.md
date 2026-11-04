# Embossed Vest

The innate enchantments on this vest serve to increase the wearer's freedom of movement.

## Research effect

The innate enchantments on this vest serve to increase the wearer's freedom of movement.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | embossed_vest |
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
| [Embossed Vest](item-embossed_vest.md) |

## Related recipe

| Recipe |
| --- |
| [Embossed Vest](recipe-embossed_vest.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"leatherworker\"",
  "IconName": "\"Icons2_34\"",
  "CostTier": "7",
  "AdditionalRequirements": "new List<string> { \"embossed_leather\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Leatherworker.cs:54`
- `Assets.Source.Player/TechNode.cs:1`
