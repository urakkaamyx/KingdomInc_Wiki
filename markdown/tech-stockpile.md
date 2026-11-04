# Stockpile

Buffers up to 10 items to smooth out bumps in supply and demand.

## Research effect

Buffers up to 10 items to smooth out bumps in supply and demand.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | stockpile |
| Type | Flow Element |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Manifold](tech-manifold.md) |

## Leads to

| Research |
| --- |
| [Dimensional Storage](tech-stockpile_capacity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"manifold\"",
  "RelativePosition": "new Vector2Int(270, 0)",
  "IconName": "\"Icons_105\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T4Forest.cs:187`
- `Assets.Source.Player/TechNode.cs:1`
