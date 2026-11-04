# Prayer Wheel

Unlocks the first Upgrade slot for your Shrine.

Unlocks the Worker upgrade to automate blessings and prayers.

## Research effect

Unlocks the first Upgrade slot for your Shrine.

Unlocks the Worker upgrade to automate blessings and prayers.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | shrine_automation |
| Type | Upgrade Slot |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Shrine](tech-shrine.md) |

## Leads to

| Research |
| --- |
| [Shrine · second add-on slot](tech-shrine_automation_2.md) |
| [Shrine · overseers](tech-shrine_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Shrine\", \"callSource\": \"source/Assets.Source.Player.Tech/T11Shrine.cs\", \"callLine\": 26, \"id\": \"shrine_automation\", \"root\": \"shrine\", \"tier\": 11, \"name\": \"Prayer Wheel\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"shrine\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T11Shrine.cs:26`
