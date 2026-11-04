# Cross-country Carriers

Unlocks the first Upgrade slot for your Forest.

Unlocks the Worker upgrade to automatically extract harvested items from the forest.

## Research effect

Unlocks the first Upgrade slot for your Forest.

Unlocks the Worker upgrade to automatically extract harvested items from the forest.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | forest_automation |
| Type | Upgrade Slot |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Forest](tech-forest.md) |

## Leads to

| Research |
| --- |
| [Forest · second add-on slot](tech-forest_automation_2.md) |
| [Forest · overseers](tech-forest_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Forest\", \"callSource\": \"source/Assets.Source.Player.Tech/T4Forest.cs\", \"callLine\": 39, \"id\": \"forest_automation\", \"root\": \"forest\", \"tier\": 4, \"name\": \"Cross-country Carriers\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"forest\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T4Forest.cs:39`
