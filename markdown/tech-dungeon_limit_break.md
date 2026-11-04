# Together As One

Unlocks a new Upgrade for your Dungeon.

If an Adventurer loses all energy they do not give up until all party members are exhausted.

Adventurers fighting with no energy left suffer a 25% Combat Power penalty.

## Research effect

Unlocks a new Upgrade for your Dungeon.

If an Adventurer loses all energy they do not give up until all party members are exhausted.

Adventurers fighting with no energy left suffer a 25% Combat Power penalty.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | dungeon_limit_break |
| Type | Upgrade Slot |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Dungeon](tech-dungeon.md) |
| [Support Staff](tech-dungeon_automation_2.md) |

## Leads to

| Research |
| --- |
| [Unshakable Devotion](tech-dungeon_limit_break_2.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.UpgradeSlot",
  "Previous": "\"dungeon_automation_2\"",
  "RelativePosition": "new Vector2Int(0, 180)",
  "IconName": "\"Icons2_49\"",
  "CostTier": "9",
  "CostMultiplier": "5.0",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddAvailableFlowUpgrade(\"Dungeon\", \"DungeonLimitBreak\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8Dungeon.cs:59`
- `Assets.Source.Player/TechNode.cs:1`
