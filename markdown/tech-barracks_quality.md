# Barracks · artisans

Barracks · artisans is a tier 5 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | barracks_quality |
| Type | Upgrade Slot |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Barracks](tech-barracks.md) |
| [Structured Recruitment](tech-barracks_automation_2.md) |

## Additional condition

Requires war progress: Byrgenwald College

## Campaign condition

forest:2 (campaign ID : completed stage)

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 94, \"generated\": true, \"building\": \"Barracks\", \"callSource\": \"source/Assets.Source.Player.Tech/T3Barracks.cs\", \"callLine\": 26, \"id\": \"barracks_quality\", \"previous\": \"barracks_automation_2\", \"tier\": 5, \"name\": \"Barracks · artisans\", \"icon\": \"Icons_118\", \"addon\": \"RecruitArtisan\", \"warGate\": \"forest:2\", \"conditionText\": \"Requires war progress: Byrgenwald College\", \"root\": \"barracks\", \"requires\": [\"barracks\", \"barracks_automation_2\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:94`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T3Barracks.cs:26`
