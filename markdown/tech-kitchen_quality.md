# Kitchen · artisans

Kitchen · artisans is a tier 9 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | kitchen_quality |
| Type | Upgrade Slot |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Kitchen](tech-kitchen.md) |
| [Kitchen Brigade](tech-kitchen_automation_2.md) |

## Additional condition

Requires war progress: Byrgenwald College

## Campaign condition

forest:2 (campaign ID : completed stage)

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 94, \"generated\": true, \"building\": \"Kitchen\", \"callSource\": \"source/Assets.Source.Player.Tech/T7Kitchen.cs\", \"callLine\": 19, \"id\": \"kitchen_quality\", \"previous\": \"kitchen_automation_2\", \"tier\": 9, \"name\": \"Kitchen · artisans\", \"icon\": \"Icons_118\", \"addon\": \"Artisan\", \"warGate\": \"forest:2\", \"conditionText\": \"Requires war progress: Byrgenwald College\", \"root\": \"kitchen\", \"requires\": [\"kitchen\", \"kitchen_automation_2\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:94`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T7Kitchen.cs:19`
