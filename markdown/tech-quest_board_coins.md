# Negotiator

Unlocks a new Upgrade for your Quest Board.

Increases all currency gained from quests by {0}.

## Research effect

Unlocks a new Upgrade for your Quest Board.

Increases all currency gained from quests by {0}.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | quest_board_coins |
| Type | Upgrade Slot |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Quest Board](tech-quest_board.md) |
| [Quest Receptionist](tech-quest_board_automation.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.UpgradeSlot",
  "Previous": "\"quest_board_automation\"",
  "RelativePosition": "new Vector2Int(0, 180)",
  "Description": "Translation.TranslateOnly(\"@quest_board_coins_desc\", GameMath.FormatPercentage(0.10000000149011612))",
  "CostCurrency": "CurrencyCollection.GoldRing",
  "IconName": "\"Icons_119\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddAvailableFlowUpgrade(\"QuestBoard\", \"QuestCoinLoot\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5QuestBoard.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
