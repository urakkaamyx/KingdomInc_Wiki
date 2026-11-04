# Parade Armor

A suit of armor made not for protection, but for showing off your wealth and status.

## Research effect

A suit of armor made not for protection, but for showing off your wealth and status.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | gold_armor |
| Type | Recipe |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Blacksmith](tech-blacksmith.md) |
| [Gold Ingot](tech-gold_ingot.md) |
| [Silver Ingot](tech-silver_ingot.md) |

## Related item

| Item |
| --- |
| [Parade Armor](item-gold_armor.md) |

## Related recipe

| Recipe |
| --- |
| [Parade Armor](recipe-gold_armor.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"blacksmith\"",
  "IconName": "\"Icons_107\"",
  "CostTier": "3",
  "AdditionalRequirements": "new List<string> { \"gold_ingot\", \"silver_ingot\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:74`
- `Assets.Source.Player/TechNode.cs:1`
