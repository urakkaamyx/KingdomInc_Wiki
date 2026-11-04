# Novice Necromancer

Unlocks the first Upgrade slot for your Necromancer.

Unlocks the Worker upgrade to automatically awaken the dead.

## Research effect

Unlocks the first Upgrade slot for your Necromancer.

Unlocks the Worker upgrade to automatically awaken the dead.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | necromancer_automation |
| Type | Upgrade Slot |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Necromancer](tech-necromancer.md) |

## Leads to

| Research |
| --- |
| [Necromancer · second add-on slot](tech-necromancer_automation_2.md) |
| [Necromancer · overseers](tech-necromancer_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Necromancer\", \"callSource\": \"source/Assets.Source.Player.Tech/T11Necromancer.cs\", \"callLine\": 21, \"id\": \"necromancer_automation\", \"root\": \"necromancer\", \"tier\": 11, \"name\": \"Novice Necromancer\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"necromancer\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T11Necromancer.cs:21`
