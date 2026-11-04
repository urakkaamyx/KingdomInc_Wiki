# Summon Arbiter

Summon Arbiter is a tier 11 recipe research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | summon_arbiter |
| Type | Recipe |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Summoning Circle](tech-summoning_circle.md) |
| [Shrine](tech-shrine.md) |

## Related recipe

| Recipe |
| --- |
| [Summon Arbiter](recipe-summon_arbiter.md) |

<details><summary>Implementation fields</summary>

```json
{
  "Description": "\"@arbiter_desc\"",
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"summoning_circle\"",
  "IconName": "\"Icons2_165\"",
  "CostTier": "11",
  "CostCurrency": "CurrencyCollection.GoldFaith",
  "AdditionalRequirements": "new List<string> { \"shrine\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8SummoningCircle.cs:66`
- `Assets.Source.Player/TechNode.cs:1`
