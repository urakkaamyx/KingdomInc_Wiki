# Malignant Cover

Tiny needles hook into the wearer's flesh, causing immense discomfort but somehow also making almost any movement more graceful and deadly.

## Research effect

Tiny needles hook into the wearer's flesh, causing immense discomfort but somehow also making almost any movement more graceful and deadly.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | hellish_cover |
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
| [Malignant Cover](item-hellish_cover.md) |

## Related recipe

| Recipe |
| --- |
| [Malignant Cover](recipe-hellish_cover.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"scribe\"",
  "IconName": "\"Icons3_8\"",
  "CostCurrency": "CurrencyCollection.GoldIngenuity",
  "AdditionalRequirements": "new List<string> { \"dungeon_catacombs\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Scribe.cs:158`
- `Assets.Source.Player/TechNode.cs:1`
