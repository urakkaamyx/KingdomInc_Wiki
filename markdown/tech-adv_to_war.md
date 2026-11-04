# Desperate Measures

Adventurers can now be sent to the War Effort. Combat effectiveness is reduced by up to 50% based on energy levels.

## Research effect

Adventurers can now be sent to the War Effort. Combat effectiveness is reduced by up to 50% based on energy levels.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | adv_to_war |
| Type | Utility |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [War: Eastern Front](tech-war_effort_east.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"war_effort_east\"",
  "RelativePosition": "new Vector2Int(-315, 45)",
  "CostMultiplier": "3.0",
  "IconName": "\"Icons_172\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T6Enchanter.cs:219`
- `Assets.Source.Player/TechNode.cs:1`
