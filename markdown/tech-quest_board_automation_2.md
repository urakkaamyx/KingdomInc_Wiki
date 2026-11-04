# Quest Board · second add-on slot

Quest Board · second add-on slot is a tier 6 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | quest_board_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Quest Board](tech-quest_board.md) |
| [Quest Receptionist](tech-quest_board_automation.md) |
| [War Effort](tech-war_effort.md) |

## Leads to

| Research |
| --- |
| [Explorer](tech-quest_board_quality.md) |
| [Quest Board · third add-on slot](tech-quest_board_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"QuestBoard\", \"callSource\": \"source/Assets.Source.Player.Tech/T5QuestBoard.cs\", \"callLine\": 41, \"id\": \"quest_board_automation_2\", \"previous\": \"quest_board_automation\", \"tier\": 6, \"additional\": [\"war_effort\", \"quest_board\"], \"name\": \"Quest Board · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"quest_board\", \"requires\": [\"quest_board\", \"quest_board_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:41`
