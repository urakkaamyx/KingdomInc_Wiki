# Necromancer · second add-on slot

Necromancer · second add-on slot is a tier 12 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | necromancer_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 12 |

## Prerequisites

| Required research |
| --- |
| [Necromancer](tech-necromancer.md) |
| [Novice Necromancer](tech-necromancer_automation.md) |
| [War Effort](tech-war_effort.md) |
| [Dungeon](tech-dungeon.md) |

## Leads to

| Research |
| --- |
| [Necromancer · artisans](tech-necromancer_quality.md) |
| [Necromancer · third add-on slot](tech-necromancer_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Necromancer\", \"callSource\": \"source/Assets.Source.Player.Tech/T11Necromancer.cs\", \"callLine\": 21, \"id\": \"necromancer_automation_2\", \"previous\": \"necromancer_automation\", \"tier\": 12, \"additional\": [\"war_effort\", \"dungeon\"], \"name\": \"Necromancer · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"necromancer\", \"requires\": [\"necromancer\", \"necromancer_automation\", \"war_effort\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T11Necromancer.cs:21`
