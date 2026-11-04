# Overflowing Armory

Adds a pass-through output to all global storage nodes that are configured as collectors. When connected, items are passed to this output if the storage buffer is full.

## Research effect

Adds a pass-through output to all global storage nodes that are configured as collectors. When connected, items are passed to this output if the storage buffer is full.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | armory_overflow |
| Type | Utility |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Extradimensional Storage Space](tech-armory_unlock_channels.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"armory_unlock_channels\"",
  "RelativePosition": "new Vector2Int(-180, 0)",
  "IconName": "\"Icons_103\"",
  "CostCurrency": "CurrencyCollection.GoldMana",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tforeach (Armory element4 in ply.GetElements<Armory>())\n\t\t\t\t{\n\t\t\t\t\tif (element4.OutputType == null)\n\t\t\t\t\t{\n\t\t\t\t\t\telement4.SetOutputType(null);\n\t\t\t\t\t\telement4.World.UpdateIO();\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:127`
- `Assets.Source.Player/TechNode.cs:1`
