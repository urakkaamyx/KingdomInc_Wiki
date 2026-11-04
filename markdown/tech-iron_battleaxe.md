# Iron Battleaxe

An enormous brute-force weapon made for enormous brute-force warriors.

## Research effect

An enormous brute-force weapon made for enormous brute-force warriors.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | iron_battleaxe |
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
| [Iron Battleaxe](item-iron_battleaxe.md) |

## Related recipe

| Recipe |
| --- |
| [Iron Battleaxe](recipe-iron_battleaxe.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"blacksmith\"",
  "CostTier": "2",
  "IconName": "\"Icons_55\"",
  "AdditionalRequirements": "new List<string> { \"rough_string\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:58`
- `Assets.Source.Player/TechNode.cs:1`
