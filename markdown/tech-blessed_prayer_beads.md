# Blessed Prayer Beads

Having been blessed by a miracle of Saint Ilonia, clerics from all walks of life would be honored to own these beads.

## Research effect

Having been blessed by a miracle of Saint Ilonia, clerics from all walks of life would be honored to own these beads.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | blessed_prayer_beads |
| Type | Recipe |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Shrine](tech-shrine.md) |

## Related item

| Item |
| --- |
| [Blessed Prayer Beads](item-blessed_prayer_beads.md) |

## Related recipe

| Recipe |
| --- |
| [Blessed Prayer Beads](recipe-blessed_prayer_beads.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"shrine\"",
  "IconName": "\"Icons3_71\"",
  "CostCurrency": "CurrencyCollection.GoldFaith",
  "CostMultiplier": "0.5"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:38`
- `Assets.Source.Player/TechNode.cs:1`
