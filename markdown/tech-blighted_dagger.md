# Blighted Dagger

A system of hollow tubes constantly delivers a deadly mixture of flesh-devouring toxins to the tip of the blade.

## Research effect

A system of hollow tubes constantly delivers a deadly mixture of flesh-devouring toxins to the tip of the blade.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | blighted_dagger |
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
| [Blighted Dagger](item-blighted_dagger.md) |

## Related recipe

| Recipe |
| --- |
| [Blighted Dagger](recipe-blighted_dagger.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"shrine\"",
  "IconName": "\"Icons3_18\"",
  "CostCurrency": "CurrencyCollection.GoldFaith",
  "AdditionalRequirements": "new List<string> { \"dungeon_archive\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:135`
- `Assets.Source.Player/TechNode.cs:1`
