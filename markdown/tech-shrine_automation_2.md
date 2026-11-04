# Shrine · second add-on slot

Shrine · second add-on slot is a tier 12 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | shrine_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 12 |

## Prerequisites

| Required research |
| --- |
| [Shrine](tech-shrine.md) |
| [Prayer Wheel](tech-shrine_automation.md) |
| [War Effort](tech-war_effort.md) |
| [Dungeon](tech-dungeon.md) |

## Leads to

| Research |
| --- |
| [Shrine · artisans](tech-shrine_quality.md) |
| [Shrine · third add-on slot](tech-shrine_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Shrine\", \"callSource\": \"source/Assets.Source.Player.Tech/T11Shrine.cs\", \"callLine\": 26, \"id\": \"shrine_automation_2\", \"previous\": \"shrine_automation\", \"tier\": 12, \"additional\": [\"war_effort\", \"dungeon\"], \"name\": \"Shrine · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"shrine\", \"requires\": [\"shrine\", \"shrine_automation\", \"war_effort\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T11Shrine.cs:26`
