# Forest · artisans

Unlocks the Deep Woods upgrade to increase the quality of forest items, at an additional cost per item.

## Research effect

Unlocks the Deep Woods upgrade to increase the quality of forest items, at an additional cost per item.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | forest_quality |
| Type | Upgrade Slot |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Forest](tech-forest.md) |
| [Logging Camp](tech-forest_automation_2.md) |

## Additional condition

Requires war progress: Byrgenwald College

## Campaign condition

forest:2 (campaign ID : completed stage)

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 94, \"generated\": true, \"building\": \"Forest\", \"callSource\": \"source/Assets.Source.Player.Tech/T4Forest.cs\", \"callLine\": 39, \"id\": \"forest_quality\", \"previous\": \"forest_automation_2\", \"tier\": 6, \"name\": \"Forest · artisans\", \"icon\": \"Icons_118\", \"addon\": \"ForestArtisan\", \"warGate\": \"forest:2\", \"conditionText\": \"Requires war progress: Byrgenwald College\", \"root\": \"forest\", \"requires\": [\"forest\", \"forest_automation_2\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:94`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T4Forest.cs:39`
