# Campfire · artisans

Campfire · artisans is a tier 6 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | campfire_quality |
| Type | Upgrade Slot |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Campfire](tech-campfire.md) |
| [Wilderness Kitchen](tech-campfire_automation_2.md) |

## Additional condition

Requires war progress: Byrgenwald College

## Campaign condition

forest:2 (campaign ID : completed stage)

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 94, \"generated\": true, \"building\": \"Campfire\", \"callSource\": \"source/Assets.Source.Player.Tech/T4Campfire.cs\", \"callLine\": 56, \"id\": \"campfire_quality\", \"previous\": \"campfire_automation_2\", \"tier\": 6, \"name\": \"Campfire · artisans\", \"icon\": \"Icons_118\", \"addon\": \"Artisan\", \"warGate\": \"forest:2\", \"conditionText\": \"Requires war progress: Byrgenwald College\", \"root\": \"campfire\", \"requires\": [\"campfire\", \"campfire_automation_2\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:94`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T4Campfire.cs:56`
