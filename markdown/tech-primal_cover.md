# Primal Cover

The shimmering surface of this armor serves to obscure the wearer's movements.

## Research effect

The shimmering surface of this armor serves to obscure the wearer's movements.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | primal_cover |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Leatherworker](tech-leatherworker.md) |
| [Inventor](tech-inventor.md) |

## Related item

| Item |
| --- |
| [Primal Cover](item-primal_cover.md) |

## Related recipe

| Recipe |
| --- |
| [Primal Cover](recipe-primal_cover.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"leatherworker\"",
  "IconName": "\"Icons3_7\"",
  "CostTier": "10",
  "AdditionalRequirements": "new List<string> { \"inventor\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Leatherworker.cs:78`
- `Assets.Source.Player/TechNode.cs:1`
