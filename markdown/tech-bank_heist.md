# Bank "Heist"

The Central Bank of Yensburg holds a vast number of gold and silver bars that technically belong to you, but withdrawing them would mean years of paperwork. Thankfully, there's an easier way of getting your hands on them.

## Research effect

The Central Bank of Yensburg holds a vast number of gold and silver bars that technically belong to you, but withdrawing them would mean years of paperwork. Thankfully, there's an easier way of getting your hands on them.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | bank_heist |
| Type | Quest |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Quest Board](tech-quest_board.md) |
| [Dungeon](tech-dungeon.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Quest",
  "Root": "\"quest_board\"",
  "IconName": "\"Icons_204\"",
  "CostTier": "8",
  "AdditionalRequirements": "new List<string> { \"dungeon\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5QuestBoard.cs:163`
- `Assets.Source.Player/TechNode.cs:1`
