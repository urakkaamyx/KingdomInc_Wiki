# Dungeon · second add-on slot

Dungeon · second add-on slot is a tier 9 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | dungeon_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Dungeon](tech-dungeon.md) |
| [Dungeon Keeper](tech-dungeon_automation.md) |
| [War Effort](tech-war_effort.md) |

## Leads to

| Research |
| --- |
| [Dungeon · third add-on slot](tech-dungeon_automation_3.md) |
| [Together As One](tech-dungeon_limit_break.md) |
| [Perfectly Preserved](tech-dungeon_item_loot.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Dungeon\", \"callSource\": \"source/Assets.Source.Player.Tech/T8Dungeon.cs\", \"callLine\": 29, \"id\": \"dungeon_automation_2\", \"previous\": \"dungeon_automation\", \"tier\": 9, \"additional\": [\"war_effort\", \"dungeon\"], \"name\": \"Dungeon · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"dungeon\", \"requires\": [\"dungeon\", \"dungeon_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T8Dungeon.cs:29`
