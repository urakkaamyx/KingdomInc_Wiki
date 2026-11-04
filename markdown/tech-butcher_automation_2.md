# Butcher · second add-on slot

Butcher · second add-on slot is a tier 8 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | butcher_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Butcher](tech-butcher.md) |
| [The Meat Man](tech-butcher_automation.md) |
| [War Effort](tech-war_effort.md) |
| [Dungeon](tech-dungeon.md) |

## Leads to

| Research |
| --- |
| [Butcher · artisans](tech-butcher_quality.md) |
| [Butcher · third add-on slot](tech-butcher_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Butcher\", \"callSource\": \"source/Assets.Source.Player.Tech/T7Butcher.cs\", \"callLine\": 23, \"id\": \"butcher_automation_2\", \"previous\": \"butcher_automation\", \"tier\": 8, \"additional\": [\"war_effort\", \"dungeon\"], \"name\": \"Butcher · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"butcher\", \"requires\": [\"butcher\", \"butcher_automation\", \"war_effort\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T7Butcher.cs:23`
