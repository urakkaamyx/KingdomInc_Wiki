# Quest Board · third add-on slot

Quest Board · third add-on slot is a tier 7 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | quest_board_automation_3 |
| Type | Upgrade Slot |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Quest Board](tech-quest_board.md) |
| [Guild Infrastructure](tech-quest_board_automation_2.md) |
| [Dungeon](tech-dungeon.md) |

## Leads to

| Research |
| --- |
| [Autodidact](tech-quest_board_training.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 73, \"generated\": true, \"building\": \"QuestBoard\", \"callSource\": \"source/Assets.Source.Player.Tech/T5QuestBoard.cs\", \"callLine\": 54, \"id\": \"quest_board_automation_3\", \"previous\": \"quest_board_automation_2\", \"additional\": [\"dungeon\"], \"tier\": 7, \"name\": \"Quest Board · third add-on slot\", \"icon\": \"Icons2_77\", \"slotCount\": 3, \"root\": \"quest_board\", \"requires\": [\"quest_board\", \"quest_board_automation_2\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:73`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:54`
