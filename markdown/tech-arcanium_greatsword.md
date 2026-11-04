# Arcanite Claymore

The blade appears clumsy and cumbersome, but is surprisingly versatile in combat.

## Research effect

The blade appears clumsy and cumbersome, but is surprisingly versatile in combat.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | arcanium_greatsword |
| Type | Recipe |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Blacksmith](tech-blacksmith.md) |
| [Arcanite Ingot](tech-arcanium_ingot.md) |

## Related item

| Item |
| --- |
| [Arcanite Claymore](item-arcanium_greatsword.md) |

## Related recipe

| Recipe |
| --- |
| [Arcanite Claymore](recipe-arcanium_greatsword.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"blacksmith\"",
  "IconName": "\"Icons2_13\"",
  "CostTier": "6",
  "AdditionalRequirements": "new List<string> { \"arcanium_ingot\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:138`
- `Assets.Source.Player/TechNode.cs:1`
