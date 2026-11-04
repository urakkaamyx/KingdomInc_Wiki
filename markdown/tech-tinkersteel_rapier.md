# Tinkersteel Rapier

The impossibly light blade darts through the air as if it's teleporting, slicing through its victims without slowing down.

## Research effect

The impossibly light blade darts through the air as if it's teleporting, slicing through its victims without slowing down.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | tinkersteel_rapier |
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
| [Tinkersteel Rapier](item-tinkersteel_rapier.md) |

## Related recipe

| Recipe |
| --- |
| [Tinkersteel Rapier](recipe-tinkersteel_rapier.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"blacksmith\"",
  "IconName": "\"Icons3_21\"",
  "CostTier": "10",
  "AdditionalRequirements": "new List<string> { \"inventor\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:186`
- `Assets.Source.Player/TechNode.cs:1`
