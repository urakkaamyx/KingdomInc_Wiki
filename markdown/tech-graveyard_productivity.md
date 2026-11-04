# Graveyard · overseers

Graveyard · overseers is a tier 12 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | graveyard_productivity |
| Type | Upgrade Slot |
| Cost tier | 12 |
| Visibility | Hidden by code |

## Prerequisites

| Required research |
| --- |
| [Graveyard](tech-graveyard.md) |
| [Gravedigger](tech-graveyard_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"Graveyard\", \"callSource\": \"source/Assets.Source.Player.Tech/T11Graveyard.cs\", \"callLine\": 57, \"id\": \"graveyard_productivity\", \"previous\": \"graveyard_automation\", \"additional\": [\"war_effort\"], \"tier\": 12, \"name\": \"Graveyard · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"graveyard\", \"requires\": [\"graveyard\", \"graveyard_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": [], \"hidden\": true}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T11Graveyard.cs:57`
