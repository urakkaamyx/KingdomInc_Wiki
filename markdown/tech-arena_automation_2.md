# Arena · second add-on slot

Arena · second add-on slot is a tier 10 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | arena_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Arena](tech-arena.md) |
| [Fight Announcer](tech-arena_automation.md) |
| [War Effort](tech-war_effort.md) |
| [Dungeon](tech-dungeon.md) |

## Leads to

| Research |
| --- |
| [Arena · third add-on slot](tech-arena_automation_3.md) |
| [Fight To The Death](tech-arena_blood_sport.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Arena\", \"callSource\": \"source/Assets.Source.Player.Tech/T9Arena.cs\", \"callLine\": 24, \"id\": \"arena_automation_2\", \"previous\": \"arena_automation\", \"tier\": 10, \"additional\": [\"war_effort\", \"dungeon\"], \"name\": \"Arena · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"arena\", \"requires\": [\"arena\", \"arena_automation\", \"war_effort\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T9Arena.cs:24`
