# Archmage's Hat

The kind of headwear that draws attention at a conference of mages. Subtle thought manipulation makes the wearer more adept at magic.

## Research effect

The kind of headwear that draws attention at a conference of mages. Subtle thought manipulation makes the wearer more adept at magic.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | archmage_hat |
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
| [Archmage's Hat](item-archmage_hat.md) |

## Related recipe

| Recipe |
| --- |
| [Archmage's Hat](recipe-archmage_hat.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"scribe\"",
  "IconName": "\"Icons3_10\"",
  "CostCurrency": "CurrencyCollection.GoldIngenuity",
  "AdditionalRequirements": "new List<string> { \"dungeon_catacombs\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Scribe.cs:166`
- `Assets.Source.Player/TechNode.cs:1`
