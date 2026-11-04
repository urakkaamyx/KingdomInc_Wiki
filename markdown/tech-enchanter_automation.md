# Leyline Guide

Unlocks the first Upgrade slot for your Enchanters.

Unlocks the Worker upgrade to automatically manipulate mana.

## Research effect

Unlocks the first Upgrade slot for your Enchanters.

Unlocks the Worker upgrade to automatically manipulate mana.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | enchanter_automation |
| Type | Upgrade Slot |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Enchanter](tech-enchanter.md) |

## Leads to

| Research |
| --- |
| [Enchanter · second add-on slot](tech-enchanter_automation_2.md) |
| [Enchanter · overseers](tech-enchanter_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Enchanter\", \"callSource\": \"source/Assets.Source.Player.Tech/T6Enchanter.cs\", \"callLine\": 29, \"id\": \"enchanter_automation\", \"root\": \"enchanter\", \"tier\": 6, \"name\": \"Leyline Guide\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"enchanter\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T6Enchanter.cs:29`
