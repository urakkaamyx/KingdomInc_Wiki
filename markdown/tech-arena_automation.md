# Fight Announcer

Unlocks an additional Upgrade slot for your Arenas.

Unlocks the Worker upgrade to automatically start arena fights.

## Research effect

Unlocks an additional Upgrade slot for your Arenas.

Unlocks the Worker upgrade to automatically start arena fights.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | arena_automation |
| Type | Upgrade Slot |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Arena](tech-arena.md) |

## Leads to

| Research |
| --- |
| [Arena · second add-on slot](tech-arena_automation_2.md) |
| [Fight Purse](tech-arena_cashier.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Arena\", \"callSource\": \"source/Assets.Source.Player.Tech/T9Arena.cs\", \"callLine\": 23, \"id\": \"arena_automation\", \"root\": \"arena\", \"tier\": 9, \"name\": \"Fight Announcer\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"arena\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T9Arena.cs:23`
