# Blank Tome

Pristine blank pages, ready to be filled with arcane incantations or prophetic writings.

## Research effect

Pristine blank pages, ready to be filled with arcane incantations or prophetic writings.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | blank_tome |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Scribe](tech-scribe.md) |

## Related item

| Item |
| --- |
| [Blank Tome](item-blank_tome.md) |

## Related recipe

| Recipe |
| --- |
| [Blank Tome](recipe-blank_tome.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"scribe\"",
  "IconName": "\"Icons3_38\"",
  "CostCurrency": "CurrencyCollection.GoldIngenuity",
  "CostMultiplier": "0.5"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Scribe.cs:32`
- `Assets.Source.Player/TechNode.cs:1`
