# Mine

Provides raw metal ores to your kingdom.

## Research effect

Provides raw metal ores to your kingdom.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | mine |
| Type | Flow Element |
| Cost tier | 1 |

## Also grants research

| Unlocked automatically |
| --- |
| [Mine Iron Ore](tech-mine_iron_ore.md) |

## Leads to

| Research |
| --- |
| [Mine Iron Ore](tech-mine_iron_ore.md) |
| [Mine Sapphire](tech-mine_sapphire.md) |
| [Mine Gold Ore](tech-mine_gold_ore.md) |
| [Mine Silver Ore](tech-mine_silver_ore.md) |
| [Drudge Miners](tech-mine_automation.md) |
| [Mine · second add-on slot](tech-mine_automation_2.md) |
| [Mine · overseers](tech-mine_productivity.md) |
| [Mine · artisans](tech-mine_quality.md) |
| [Mine · third add-on slot](tech-mine_automation_3.md) |
| [Decorations](tech-tech_deco.md) |
| [Forge](tech-forge.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "AbsolutePosition": "new Vector2Int(-600, -272)",
  "IconName": "\"Icons_1\"",
  "CostTier": "1",
  "CostMultiplier": "0.0",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddTech(\"mine_iron_ore\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Mine.cs:11`
- `Assets.Source.Player/TechNode.cs:1`
