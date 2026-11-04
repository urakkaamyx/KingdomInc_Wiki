# Wilderness Cookery

Unlocks the first Upgrade slot for your Campfires.

Unlocks the Worker upgrade to automatically cook simple food.

## Research effect

Unlocks the first Upgrade slot for your Campfires.

Unlocks the Worker upgrade to automatically cook simple food.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | campfire_automation |
| Type | Upgrade Slot |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Campfire](tech-campfire.md) |

## Leads to

| Research |
| --- |
| [Campfire · second add-on slot](tech-campfire_automation_2.md) |
| [Campfire · overseers](tech-campfire_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Campfire\", \"callSource\": \"source/Assets.Source.Player.Tech/T4Campfire.cs\", \"callLine\": 56, \"id\": \"campfire_automation\", \"root\": \"campfire\", \"tier\": 4, \"name\": \"Wilderness Cookery\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"campfire\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T4Campfire.cs:56`
