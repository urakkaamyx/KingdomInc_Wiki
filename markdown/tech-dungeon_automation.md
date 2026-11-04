# Dungeon Keeper

Unlocks the first Upgrade slot for your Dungeon.

Unlocks the Worker upgrade to automatically begin expeditions.

## Research effect

Unlocks the first Upgrade slot for your Dungeon.

Unlocks the Worker upgrade to automatically begin expeditions.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | dungeon_automation |
| Type | Upgrade Slot |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Dungeon](tech-dungeon.md) |

## Leads to

| Research |
| --- |
| [Dungeon · second add-on slot](tech-dungeon_automation_2.md) |
| [Trash Loot](tech-dungeon_trash_loot.md) |
| [Ancient Treasures](tech-dungeon_coin_loot.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Dungeon\", \"callSource\": \"source/Assets.Source.Player.Tech/T8Dungeon.cs\", \"callLine\": 28, \"id\": \"dungeon_automation\", \"root\": \"dungeon\", \"tier\": 8, \"name\": \"Dungeon Keeper\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T8Dungeon.cs:28`
