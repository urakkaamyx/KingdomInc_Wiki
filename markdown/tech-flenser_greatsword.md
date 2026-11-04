# Flenser's Sword

A blade from the deepest pits of hell. It subtly encourages the wielder to commit horrible atrocities.

## Research effect

A blade from the deepest pits of hell. It subtly encourages the wielder to commit horrible atrocities.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | flenser_greatsword |
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
| [Flenser's Sword](item-flenser_greatsword.md) |

## Related recipe

| Recipe |
| --- |
| [Flenser's Sword](recipe-flenser_greatsword.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"shrine\"",
  "IconName": "\"Icons3_16\"",
  "CostCurrency": "CurrencyCollection.GoldFaith",
  "AdditionalRequirements": "new List<string> { \"dungeon_archive\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:151`
- `Assets.Source.Player/TechNode.cs:1`
