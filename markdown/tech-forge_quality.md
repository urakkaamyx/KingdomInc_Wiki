# Forge · artisans

Forge · artisans is a tier 4 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | forge_quality |
| Type | Upgrade Slot |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Forge](tech-forge.md) |
| [Smelting Array](tech-forge_automation_2.md) |

## Additional condition

Requires war progress: Byrgenwald College

## Campaign condition

forest:2 (campaign ID : completed stage)

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 94, \"generated\": true, \"building\": \"Forge\", \"callSource\": \"source/Assets.Source.Player.Tech/T1Forge.cs\", \"callLine\": 41, \"id\": \"forge_quality\", \"previous\": \"forge_automation_2\", \"tier\": 4, \"name\": \"Forge · artisans\", \"icon\": \"Icons_118\", \"addon\": \"Artisan\", \"warGate\": \"forest:2\", \"conditionText\": \"Requires war progress: Byrgenwald College\", \"root\": \"forge\", \"requires\": [\"forge\", \"forge_automation_2\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:94`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T1Forge.cs:41`
