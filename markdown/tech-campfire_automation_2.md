# Campfire · second add-on slot

Campfire · second add-on slot is a tier 5 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | campfire_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Campfire](tech-campfire.md) |
| [Wilderness Cookery](tech-campfire_automation.md) |
| [War Effort](tech-war_effort.md) |
| [Quest Board](tech-quest_board.md) |

## Leads to

| Research |
| --- |
| [Campfire · artisans](tech-campfire_quality.md) |
| [Campfire · third add-on slot](tech-campfire_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Campfire\", \"callSource\": \"source/Assets.Source.Player.Tech/T4Campfire.cs\", \"callLine\": 56, \"id\": \"campfire_automation_2\", \"previous\": \"campfire_automation\", \"tier\": 5, \"additional\": [\"war_effort\", \"quest_board\"], \"name\": \"Campfire · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"campfire\", \"requires\": [\"campfire\", \"campfire_automation\", \"war_effort\", \"quest_board\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T4Campfire.cs:56`
