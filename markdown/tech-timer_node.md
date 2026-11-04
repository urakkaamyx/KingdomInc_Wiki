# Timer

Allows you to pace your workflow by introducing a minimum waiting time.

## Research effect

Allows you to pace your workflow by introducing a minimum waiting time.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | timer_node |
| Type | Flow Element |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Engraver](tech-engraver.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"engraver\"",
  "RelativePosition": "new Vector2Int(-450, 17)",
  "IconName": "\"Icons_75\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3Engraver.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
