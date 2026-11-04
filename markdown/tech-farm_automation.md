# Farmhand

Unlocks the first Upgrade slot for your Farm.

Unlocks the Worker upgrade to automatically harvest items.

## Research effect

Unlocks the first Upgrade slot for your Farm.

Unlocks the Worker upgrade to automatically harvest items.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | farm_automation |
| Type | Upgrade Slot |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Farm](tech-farm.md) |

## Leads to

| Research |
| --- |
| [Farm · second add-on slot](tech-farm_automation_2.md) |
| [Farm · overseers](tech-farm_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Farm\", \"callSource\": \"source/Assets.Source.Player.Tech/T7Farm.cs\", \"callLine\": 35, \"id\": \"farm_automation\", \"root\": \"farm\", \"tier\": 7, \"name\": \"Farmhand\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"farm\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T7Farm.cs:35`
