# Overflowing Portal

Adds a pass-through output to Portals that are configured as collectors. When connected, items are passed to this output if the portal storage buffer is full.

## Research effect

Adds a pass-through output to Portals that are configured as collectors. When connected, items are passed to this output if the portal storage buffer is full.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | portal_overflow |
| Type | Utility |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Multidimensional Transportation](tech-portal_unlock_channels.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"portal_unlock_channels\"",
  "RelativePosition": "new Vector2Int(-180, 0)",
  "IconName": "\"Icons_103\"",
  "CostCurrency": "CurrencyCollection.GoldMana",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tforeach (Portal element2 in ply.GetElements<Portal>())\n\t\t\t\t{\n\t\t\t\t\tif (!element2.IsOutput)\n\t\t\t\t\t{\n\t\t\t\t\t\telement2.SetOutput(output: false);\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Farm.cs:167`
- `Assets.Source.Player/TechNode.cs:1`
