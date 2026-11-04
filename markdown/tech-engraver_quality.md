# Engraver · artisans

Engraver · artisans is a tier 5 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | engraver_quality |
| Type | Upgrade Slot |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Engraver](tech-engraver.md) |
| [Parallel Engraving](tech-engraver_automation_2.md) |

## Additional condition

Requires war progress: Byrgenwald College

## Campaign condition

forest:2 (campaign ID : completed stage)

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 94, \"generated\": true, \"building\": \"Engraver\", \"callSource\": \"source/Assets.Source.Player.Tech/T3Engraver.cs\", \"callLine\": 23, \"id\": \"engraver_quality\", \"previous\": \"engraver_automation_2\", \"tier\": 5, \"name\": \"Engraver · artisans\", \"icon\": \"Icons_118\", \"addon\": \"Artisan\", \"warGate\": \"forest:2\", \"conditionText\": \"Requires war progress: Byrgenwald College\", \"root\": \"engraver\", \"requires\": [\"engraver\", \"engraver_automation_2\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:94`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T3Engraver.cs:23`
