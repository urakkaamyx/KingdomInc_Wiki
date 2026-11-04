# Mine Iron Ore

Provides a steady supply of Iron Ore from your Mine.

## Research effect

Provides a steady supply of Iron Ore from your Mine.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | mine_iron_ore |
| Type | Resource |
| Cost tier | 1 |

## Prerequisites

| Required research |
| --- |
| [Mine](tech-mine.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Resource",
  "Root": "\"mine\"",
  "IconName": "\"Icons_11\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Mine.cs:31`
- `Assets.Source.Player/TechNode.cs:1`
