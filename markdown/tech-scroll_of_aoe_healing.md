# Scroll of Radiance

The scroll's magic is consumed upon use to restore a small amount of health to all party members.

## Research effect

The scroll's magic is consumed upon use to restore a small amount of health to all party members.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | scroll_of_aoe_healing |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Scribe](tech-scribe.md) |

## Related item

| Item |
| --- |
| [Scroll of Radiance](item-scroll_of_aoe_healing.md) |

## Related recipe

| Recipe |
| --- |
| [Scroll of Radiance](recipe-scroll_of_aoe_healing.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"scribe\"",
  "IconName": "\"Icons3_61\"",
  "CostCurrency": "CurrencyCollection.GoldIngenuity"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Scribe.cs:55`
- `Assets.Source.Player/TechNode.cs:1`
