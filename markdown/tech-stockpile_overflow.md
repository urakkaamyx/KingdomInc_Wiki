# Overflowing Stockpile

Adds an optional second output that will only receive items when the stockpile is completely full.

## Research effect

Adds an optional second output that will only receive items when the stockpile is completely full.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | stockpile_overflow |
| Type | Utility |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Dimensional Storage](tech-stockpile_capacity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"stockpile_capacity\"",
  "RelativePosition": "new Vector2Int(-90, 180)",
  "IconName": "\"Icons_103\"",
  "CostCurrency": "CurrencyCollection.GoldMana",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tforeach (Stockpile element in ply.GetElements<Stockpile>())\n\t\t\t\t{\n\t\t\t\t\telement.UpdateOutput();\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T4Forest.cs:204`
- `Assets.Source.Player/TechNode.cs:1`
