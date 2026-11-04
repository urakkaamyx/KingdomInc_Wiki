# Hoard

A place to store loot collected from dungeons and quests. No storage fee. All hoards are linked and contents can be accessed from anywhere.

## Research effect

A place to store loot collected from dungeons and quests. No storage fee. All hoards are linked and contents can be accessed from anywhere.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | hoard |
| Type | Flow Element |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Temple of the Last Rite](tech-dungeon_temple.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"dungeon_temple\"",
  "RelativePosition": "new Vector2Int(270, 0)",
  "IconName": "\"Icons2_65\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T9Arena.cs:76`
- `Assets.Source.Player/TechNode.cs:1`
