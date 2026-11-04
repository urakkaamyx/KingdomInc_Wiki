# Flash of Brilliance

Refiners and most Crafting nodes gain a 1% chance to double their quality bonus.

## Research effect

Refiners and most Crafting nodes gain a 1% chance to double their quality bonus.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | critical_craft |
| Type | Utility |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Refiner](tech-refiner.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"refiner\"",
  "RelativePosition": "new Vector2Int(-225, 26)",
  "IconName": "\"Icons_158\"",
  "CostMultiplier": "6.0",
  "CostCurrency": "CurrencyCollection.GoldMana"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T6Enchanter.cs:160`
- `Assets.Source.Player/TechNode.cs:1`
