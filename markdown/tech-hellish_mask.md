# Malignant Mask

The mask slowly grows over the wearer's face, replacing their human features with a horrifying demonic visage.

## Research effect

The mask slowly grows over the wearer's face, replacing their human features with a horrifying demonic visage.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | hellish_mask |
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
| [Malignant Mask](item-hellish_mask.md) |

## Related recipe

| Recipe |
| --- |
| [Malignant Mask](recipe-hellish_mask.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"scribe\"",
  "IconName": "\"Icons3_6\"",
  "CostCurrency": "CurrencyCollection.GoldIngenuity",
  "AdditionalRequirements": "new List<string> { \"dungeon_catacombs\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Scribe.cs:150`
- `Assets.Source.Player/TechNode.cs:1`
