# Simple Prayer

A cleric offers a devout prayer to Saint Ilonia, generating a small amount of faith for your Kingdom.

## Research effect

A cleric offers a devout prayer to Saint Ilonia, generating a small amount of faith for your Kingdom.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | prayer_1 |
| Type | Recipe |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Shrine](tech-shrine.md) |

## Related recipe

| Recipe |
| --- |
| [Simple Prayer](recipe-prayer_1.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"shrine\"",
  "IconName": "\"Icons3_72\"",
  "CostMultiplier": "0.5"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:31`
- `Assets.Source.Player/TechNode.cs:1`
