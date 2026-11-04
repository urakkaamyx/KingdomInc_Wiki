# Inventor · artisans

Inventor · artisans is a tier 12 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | inventor_quality |
| Type | Upgrade Slot |
| Cost tier | 12 |

## Prerequisites

| Required research |
| --- |
| [Inventor](tech-inventor.md) |
| [Eureka!](tech-inventor_automation_2.md) |

## Additional condition

Requires war progress: Byrgenwald College

## Campaign condition

forest:2 (campaign ID : completed stage)

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 94, \"generated\": true, \"building\": \"Inventor\", \"callSource\": \"source/Assets.Source.Player.Tech/T10Inventor.cs\", \"callLine\": 25, \"id\": \"inventor_quality\", \"previous\": \"inventor_automation_2\", \"tier\": 12, \"name\": \"Inventor · artisans\", \"icon\": \"Icons_118\", \"addon\": \"Artisan\", \"warGate\": \"forest:2\", \"conditionText\": \"Requires war progress: Byrgenwald College\", \"root\": \"inventor\", \"requires\": [\"inventor\", \"inventor_automation_2\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:94`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T10Inventor.cs:25`
