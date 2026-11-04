# Summon Cherub

Summon Cherub is a tier 11 recipe research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | summon_cherub |
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
| [Summon Cherub](recipe-summon_cherub.md) |

<details><summary>Implementation fields</summary>

```json
{
  "Description": "\"@cherub_desc\"",
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"summoning_circle\"",
  "IconName": "\"Icons2_163\"",
  "CostTier": "11",
  "CostCurrency": "CurrencyCollection.GoldFaith",
  "CostMultiplier": "0.5",
  "AdditionalRequirements": "new List<string> { \"shrine\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8SummoningCircle.cs:44`
- `Assets.Source.Player/TechNode.cs:1`
