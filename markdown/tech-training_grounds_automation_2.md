# Training Grounds · second add-on slot

Unlocks an additional Upgrade slot for your Training Grounds.

Adding more Workers increases training speed.

## Research effect

Unlocks an additional Upgrade slot for your Training Grounds.

Adding more Workers increases training speed.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | training_grounds_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Training Grounds](tech-training_grounds.md) |
| [Drill Sergeant](tech-training_grounds_automation.md) |
| [War Effort](tech-war_effort.md) |
| [Quest Board](tech-quest_board.md) |

## Leads to

| Research |
| --- |
| [Training Grounds · artisans](tech-training_grounds_quality.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"TrainingGrounds\", \"callSource\": \"source/Assets.Source.Player.Tech/T5TrainingGrounds.cs\", \"callLine\": 25, \"id\": \"training_grounds_automation_2\", \"previous\": \"training_grounds_automation\", \"tier\": 6, \"additional\": [\"war_effort\", \"quest_board\"], \"name\": \"Training Grounds · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"training_grounds\", \"requires\": [\"training_grounds\", \"training_grounds_automation\", \"war_effort\", \"quest_board\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:25`
