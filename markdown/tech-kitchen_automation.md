# Sous Chef

Unlocks the first Upgrade slot for your Kitchens.

Unlocks the Worker upgrade to automatically cook food.

## Research effect

Unlocks the first Upgrade slot for your Kitchens.

Unlocks the Worker upgrade to automatically cook food.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | kitchen_automation |
| Type | Upgrade Slot |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Kitchen](tech-kitchen.md) |

## Leads to

| Research |
| --- |
| [Kitchen · second add-on slot](tech-kitchen_automation_2.md) |
| [Kitchen · overseers](tech-kitchen_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Kitchen\", \"callSource\": \"source/Assets.Source.Player.Tech/T7Kitchen.cs\", \"callLine\": 19, \"id\": \"kitchen_automation\", \"root\": \"kitchen\", \"tier\": 7, \"name\": \"Sous Chef\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"kitchen\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T7Kitchen.cs:19`
