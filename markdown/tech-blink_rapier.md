# Ethereal Rapier

The thin blade of this sword is only connected to the hilt in some unseen dimension, allowing the point to bypass armor with ease.

## Research effect

The thin blade of this sword is only connected to the hilt in some unseen dimension, allowing the point to bypass armor with ease.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | blink_rapier |
| Type | Recipe |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Shrine](tech-shrine.md) |
| [Timeless Archive](tech-dungeon_archive.md) |

## Related item

| Item |
| --- |
| [Ethereal Rapier](item-blink_rapier.md) |

## Related recipe

| Recipe |
| --- |
| [Ethereal Rapier](recipe-blink_rapier.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"shrine\"",
  "IconName": "\"Icons3_22\"",
  "CostCurrency": "CurrencyCollection.GoldFaith",
  "AdditionalRequirements": "new List<string> { \"dungeon_archive\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
