# Drill Sergeant

Unlocks the first Upgrade slot for your Training Grounds.

Unlocks the Worker upgrade to automatically train adventurers and conscripts.

## Research effect

Unlocks the first Upgrade slot for your Training Grounds.

Unlocks the Worker upgrade to automatically train adventurers and conscripts.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | training_grounds_automation |
| Type | Upgrade Slot |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Training Grounds](tech-training_grounds.md) |

## Leads to

| Research |
| --- |
| [Training Grounds · second add-on slot](tech-training_grounds_automation_2.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"TrainingGrounds\", \"callSource\": \"source/Assets.Source.Player.Tech/T5TrainingGrounds.cs\", \"callLine\": 24, \"id\": \"training_grounds_automation\", \"root\": \"training_grounds\", \"tier\": 5, \"name\": \"Drill Sergeant\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"training_grounds\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:24`
