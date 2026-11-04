# Only Hammers

Unlocks the first Upgrade slot for your Carpenter.

Unlocks the Worker upgrade to automate production.

## Research effect

Unlocks the first Upgrade slot for your Carpenter.

Unlocks the Worker upgrade to automate production.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | carpenter_automation |
| Type | Upgrade Slot |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Carpenter](tech-carpenter.md) |

## Leads to

| Research |
| --- |
| [Carpenter · second add-on slot](tech-carpenter_automation_2.md) |
| [Carpenter · overseers](tech-carpenter_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Carpenter\", \"callSource\": \"source/Assets.Source.Player.Tech/T2Carpenter.cs\", \"callLine\": 157, \"id\": \"carpenter_automation\", \"root\": \"carpenter\", \"tier\": 2, \"name\": \"Only Hammers\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"carpenter\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T2Carpenter.cs:157`
