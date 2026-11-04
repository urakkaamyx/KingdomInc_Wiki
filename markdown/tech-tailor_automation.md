# Animated Scissors

Unlocks the first Upgrade slot for your Tailor.

Unlocks the Worker upgrade to automate production.

## Research effect

Unlocks the first Upgrade slot for your Tailor.

Unlocks the Worker upgrade to automate production.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | tailor_automation |
| Type | Upgrade Slot |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Tailor](tech-tailor.md) |

## Leads to

| Research |
| --- |
| [Tailor · second add-on slot](tech-tailor_automation_2.md) |
| [Tailor · overseers](tech-tailor_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Tailor\", \"callSource\": \"source/Assets.Source.Player.Tech/T2Tailor.cs\", \"callLine\": 85, \"id\": \"tailor_automation\", \"root\": \"tailor\", \"tier\": 2, \"name\": \"Animated Scissors\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"tailor\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T2Tailor.cs:85`
