# Gravedigger

Unlocks the first Upgrade slot for your Graveyard.

Unlocks the Worker upgrade to automatically bury the dead.

## Research effect

Unlocks the first Upgrade slot for your Graveyard.

Unlocks the Worker upgrade to automatically bury the dead.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | graveyard_automation |
| Type | Upgrade Slot |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Graveyard](tech-graveyard.md) |

## Leads to

| Research |
| --- |
| [Graveyard · second add-on slot](tech-graveyard_automation_2.md) |
| [Graveyard · overseers](tech-graveyard_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Graveyard\", \"callSource\": \"source/Assets.Source.Player.Tech/T11Graveyard.cs\", \"callLine\": 57, \"id\": \"graveyard_automation\", \"root\": \"graveyard\", \"tier\": 11, \"name\": \"Gravedigger\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"graveyard\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T11Graveyard.cs:57`
