# Elemental Eradication

For generations, the elementals of Midlake have lived in relatively harmony with the surrounding human settlements. Their recent unprovoked aggression calls for them to be culled once and for all.

## Research effect

For generations, the elementals of Midlake have lived in relatively harmony with the surrounding human settlements. Their recent unprovoked aggression calls for them to be culled once and for all.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | elemental_eradication |
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
  "IconName": "\"Icons2_143\"",
  "CostTier": "7",
  "AdditionalRequirements": "new List<string> { \"farm\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5QuestBoard.cs:179`
- `Assets.Source.Player/TechNode.cs:1`
