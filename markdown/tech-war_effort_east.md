# War: Eastern Front

Yensburg once controlled territory to the east up to the fortress city of Bastion. Recently, an army of orcs has invaded and occupied those lands.

## Research effect

Yensburg once controlled territory to the east up to the fortress city of Bastion. Recently, an army of orcs has invaded and occupied those lands.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | war_effort_east |
| Type | War |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Enchanter](tech-enchanter.md) |

## Leads to

| Research |
| --- |
| [Shield of the Innocent](tech-shield_innocent.md) |
| [Aiding the Refugees](tech-aid_refugees.md) |
| [Desperate Measures](tech-adv_to_war.md) |
| [Farm](tech-farm.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.War",
  "Previous": "\"enchanter\"",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons_176\"",
  "OverrideRootNode": "\"war_effort\"",
  "CostCurrency": "CurrencyCollection.GoldRing",
  "CostMultiplier": "8.0",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tGamePlayer.Current.UnlockWar(\"eastern\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T6Enchanter.cs:205`
- `Assets.Source.Player/TechNode.cs:1`
