# Farmstead Liberator

Gangs of orcs and other marauders have occupied much of the farmland that surrounds Yensburg, enslaving the farmers and exporting the produce back to their homeland. Eradicate these squatters from your lands.

## Research effect

Gangs of orcs and other marauders have occupied much of the farmland that surrounds Yensburg, enslaving the farmers and exporting the produce back to their homeland. Eradicate these squatters from your lands.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | farmstead_liberator |
| Type | Quest |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Quest Board](tech-quest_board.md) |
| [Farm](tech-farm.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Quest",
  "Root": "\"quest_board\"",
  "IconName": "\"Icons_182\"",
  "CostTier": "7",
  "AdditionalRequirements": "new List<string> { \"farm\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5QuestBoard.cs:155`
- `Assets.Source.Player/TechNode.cs:1`
