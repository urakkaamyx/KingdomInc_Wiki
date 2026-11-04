# Rough Leather

Processed skin of a dead animal with surprisingly many use cases.

## Research effect

Processed skin of a dead animal with surprisingly many use cases.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | rough_leather |
| Type | Recipe |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Leatherworker](tech-leatherworker.md) |
| [Forest](tech-forest.md) |

## Related item

| Item |
| --- |
| [Rough Leather](item-rough_leather.md) |

## Related recipe

| Recipe |
| --- |
| [Rough Leather](recipe-rough_leather.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"leatherworker\"",
  "IconName": "\"Icons_39\"",
  "AdditionalRequirements": "new List<string> { \"forest\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Leatherworker.cs:39`
- `Assets.Source.Player/TechNode.cs:1`
