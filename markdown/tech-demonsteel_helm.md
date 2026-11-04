# Demonsteel Helm

The incessant clicking of gears has been replaced with maddening whispers.

## Research effect

The incessant clicking of gears has been replaced with maddening whispers.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | demonsteel_helm |
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
| [Demonsteel Helm](item-demonsteel_helm.md) |

## Related recipe

| Recipe |
| --- |
| [Demonsteel Helm](recipe-demonsteel_helm.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"scribe\"",
  "IconName": "\"Icons3_2\"",
  "CostCurrency": "CurrencyCollection.GoldIngenuity",
  "AdditionalRequirements": "new List<string> { \"dungeon_catacombs\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Scribe.cs:126`
- `Assets.Source.Player/TechNode.cs:1`
