# Witch Hood

The living cloth whispers impossible promises and mad prophecies to the wearer.

## Research effect

The living cloth whispers impossible promises and mad prophecies to the wearer.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | witch_hood |
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
| [Witch Hood](item-witch_hood.md) |

## Related recipe

| Recipe |
| --- |
| [Witch Hood](recipe-witch_hood.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"tailor\"",
  "IconName": "\"Icons3_9\"",
  "CostTier": "10",
  "AdditionalRequirements": "new List<string> { \"inventor\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Tailor.cs:77`
- `Assets.Source.Player/TechNode.cs:1`
