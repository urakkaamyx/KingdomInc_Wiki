# Dark Prophet's Hood

The wearer is tormented by myriad voices screaming blasphemous prophecies into their ears.

## Research effect

The wearer is tormented by myriad voices screaming blasphemous prophecies into their ears.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | prophet_hood |
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
| [Dark Prophet's Hood](item-prophet_hood.md) |

## Related recipe

| Recipe |
| --- |
| [Dark Prophet's Hood](recipe-prophet_hood.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"scribe\"",
  "IconName": "\"Icons3_13\"",
  "CostCurrency": "CurrencyCollection.GoldIngenuity",
  "AdditionalRequirements": "new List<string> { \"dungeon_catacombs\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Scribe.cs:182`
- `Assets.Source.Player/TechNode.cs:1`
