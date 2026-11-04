# Assassin's Goggles

Automatically highlights the target's weakspots for the wearer.

A character can only benefit from a single source of Critical Hit.

## Research effect

Automatically highlights the target's weakspots for the wearer.

A character can only benefit from a single source of Critical Hit.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | crit_goggles |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Inventor](tech-inventor.md) |

## Related item

| Item |
| --- |
| [Assassin's Goggles](item-crit_goggles.md) |

## Related recipe

| Recipe |
| --- |
| [Assassin's Goggles](recipe-crit_goggles.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"inventor\"",
  "IconName": "\"Icons3_56\"",
  "CostCurrency": "CurrencyCollection.GoldIngenuity"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Inventor.cs:135`
- `Assets.Source.Player/TechNode.cs:1`
