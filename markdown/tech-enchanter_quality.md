# Enchanter · artisans

Enchanter · artisans is a tier 8 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | enchanter_quality |
| Type | Upgrade Slot |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Enchanter](tech-enchanter.md) |
| [Enchanted Helpers](tech-enchanter_automation_2.md) |

## Additional condition

Requires war progress: Byrgenwald College

## Campaign condition

forest:2 (campaign ID : completed stage)

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 94, \"generated\": true, \"building\": \"Enchanter\", \"callSource\": \"source/Assets.Source.Player.Tech/T6Enchanter.cs\", \"callLine\": 29, \"id\": \"enchanter_quality\", \"previous\": \"enchanter_automation_2\", \"tier\": 8, \"name\": \"Enchanter · artisans\", \"icon\": \"Icons_118\", \"addon\": \"Artisan\", \"warGate\": \"forest:2\", \"conditionText\": \"Requires war progress: Byrgenwald College\", \"root\": \"enchanter\", \"requires\": [\"enchanter\", \"enchanter_automation_2\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:94`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T6Enchanter.cs:29`
