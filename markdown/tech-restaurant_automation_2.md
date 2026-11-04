# Restaurant · second add-on slot

Restaurant · second add-on slot is a tier 8 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | restaurant_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Restaurant](tech-restaurant.md) |
| [Tactical Waitstaff](tech-restaurant_automation.md) |
| [War Effort](tech-war_effort.md) |
| [Dungeon](tech-dungeon.md) |

## Leads to

| Research |
| --- |
| [Restaurant · third add-on slot](tech-restaurant_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Restaurant\", \"callSource\": \"source/Assets.Source.Player.Tech/T7Kitchen.cs\", \"callLine\": 55, \"id\": \"restaurant_automation_2\", \"previous\": \"restaurant_automation\", \"tier\": 8, \"additional\": [\"war_effort\", \"dungeon\"], \"name\": \"Restaurant · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"restaurant\", \"requires\": [\"restaurant\", \"restaurant_automation\", \"war_effort\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T7Kitchen.cs:55`
