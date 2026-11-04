# Grinding Wheel

Unlocks the first Upgrade slot for your Jeweler.

Unlocks the Worker upgrade to automatically craft jewelry.

## Research effect

Unlocks the first Upgrade slot for your Jeweler.

Unlocks the Worker upgrade to automatically craft jewelry.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | jeweler_automation |
| Type | Upgrade Slot |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Jeweler](tech-jeweler.md) |

## Leads to

| Research |
| --- |
| [Jeweler · second add-on slot](tech-jeweler_automation_2.md) |
| [Jeweler · overseers](tech-jeweler_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Jeweler\", \"callSource\": \"source/Assets.Source.Player.Tech/T8Jeweler.cs\", \"callLine\": 24, \"id\": \"jeweler_automation\", \"root\": \"jeweler\", \"tier\": 8, \"name\": \"Grinding Wheel\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"jeweler\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T8Jeweler.cs:24`
