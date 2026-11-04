# Byrgenwald Expedition

The vast woods south of Yensburg have never been fully safe, but recently even travel over the Imperial Road has been fraught with danger. Drive off the wild creatures that threaten passage through the forest.

## Research effect

The vast woods south of Yensburg have never been fully safe, but recently even travel over the Imperial Road has been fraught with danger. Drive off the wild creatures that threaten passage through the forest.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | byrgenwald_expedition |
| Type | Quest |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Quest Board](tech-quest_board.md) |
| [Alchemist](tech-alchemist.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Quest",
  "Root": "\"quest_board\"",
  "IconName": "\"Icons_123\"",
  "CostTier": "9",
  "AdditionalRequirements": "new List<string> { \"alchemist\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5QuestBoard.cs:171`
- `Assets.Source.Player/TechNode.cs:1`
