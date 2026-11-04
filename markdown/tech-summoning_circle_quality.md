# Summoning Circle · artisans

Summoning Circle · artisans is a tier 10 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | summoning_circle_quality |
| Type | Upgrade Slot |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Summoning Circle](tech-summoning_circle.md) |
| [Witch Coven](tech-summoning_circle_automation_2.md) |

## Additional condition

Requires war progress: Byrgenwald College

## Campaign condition

forest:2 (campaign ID : completed stage)

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 94, \"generated\": true, \"building\": \"SummoningCircle\", \"callSource\": \"source/Assets.Source.Player.Tech/T8SummoningCircle.cs\", \"callLine\": 25, \"id\": \"summoning_circle_quality\", \"previous\": \"summoning_circle_automation_2\", \"tier\": 10, \"name\": \"Summoning Circle · artisans\", \"icon\": \"Icons_118\", \"addon\": \"Artisan\", \"warGate\": \"forest:2\", \"conditionText\": \"Requires war progress: Byrgenwald College\", \"root\": \"summoning_circle\", \"requires\": [\"summoning_circle\", \"summoning_circle_automation_2\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:94`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T8SummoningCircle.cs:25`
