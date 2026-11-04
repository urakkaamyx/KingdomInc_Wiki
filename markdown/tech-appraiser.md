# Appraiser

Sorts incoming items and humans by their stats and characteristics.

## Research effect

Sorts incoming items and humans by their stats and characteristics.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | appraiser |
| Type | Flow Element |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Filter](tech-filter.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"filter\"",
  "RelativePosition": "new Vector2Int(-270, 90)",
  "IconName": "\"Icons_148\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5QuestBoard.cs:95`
- `Assets.Source.Player/TechNode.cs:1`
