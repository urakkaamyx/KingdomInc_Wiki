# Metamorphosis

As long as Mana Sculptor is enabled, Refiners can now also improve the quality of creatures summoned by the Summoning Circle.

## Research effect

As long as Mana Sculptor is enabled, Refiners can now also improve the quality of creatures summoned by the Summoning Circle.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | refiner_demon |
| Type | Utility |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Mana Sculptor](tech-refiner_mana.md) |
| [Summoning Circle](tech-summoning_circle.md) |

## Leads to

| Research |
| --- |
| [Flesh Sculptor](tech-refiner_human.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"refiner_mana\"",
  "RelativePosition": "new Vector2Int(180, 0)",
  "IconName": "\"Icons2_47\"",
  "CostMultiplier": "3.0",
  "CostTier": "8",
  "AdditionalRequirements": "new List<string> { \"summoning_circle\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T6Enchanter.cs:185`
- `Assets.Source.Player/TechNode.cs:1`
