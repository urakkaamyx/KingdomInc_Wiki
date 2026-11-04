# Ceremonial Sword

Not a suitable combat weapon as-is, but its brilliant shine will surely draw attention.

## Research effect

Not a suitable combat weapon as-is, but its brilliant shine will surely draw attention.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | gold_sword |
| Type | Recipe |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Blacksmith](tech-blacksmith.md) |
| [Gold Ingot](tech-gold_ingot.md) |

## Related item

| Item |
| --- |
| [Ceremonial Sword](item-gold_sword.md) |

## Related recipe

| Recipe |
| --- |
| [Ceremonial Sword](recipe-gold_sword.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"blacksmith\"",
  "IconName": "\"Icons_106\"",
  "CostTier": "3",
  "AdditionalRequirements": "new List<string> { \"gold_ingot\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:66`
- `Assets.Source.Player/TechNode.cs:1`
