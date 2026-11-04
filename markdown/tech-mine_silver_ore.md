# Mine Silver Ore

A large deposit deep underground provides a steady supply of Silver Ore.

## Research effect

A large deposit deep underground provides a steady supply of Silver Ore.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | mine_silver_ore |
| Type | Resource |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Mine](tech-mine.md) |
| [Engraver](tech-engraver.md) |

## Resource quota granted

| Resource | Amount |
| --- | --- |
| [Silver Ore](item-silver_ore.md) | 0.5 |

## Leads to

| Research |
| --- |
| [Silver Ingot](tech-silver_ingot.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Resource",
  "Root": "\"mine\"",
  "IconName": "\"Icons_87\"",
  "CostTier": "3",
  "AdditionalRequirements": "new List<string> { \"engraver\" }",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddResource(\"silver_ore\", 0.5);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Mine.cs:61`
- `Assets.Source.Player/TechNode.cs:1`
