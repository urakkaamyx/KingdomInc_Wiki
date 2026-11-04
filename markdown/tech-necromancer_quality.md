# Necromancer · artisans

Necromancer · artisans is a tier 13 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | necromancer_quality |
| Type | Upgrade Slot |
| Cost tier | 13 |

## Prerequisites

| Required research |
| --- |
| [Necromancer](tech-necromancer.md) |
| [Undead Helpers](tech-necromancer_automation_2.md) |

## Additional condition

Requires war progress: Byrgenwald College

## Campaign condition

forest:2 (campaign ID : completed stage)

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 94, \"generated\": true, \"building\": \"Necromancer\", \"callSource\": \"source/Assets.Source.Player.Tech/T11Necromancer.cs\", \"callLine\": 21, \"id\": \"necromancer_quality\", \"previous\": \"necromancer_automation_2\", \"tier\": 13, \"name\": \"Necromancer · artisans\", \"icon\": \"Icons_118\", \"addon\": \"Artisan\", \"warGate\": \"forest:2\", \"conditionText\": \"Requires war progress: Byrgenwald College\", \"root\": \"necromancer\", \"requires\": [\"necromancer\", \"necromancer_automation_2\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:94`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T11Necromancer.cs:21`
