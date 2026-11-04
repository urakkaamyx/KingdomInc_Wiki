# Carpenter · artisans

Carpenter · artisans is a tier 4 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | carpenter_quality |
| Type | Upgrade Slot |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Carpenter](tech-carpenter.md) |
| [Streamlined Carpentry](tech-carpenter_automation_2.md) |

## Additional condition

Requires war progress: Byrgenwald College

## Campaign condition

forest:2 (campaign ID : completed stage)

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 94, \"generated\": true, \"building\": \"Carpenter\", \"callSource\": \"source/Assets.Source.Player.Tech/T2Carpenter.cs\", \"callLine\": 157, \"id\": \"carpenter_quality\", \"previous\": \"carpenter_automation_2\", \"tier\": 4, \"name\": \"Carpenter · artisans\", \"icon\": \"Icons_118\", \"addon\": \"Artisan\", \"warGate\": \"forest:2\", \"conditionText\": \"Requires war progress: Byrgenwald College\", \"root\": \"carpenter\", \"requires\": [\"carpenter\", \"carpenter_automation_2\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:94`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T2Carpenter.cs:157`
