# Explorer

Unlocks a new Upgrade for your Quest Board.

Increases the Quality of quest reward items by {0}.

## Research effect

Unlocks a new Upgrade for your Quest Board.

Increases the Quality of quest reward items by {0}.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | quest_board_quality |
| Type | Upgrade Slot |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Quest Board](tech-quest_board.md) |
| [Guild Infrastructure](tech-quest_board_automation_2.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.UpgradeSlot",
  "Previous": "\"quest_board_automation_2\"",
  "RelativePosition": "new Vector2Int(0, 180)",
  "Description": "Translation.TranslateOnly(\"@quest_board_quality_desc\", GameMath.FormatPercentage(0.10000000149011612))",
  "IconName": "\"Icons_118\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddAvailableFlowUpgrade(\"QuestBoard\", \"QuestItemLoot\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5QuestBoard.cs:42`
- `Assets.Source.Player/TechNode.cs:1`
