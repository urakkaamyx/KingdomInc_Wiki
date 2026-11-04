# Extinguish the Ritual

Spies in Yensburg have discovered a network of occult rituals being carried out in the dark places of the city. Send in someone with knowledge of the occult to put a stop to these blasphemous practices.

## Research effect

Spies in Yensburg have discovered a network of occult rituals being carried out in the dark places of the city. Send in someone with knowledge of the occult to put a stop to these blasphemous practices.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | extinguish_ritual |
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
  "IconName": "\"Icons2_107\"",
  "CostTier": "9",
  "AdditionalRequirements": "new List<string> { \"alchemist\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5QuestBoard.cs:195`
- `Assets.Source.Player/TechNode.cs:1`
