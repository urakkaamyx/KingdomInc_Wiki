# Archmage's Robe

Stylish and gaudy, this magnificent robe is sure to awe anyone that sees you wearing it. No harm ever came from trying on some clothes, right?

## Research effect

Stylish and gaudy, this magnificent robe is sure to awe anyone that sees you wearing it. No harm ever came from trying on some clothes, right?

## Research data

| Property | Value |
| --- | --- |
| Internal ID | archmage_robe |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Scribe](tech-scribe.md) |
| [Yensburg Catacombs](tech-dungeon_catacombs.md) |

## Related item

| Item |
| --- |
| [Archmage's Robe](item-archmage_robe.md) |

## Related recipe

| Recipe |
| --- |
| [Archmage's Robe](recipe-archmage_robe.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"scribe\"",
  "IconName": "\"Icons3_12\"",
  "CostCurrency": "CurrencyCollection.GoldIngenuity",
  "AdditionalRequirements": "new List<string> { \"dungeon_catacombs\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Scribe.cs:174`
- `Assets.Source.Player/TechNode.cs:1`
