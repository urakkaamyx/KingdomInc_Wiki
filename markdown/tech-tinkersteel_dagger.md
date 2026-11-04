# Tinkersteel Dagger

A nimble, telescopic blade. The blade extends after puncturing the target, causing extensive internal damage.

## Research effect

A nimble, telescopic blade. The blade extends after puncturing the target, causing extensive internal damage.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | tinkersteel_dagger |
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
| [Tinkersteel Dagger](item-tinkersteel_dagger.md) |

## Related recipe

| Recipe |
| --- |
| [Tinkersteel Dagger](recipe-tinkersteel_dagger.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"blacksmith\"",
  "IconName": "\"Icons3_17\"",
  "CostTier": "10",
  "AdditionalRequirements": "new List<string> { \"inventor\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:178`
- `Assets.Source.Player/TechNode.cs:1`
