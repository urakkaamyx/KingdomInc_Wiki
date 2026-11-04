# Accountant

Only allows items to pass through if your currency stockpile meets the set requirements.

## Research effect

Only allows items to pass through if your currency stockpile meets the set requirements.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | accountant |
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
  "RelativePosition": "new Vector2Int(-270, -90)",
  "IconName": "\"Icons_149\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5QuestBoard.cs:102`
- `Assets.Source.Player/TechNode.cs:1`
