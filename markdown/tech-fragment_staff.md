# Splintered Staff

Unable to contain its frightening power, the staff fractured into shards that are still bound together by some unseen force.

## Research effect

Unable to contain its frightening power, the staff fractured into shards that are still bound together by some unseen force.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | fragment_staff |
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
| [Splintered Staff](item-fragment_staff.md) |

## Related recipe

| Recipe |
| --- |
| [Splintered Staff](recipe-fragment_staff.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"shrine\"",
  "IconName": "\"Icons3_30\"",
  "CostCurrency": "CurrencyCollection.GoldFaith",
  "AdditionalRequirements": "new List<string> { \"dungeon_archive\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:175`
- `Assets.Source.Player/TechNode.cs:1`
