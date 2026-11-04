# Witch Robe

An unworthy wearer will slowly have their soul siphoned away by the living fabric until nothing is left.

## Research effect

An unworthy wearer will slowly have their soul siphoned away by the living fabric until nothing is left.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | witch_robe |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Tailor](tech-tailor.md) |
| [Inventor](tech-inventor.md) |

## Related item

| Item |
| --- |
| [Witch Robe](item-witch_robe.md) |

## Related recipe

| Recipe |
| --- |
| [Witch Robe](recipe-witch_robe.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"tailor\"",
  "IconName": "\"Icons3_11\"",
  "CostTier": "10",
  "AdditionalRequirements": "new List<string> { \"inventor\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Tailor.cs:69`
- `Assets.Source.Player/TechNode.cs:1`
