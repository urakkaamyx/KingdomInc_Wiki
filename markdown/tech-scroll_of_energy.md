# Scroll of Second Wind

Even just holding it makes you feel revitalized. Reading the scroll will restore energy to the entire party.

## Research effect

Even just holding it makes you feel revitalized. Reading the scroll will restore energy to the entire party.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | scroll_of_energy |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Scribe](tech-scribe.md) |

## Related item

| Item |
| --- |
| [Scroll of Second Wind](item-scroll_of_energy.md) |

## Related recipe

| Recipe |
| --- |
| [Scroll of Second Wind](recipe-scroll_of_energy.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"scribe\"",
  "IconName": "\"Icons3_62\"",
  "CostCurrency": "CurrencyCollection.GoldIngenuity"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Scribe.cs:69`
- `Assets.Source.Player/TechNode.cs:1`
