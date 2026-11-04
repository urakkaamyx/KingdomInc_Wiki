# Autodidact

Unlocks a new Upgrade for your Quest Board.

Increases Training gained by adventurers by {0}.

## Research effect

Unlocks a new Upgrade for your Quest Board.

Increases Training gained by adventurers by {0}.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | quest_board_training |
| Type | Upgrade Slot |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Quest Board](tech-quest_board.md) |
| [Decentralized Quest Network](tech-quest_board_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.UpgradeSlot",
  "Previous": "\"quest_board_automation_3\"",
  "RelativePosition": "new Vector2Int(0, 180)",
  "Description": "Translation.TranslateOnly(\"@quest_board_training_desc\", GameMath.FormatPercentage(0.5))",
  "IconName": "\"Icons_137\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddAvailableFlowUpgrade(\"QuestBoard\", \"QuestTraining\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5QuestBoard.cs:55`
- `Assets.Source.Player/TechNode.cs:1`
