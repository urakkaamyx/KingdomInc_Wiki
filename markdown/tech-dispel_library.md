# Decursing the Library

The Grand Library of Yensburg has been overtaken by enchanted books. Dispel the ancient magic that animates the books and reclaim access to the library.

## Research effect

The Grand Library of Yensburg has been overtaken by enchanted books. Dispel the ancient magic that animates the books and reclaim access to the library.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | dispel_library |
| Type | Quest |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Quest Board](tech-quest_board.md) |
| [Enchanter](tech-enchanter.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Quest",
  "Root": "\"quest_board\"",
  "IconName": "\"Icons_164\"",
  "AdditionalRequirements": "new List<string> { \"enchanter\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5QuestBoard.cs:133`
- `Assets.Source.Player/TechNode.cs:1`
