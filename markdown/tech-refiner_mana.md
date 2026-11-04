# Mana Sculptor

Refiners now consume mana. In exchange, the refining process is four times more likely to succeed.

This upgrade can be disabled on any individual Refiner.

## Research effect

Refiners now consume mana. In exchange, the refining process is four times more likely to succeed.

This upgrade can be disabled on any individual Refiner.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | refiner_mana |
| Type | Utility |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Refiner](tech-refiner.md) |

## Leads to

| Research |
| --- |
| [Metamorphosis](tech-refiner_demon.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"refiner\"",
  "RelativePosition": "new Vector2Int(225, 26)",
  "IconName": "\"Icons2_48\"",
  "CostMultiplier": "6.0",
  "CostCurrency": "CurrencyCollection.GoldMana",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tforeach (Refiner element in ply.GetElements<Refiner>())\n\t\t\t\t{\n\t\t\t\t\telement.ToggleUseMana(true);\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T6Enchanter.cs:169`
- `Assets.Source.Player/TechNode.cs:1`
