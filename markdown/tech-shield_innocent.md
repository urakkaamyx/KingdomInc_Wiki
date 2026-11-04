# Shield of the Innocent

The brewing war in the East has displaced many people, driving them towards Yensburg while being chased by marauding orcs. Defend the fleeing refugees and make sure they are safe from harm.

## Research effect

The brewing war in the East has displaced many people, driving them towards Yensburg while being chased by marauding orcs. Defend the fleeing refugees and make sure they are safe from harm.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | shield_innocent |
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
  "IconName": "\"Icons2_113\"",
  "CostTier": "6",
  "AdditionalRequirements": "new List<string> { \"war_effort_east\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5QuestBoard.cs:147`
- `Assets.Source.Player/TechNode.cs:1`
