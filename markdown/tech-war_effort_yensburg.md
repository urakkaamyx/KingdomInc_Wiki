# War: Hidden Enemies

A hidden force has struck at the heart of Yensburg. Some districts have fallen under enemy control, and the tunnels beneath the city are crawling with demonic foes.

## Research effect

A hidden force has struck at the heart of Yensburg. Some districts have fallen under enemy control, and the tunnels beneath the city are crawling with demonic foes.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | war_effort_yensburg |
| Type | War |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Arena](tech-arena.md) |

## Leads to

| Research |
| --- |
| [Inventor](tech-inventor.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.War",
  "Previous": "\"arena\"",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons2_1\"",
  "OverrideRootNode": "\"war_effort\"",
  "CostCurrency": "CurrencyCollection.GoldDucat",
  "CostTier": "10",
  "CostMultiplier": "2.0",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tGamePlayer.Current.UnlockWar(\"yensburg\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T9Arena.cs:50`
- `Assets.Source.Player/TechNode.cs:1`
