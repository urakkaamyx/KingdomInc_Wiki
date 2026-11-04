# Tinkersteel Armor

The mago-tech folded into this armor serve to deflect blows and dampen impacts.

## Research effect

The mago-tech folded into this armor serve to deflect blows and dampen impacts.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | tinkersteel_armor |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Blacksmith](tech-blacksmith.md) |
| [Inventor](tech-inventor.md) |

## Related item

| Item |
| --- |
| [Tinkersteel Armor](item-tinkersteel_armor.md) |

## Related recipe

| Recipe |
| --- |
| [Tinkersteel Armor](recipe-tinkersteel_armor.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"blacksmith\"",
  "IconName": "\"Icons3_3\"",
  "CostTier": "10",
  "AdditionalRequirements": "new List<string> { \"inventor\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:154`
- `Assets.Source.Player/TechNode.cs:1`
