# Forge Attendant

Unlocks the first Upgrade slot for your Forges.

Unlocks the Worker upgrade to automate ore smelting.

## Research effect

Unlocks the first Upgrade slot for your Forges.

Unlocks the Worker upgrade to automate ore smelting.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | forge_automation |
| Type | Upgrade Slot |
| Cost tier | 1 |

## Prerequisites

| Required research |
| --- |
| [Forge](tech-forge.md) |

## Leads to

| Research |
| --- |
| [Forge · second add-on slot](tech-forge_automation_2.md) |
| [Forge · overseers](tech-forge_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Forge\", \"callSource\": \"source/Assets.Source.Player.Tech/T1Forge.cs\", \"callLine\": 41, \"id\": \"forge_automation\", \"root\": \"forge\", \"tier\": 1, \"name\": \"Forge Attendant\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"forge\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T1Forge.cs:41`
