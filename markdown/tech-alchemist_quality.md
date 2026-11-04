# Alchemist · artisans

Alchemist · artisans is a tier 11 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | alchemist_quality |
| Type | Upgrade Slot |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Alchemist](tech-alchemist.md) |
| [Cauldron Stirrers](tech-alchemist_automation_2.md) |

## Additional condition

Requires war progress: Byrgenwald College

## Campaign condition

forest:2 (campaign ID : completed stage)

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 94, \"generated\": true, \"building\": \"Alchemist\", \"callSource\": \"source/Assets.Source.Player.Tech/T9Alchemist.cs\", \"callLine\": 23, \"id\": \"alchemist_quality\", \"previous\": \"alchemist_automation_2\", \"tier\": 11, \"name\": \"Alchemist · artisans\", \"icon\": \"Icons_118\", \"addon\": \"Artisan\", \"warGate\": \"forest:2\", \"conditionText\": \"Requires war progress: Byrgenwald College\", \"root\": \"alchemist\", \"requires\": [\"alchemist\", \"alchemist_automation_2\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:94`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T9Alchemist.cs:23`
