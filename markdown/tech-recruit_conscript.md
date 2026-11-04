# Recruit Conscripts

Provides a steady supply of Conscripts to fight the enemies of Yensburg.

## Research effect

Provides a steady supply of Conscripts to fight the enemies of Yensburg.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | recruit_conscript |
| Type | Resource |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Barracks](tech-barracks.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Resource",
  "Root": "\"barracks\"",
  "IconName": "\"Icons_61\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3Barracks.cs:27`
- `Assets.Source.Player/TechNode.cs:1`
