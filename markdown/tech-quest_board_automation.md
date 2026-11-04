# Quest Receptionist

Unlocks the first Upgrade slot for your Quest Board.

Unlocks the Worker upgrade to automatically dispatch adventurers.

## Research effect

Unlocks the first Upgrade slot for your Quest Board.

Unlocks the Worker upgrade to automatically dispatch adventurers.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | quest_board_automation |
| Type | Upgrade Slot |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Quest Board](tech-quest_board.md) |

## Leads to

| Research |
| --- |
| [Negotiator](tech-quest_board_coins.md) |
| [Quest Board · second add-on slot](tech-quest_board_automation_2.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"QuestBoard\", \"callSource\": \"source/Assets.Source.Player.Tech/T5QuestBoard.cs\", \"callLine\": 27, \"id\": \"quest_board_automation\", \"root\": \"quest_board\", \"tier\": 5, \"name\": \"Quest Receptionist\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"quest_board\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:27`
