# The Meat Man

Unlocks the first Upgrade slot for your Butchers.

Unlocks the Worker upgrade to automatically butcher animals.

## Research effect

Unlocks the first Upgrade slot for your Butchers.

Unlocks the Worker upgrade to automatically butcher animals.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | butcher_automation |
| Type | Upgrade Slot |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Butcher](tech-butcher.md) |

## Leads to

| Research |
| --- |
| [Butcher · second add-on slot](tech-butcher_automation_2.md) |
| [Butcher · overseers](tech-butcher_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Butcher\", \"callSource\": \"source/Assets.Source.Player.Tech/T7Butcher.cs\", \"callLine\": 23, \"id\": \"butcher_automation\", \"root\": \"butcher\", \"tier\": 7, \"name\": \"The Meat Man\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"butcher\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T7Butcher.cs:23`
