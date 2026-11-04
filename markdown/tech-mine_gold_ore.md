# Mine Gold Ore

Your miners have discovered a mineral vein rich in Gold Ore.

## Research effect

Your miners have discovered a mineral vein rich in Gold Ore.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | mine_gold_ore |
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
| [Gold Ore](item-gold_ore.md) | 0.5 |

## Leads to

| Research |
| --- |
| [Gold Ingot](tech-gold_ingot.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Resource",
  "Root": "\"mine\"",
  "IconName": "\"Icons_88\"",
  "CostTier": "3",
  "AdditionalRequirements": "new List<string> { \"engraver\" }",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddResource(\"gold_ore\", 0.5);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Mine.cs:49`
- `Assets.Source.Player/TechNode.cs:1`
