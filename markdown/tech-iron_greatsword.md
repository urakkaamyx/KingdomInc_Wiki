# Iron Greatsword

A huge blade that still feels surprisingly maneuverable in the right hands.

## Research effect

A huge blade that still feels surprisingly maneuverable in the right hands.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | iron_greatsword |
| Type | Recipe |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Blacksmith](tech-blacksmith.md) |
| [Rough String](tech-rough_string.md) |

## Related item

| Item |
| --- |
| [Iron Greatsword](item-iron_greatsword.md) |

## Related recipe

| Recipe |
| --- |
| [Iron Greatsword](recipe-iron_greatsword.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"blacksmith\"",
  "CostTier": "2",
  "IconName": "\"Icons_54\"",
  "AdditionalRequirements": "new List<string> { \"rough_string\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:50`
- `Assets.Source.Player/TechNode.cs:1`
