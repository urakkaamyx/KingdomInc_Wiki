# Embossed Leather

Patterned with arcane symbols and suitable for the creation of powerful equipment.

## Research effect

Patterned with arcane symbols and suitable for the creation of powerful equipment.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | embossed_leather |
| Type | Recipe |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Engraver](tech-engraver.md) |
| [Stalker Hunt](tech-forest_supple_leather.md) |
| [Enchanted Thread](tech-enchanted_cotton_thread.md) |

## Related item

| Item |
| --- |
| [Embossed Leather](item-embossed_leather.md) |

## Related recipe

| Recipe |
| --- |
| [Embossed Leather](recipe-embossed_leather.md) |

## Leads to

| Research |
| --- |
| [Embossed Vest](tech-embossed_vest.md) |
| [Embossed Mask](tech-embossed_hat.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"engraver\"",
  "CostTier": "7",
  "AdditionalRequirements": "new List<string> { \"forest_supple_leather\", \"enchanted_cotton_thread\" }",
  "IconName": "\"Icons2_30\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3Engraver.cs:119`
- `Assets.Source.Player/TechNode.cs:1`
