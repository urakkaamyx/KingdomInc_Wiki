# Butcher · artisans

Butcher · artisans is a tier 9 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | butcher_quality |
| Type | Upgrade Slot |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Butcher](tech-butcher.md) |
| [Rapid Dissection](tech-butcher_automation_2.md) |

## Additional condition

Requires war progress: Byrgenwald College

## Campaign condition

forest:2 (campaign ID : completed stage)

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 94, \"generated\": true, \"building\": \"Butcher\", \"callSource\": \"source/Assets.Source.Player.Tech/T7Butcher.cs\", \"callLine\": 23, \"id\": \"butcher_quality\", \"previous\": \"butcher_automation_2\", \"tier\": 9, \"name\": \"Butcher · artisans\", \"icon\": \"Icons_118\", \"addon\": \"Artisan\", \"warGate\": \"forest:2\", \"conditionText\": \"Requires war progress: Byrgenwald College\", \"root\": \"butcher\", \"requires\": [\"butcher\", \"butcher_automation_2\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:94`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T7Butcher.cs:23`
