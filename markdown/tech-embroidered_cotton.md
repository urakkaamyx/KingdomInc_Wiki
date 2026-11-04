# Embroidered Cotton

Patterned with arcane symbols and suitable for the creation of powerful equipment.

## Research effect

Patterned with arcane symbols and suitable for the creation of powerful equipment.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | embroidered_cotton |
| Type | Recipe |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Engraver](tech-engraver.md) |
| [Enchanted Thread](tech-enchanted_cotton_thread.md) |

## Related item

| Item |
| --- |
| [Embroidered Cotton](item-embroidered_cotton.md) |

## Related recipe

| Recipe |
| --- |
| [Embroidered Cotton](recipe-embroidered_cotton.md) |

## Leads to

| Research |
| --- |
| [Scholar's Robe](tech-cotton_robe.md) |
| [Scholar's Hat](tech-cotton_hat.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"engraver\"",
  "CostTier": "7",
  "AdditionalRequirements": "new List<string> { \"enchanted_cotton_thread\" }",
  "IconName": "\"Icons2_28\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3Engraver.cs:111`
- `Assets.Source.Player/TechNode.cs:1`
