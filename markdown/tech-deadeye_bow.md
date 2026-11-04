# Deadeye Bow

Demonic flesh bursts forth and covers the shooter's hand, correcting their aim and infecting their arrows with hellish rot.

## Research effect

Demonic flesh bursts forth and covers the shooter's hand, correcting their aim and infecting their arrows with hellish rot.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | deadeye_bow |
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
| [Deadeye Bow](item-deadeye_bow.md) |

## Related recipe

| Recipe |
| --- |
| [Deadeye Bow](recipe-deadeye_bow.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"shrine\"",
  "IconName": "\"Icons3_26\"",
  "CostCurrency": "CurrencyCollection.GoldFaith",
  "AdditionalRequirements": "new List<string> { \"dungeon_archive\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:167`
- `Assets.Source.Player/TechNode.cs:1`
