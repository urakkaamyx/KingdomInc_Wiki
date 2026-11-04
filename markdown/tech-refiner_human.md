# Flesh Sculptor

As long as Mana Sculptor is enabled, Refiners can improve the training of Conscripts and Adventurers as well. Success chance is halved compared to regular items.

## Research effect

As long as Mana Sculptor is enabled, Refiners can improve the training of Conscripts and Adventurers as well. Success chance is halved compared to regular items.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | refiner_human |
| Type | Utility |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Metamorphosis](tech-refiner_demon.md) |
| [Necromancer](tech-necromancer.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"refiner_demon\"",
  "RelativePosition": "new Vector2Int(180, 0)",
  "IconName": "\"Icons2_46\"",
  "CostMultiplier": "3.0",
  "CostTier": "11",
  "AdditionalRequirements": "new List<string> { \"necromancer\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T6Enchanter.cs:195`
- `Assets.Source.Player/TechNode.cs:1`
