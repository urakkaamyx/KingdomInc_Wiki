# Mine Sweep

The network of mine tunnels that supply most of Yensburg's raw iron ore have been overrun by kobolds, causing significant supply bottlenecks. Clear out the vermin and restore access to a greater stockpile of iron.

## Research effect

The network of mine tunnels that supply most of Yensburg's raw iron ore have been overrun by kobolds, causing significant supply bottlenecks. Clear out the vermin and restore access to a greater stockpile of iron.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | clear_mines |
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
  "IconName": "\"Icons_202\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5QuestBoard.cs:121`
- `Assets.Source.Player/TechNode.cs:1`
