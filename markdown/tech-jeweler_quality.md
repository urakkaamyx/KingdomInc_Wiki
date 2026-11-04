# Jeweler · artisans

Jeweler · artisans is a tier 10 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | jeweler_quality |
| Type | Upgrade Slot |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Jeweler](tech-jeweler.md) |
| [Tiny Fingers](tech-jeweler_automation_2.md) |

## Additional condition

Requires war progress: Byrgenwald College

## Campaign condition

forest:2 (campaign ID : completed stage)

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 94, \"generated\": true, \"building\": \"Jeweler\", \"callSource\": \"source/Assets.Source.Player.Tech/T8Jeweler.cs\", \"callLine\": 24, \"id\": \"jeweler_quality\", \"previous\": \"jeweler_automation_2\", \"tier\": 10, \"name\": \"Jeweler · artisans\", \"icon\": \"Icons_118\", \"addon\": \"Artisan\", \"warGate\": \"forest:2\", \"conditionText\": \"Requires war progress: Byrgenwald College\", \"root\": \"jeweler\", \"requires\": [\"jeweler\", \"jeweler_automation_2\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:94`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T8Jeweler.cs:24`
