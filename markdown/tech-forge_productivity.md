# Forge · overseers

Forge · overseers is a tier 4 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | forge_productivity |
| Type | Upgrade Slot |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Forge](tech-forge.md) |
| [Forge Attendant](tech-forge_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"Forge\", \"callSource\": \"source/Assets.Source.Player.Tech/T1Forge.cs\", \"callLine\": 41, \"id\": \"forge_productivity\", \"previous\": \"forge_automation\", \"additional\": [\"war_effort\"], \"tier\": 4, \"name\": \"Forge · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"forge\", \"requires\": [\"forge\", \"forge_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T1Forge.cs:41`
