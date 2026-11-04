# Softwood Bow

The materials used in this bow's construction aren't ideal, but it will do in a pinch.

## Research effect

The materials used in this bow's construction aren't ideal, but it will do in a pinch.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | softwood_bow |
| Type | Recipe |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Carpenter](tech-carpenter.md) |
| [Rough String](tech-rough_string.md) |

## Related item

| Item |
| --- |
| [Softwood Bow](item-softwood_bow.md) |

## Related recipe

| Recipe |
| --- |
| [Softwood Bow](recipe-softwood_bow.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"carpenter\"",
  "IconName": "\"Icons_47\"",
  "AdditionalRequirements": "new List<string> { \"rough_string\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Carpenter.cs:21`
- `Assets.Source.Player/TechNode.cs:1`
