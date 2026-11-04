# Imbue Dark Essence

Weaves a powerful Dark Essence into any piece of equipment to significantly increase its quality.

## Research effect

Weaves a powerful Dark Essence into any piece of equipment to significantly increase its quality.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | enchant_item_quality |
| Type | Recipe |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Enchanter](tech-enchanter.md) |
| [Temple of the Last Rite](tech-dungeon_temple.md) |

## Related recipe

| Recipe |
| --- |
| [Imbue Dark Essence](recipe-enchant_item_quality.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"enchanter\"",
  "IconName": "\"Icons2_221\"",
  "AdditionalRequirements": "new List<string> { \"dungeon_temple\" }",
  "CostTier": "9",
  "CostCurrency": "CurrencyCollection.GoldMana"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T6Enchanter.cs:114`
- `Assets.Source.Player/TechNode.cs:1`
