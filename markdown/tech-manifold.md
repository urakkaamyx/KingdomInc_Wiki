# Manifold

Combines up to four I/O pairs for maximum flexibility and throughput, prioritizing from the top.

## Research effect

Combines up to four I/O pairs for maximum flexibility and throughput, prioritizing from the top.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | manifold |
| Type | Flow Element |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Forest](tech-forest.md) |

## Leads to

| Research |
| --- |
| [Build Menu Search](tech-buy_menu_search.md) |
| [Stockpile](tech-stockpile.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"forest\"",
  "RelativePosition": "new Vector2Int(450, 17)",
  "IconName": "\"Icons_104\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T4Forest.cs:172`
- `Assets.Source.Player/TechNode.cs:1`
