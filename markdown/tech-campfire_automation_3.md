# Campfire · third add-on slot

Campfire · third add-on slot is a tier 7 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | campfire_automation_3 |
| Type | Upgrade Slot |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Campfire](tech-campfire.md) |
| [Wilderness Kitchen](tech-campfire_automation_2.md) |
| [Dungeon](tech-dungeon.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 73, \"generated\": true, \"building\": \"Campfire\", \"callSource\": \"source/Assets.Source.Player.Tech/T4Campfire.cs\", \"callLine\": 56, \"id\": \"campfire_automation_3\", \"previous\": \"campfire_automation_2\", \"additional\": [\"dungeon\"], \"tier\": 7, \"name\": \"Campfire · third add-on slot\", \"icon\": \"Icons2_77\", \"slotCount\": 3, \"root\": \"campfire\", \"requires\": [\"campfire\", \"campfire_automation_2\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:73`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T4Campfire.cs:56`
