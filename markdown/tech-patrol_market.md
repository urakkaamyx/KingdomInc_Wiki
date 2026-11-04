# Patrol the Market

The market square in Yensburg is visited by thousands every week - and crime is rife. Help out the city guard by patrolling the market for pickpockets and other petty criminals.

## Research effect

The market square in Yensburg is visited by thousands every week - and crime is rife. Help out the city guard by patrolling the market for pickpockets and other petty criminals.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | patrol_market |
| Type | Quest |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Quest Board](tech-quest_board.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Quest",
  "Root": "\"quest_board\"",
  "IconName": "\"Icons_146\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5QuestBoard.cs:109`
- `Assets.Source.Player/TechNode.cs:1`
