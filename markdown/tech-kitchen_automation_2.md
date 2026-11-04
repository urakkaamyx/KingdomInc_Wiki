# Kitchen · second add-on slot

Kitchen · second add-on slot is a tier 8 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | kitchen_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Kitchen](tech-kitchen.md) |
| [Sous Chef](tech-kitchen_automation.md) |
| [War Effort](tech-war_effort.md) |
| [Dungeon](tech-dungeon.md) |

## Leads to

| Research |
| --- |
| [Kitchen · artisans](tech-kitchen_quality.md) |
| [Kitchen · third add-on slot](tech-kitchen_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Kitchen\", \"callSource\": \"source/Assets.Source.Player.Tech/T7Kitchen.cs\", \"callLine\": 19, \"id\": \"kitchen_automation_2\", \"previous\": \"kitchen_automation\", \"tier\": 8, \"additional\": [\"war_effort\", \"dungeon\"], \"name\": \"Kitchen · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"kitchen\", \"requires\": [\"kitchen\", \"kitchen_automation\", \"war_effort\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T7Kitchen.cs:19`
