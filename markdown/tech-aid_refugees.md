# Aiding the Refugees

As refugees were driven westward towards Yensburg, they ended up in a refugee camp that has been set up in the city's slums. Send in a team that has experience in dealing with the disease and misery that reign there.

## Research effect

As refugees were driven westward towards Yensburg, they ended up in a refugee camp that has been set up in the city's slums. Send in a team that has experience in dealing with the disease and misery that reign there.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | aid_refugees |
| Type | Quest |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Quest Board](tech-quest_board.md) |
| [War: Eastern Front](tech-war_effort_east.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Quest",
  "Root": "\"quest_board\"",
  "IconName": "\"Icons2_109\"",
  "CostTier": "6",
  "AdditionalRequirements": "new List<string> { \"war_effort_east\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5QuestBoard.cs:203`
- `Assets.Source.Player/TechNode.cs:1`
