# Honest Craftmanship

Unlocks the first Upgrade slot for your Leatherworker.

Unlocks the Worker upgrade to automate production.

## Research effect

Unlocks the first Upgrade slot for your Leatherworker.

Unlocks the Worker upgrade to automate production.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | leatherworker_automation |
| Type | Upgrade Slot |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Leatherworker](tech-leatherworker.md) |

## Leads to

| Research |
| --- |
| [Leatherworker · second add-on slot](tech-leatherworker_automation_2.md) |
| [Leatherworker · overseers](tech-leatherworker_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Leatherworker\", \"callSource\": \"source/Assets.Source.Player.Tech/T2Leatherworker.cs\", \"callLine\": 94, \"id\": \"leatherworker_automation\", \"root\": \"leatherworker\", \"tier\": 2, \"name\": \"Honest Craftmanship\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"leatherworker\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T2Leatherworker.cs:94`
