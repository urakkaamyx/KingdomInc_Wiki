# Cyclopean Battleaxe

The malignant growth overtaking this axe has manifested as a giant, unblinking eye, staring at its enemies with unrestrained fury.

## Research effect

The malignant growth overtaking this axe has manifested as a giant, unblinking eye, staring at its enemies with unrestrained fury.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | unblinking_axe |
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
| [Cyclopean Battleaxe](item-unblinking_axe.md) |

## Related recipe

| Recipe |
| --- |
| [Cyclopean Battleaxe](recipe-unblinking_axe.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"shrine\"",
  "IconName": "\"Icons3_20\"",
  "CostCurrency": "CurrencyCollection.GoldFaith",
  "AdditionalRequirements": "new List<string> { \"dungeon_archive\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:159`
- `Assets.Source.Player/TechNode.cs:1`
