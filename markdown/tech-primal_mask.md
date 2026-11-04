# Primal Mask

Donning this mask for a prolonged period of time slowly drives the wearer mad with bloodlust.

## Research effect

Donning this mask for a prolonged period of time slowly drives the wearer mad with bloodlust.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | primal_mask |
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
| [Primal Mask](item-primal_mask.md) |

## Related recipe

| Recipe |
| --- |
| [Primal Mask](recipe-primal_mask.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"leatherworker\"",
  "IconName": "\"Icons3_5\"",
  "CostTier": "10",
  "AdditionalRequirements": "new List<string> { \"inventor\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Leatherworker.cs:86`
- `Assets.Source.Player/TechNode.cs:1`
