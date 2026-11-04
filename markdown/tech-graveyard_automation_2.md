# Graveyard · second add-on slot

Graveyard · second add-on slot is a tier 12 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | graveyard_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 12 |

## Prerequisites

| Required research |
| --- |
| [Graveyard](tech-graveyard.md) |
| [Gravedigger](tech-graveyard_automation.md) |
| [War Effort](tech-war_effort.md) |
| [Dungeon](tech-dungeon.md) |

## Leads to

| Research |
| --- |
| [Graveyard · artisans](tech-graveyard_quality.md) |
| [Graveyard · third add-on slot](tech-graveyard_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Graveyard\", \"callSource\": \"source/Assets.Source.Player.Tech/T11Graveyard.cs\", \"callLine\": 57, \"id\": \"graveyard_automation_2\", \"previous\": \"graveyard_automation\", \"tier\": 12, \"additional\": [\"war_effort\", \"dungeon\"], \"name\": \"Graveyard · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"graveyard\", \"requires\": [\"graveyard\", \"graveyard_automation\", \"war_effort\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T11Graveyard.cs:57`
