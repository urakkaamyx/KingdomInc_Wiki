# Enchanted Ink

Jet-black ink imbued with powerful magical energy, suitable for writing spell scrolls and arcane tomes.

## Research effect

Jet-black ink imbued with powerful magical energy, suitable for writing spell scrolls and arcane tomes.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | enchanted_ink |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Enchanter](tech-enchanter.md) |
| [Scribe](tech-scribe.md) |

## Related item

| Item |
| --- |
| [Enchanted Ink](item-enchanted_ink.md) |

## Related recipe

| Recipe |
| --- |
| [Enchanted Ink](recipe-enchanted_ink.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"enchanter\"",
  "IconName": "\"Icons3_59\"",
  "CostTier": "10",
  "CostCurrency": "CurrencyCollection.GoldMana",
  "CostMultiplier": "0.5",
  "AdditionalRequirements": "new List<string> { \"scribe\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T6Enchanter.cs:132`
- `Assets.Source.Player/TechNode.cs:1`
