# Training Grounds · artisans

Training Grounds · artisans is a tier 7 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | training_grounds_quality |
| Type | Upgrade Slot |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Training Grounds](tech-training_grounds.md) |
| [We Work Together](tech-training_grounds_automation_2.md) |

## Additional condition

Requires war progress: Byrgenwald College

## Campaign condition

forest:2 (campaign ID : completed stage)

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 94, \"generated\": true, \"building\": \"TrainingGrounds\", \"callSource\": \"source/Assets.Source.Player.Tech/T5TrainingGrounds.cs\", \"callLine\": 26, \"id\": \"training_grounds_quality\", \"previous\": \"training_grounds_automation_2\", \"tier\": 7, \"name\": \"Training Grounds · artisans\", \"icon\": \"Icons_118\", \"addon\": \"TrainingArtisan\", \"warGate\": \"forest:2\", \"conditionText\": \"Requires war progress: Byrgenwald College\", \"root\": \"training_grounds\", \"requires\": [\"training_grounds\", \"training_grounds_automation_2\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:94`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:26`
