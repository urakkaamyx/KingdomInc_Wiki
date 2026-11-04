# Forge · second add-on slot

Forge · second add-on slot is a tier 3 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | forge_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Forge](tech-forge.md) |
| [Forge Attendant](tech-forge_automation.md) |
| [War Effort](tech-war_effort.md) |

## Leads to

| Research |
| --- |
| [Forge · artisans](tech-forge_quality.md) |
| [Forge · third add-on slot](tech-forge_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Forge\", \"callSource\": \"source/Assets.Source.Player.Tech/T1Forge.cs\", \"callLine\": 41, \"id\": \"forge_automation_2\", \"previous\": \"forge_automation\", \"tier\": 3, \"additional\": [\"war_effort\"], \"name\": \"Forge · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"forge\", \"requires\": [\"forge\", \"forge_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T1Forge.cs:41`
