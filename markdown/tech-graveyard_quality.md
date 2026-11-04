# Graveyard · artisans

Graveyard · artisans is a tier 13 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | graveyard_quality |
| Type | Upgrade Slot |
| Cost tier | 13 |

## Prerequisites

| Required research |
| --- |
| [Graveyard](tech-graveyard.md) |
| [Animated Shovels](tech-graveyard_automation_2.md) |

## Additional condition

Requires war progress: Byrgenwald College

## Campaign condition

forest:2 (campaign ID : completed stage)

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 94, \"generated\": true, \"building\": \"Graveyard\", \"callSource\": \"source/Assets.Source.Player.Tech/T11Graveyard.cs\", \"callLine\": 57, \"id\": \"graveyard_quality\", \"previous\": \"graveyard_automation_2\", \"tier\": 13, \"name\": \"Graveyard · artisans\", \"icon\": \"Icons_118\", \"addon\": \"Artisan\", \"warGate\": \"forest:2\", \"conditionText\": \"Requires war progress: Byrgenwald College\", \"root\": \"graveyard\", \"requires\": [\"graveyard\", \"graveyard_automation_2\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:94`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T11Graveyard.cs:57`
