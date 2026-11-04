# Nightmare Casing

A hideously complex mago-tech invention, designed to constrain and direct the concentrated power of nightmare.

## Research effect

A hideously complex mago-tech invention, designed to constrain and direct the concentrated power of nightmare.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | nightmare_casing |
| Type | Recipe |
| Cost tier | 12 |

## Prerequisites

| Required research |
| --- |
| [Blacksmith](tech-blacksmith.md) |
| [Nightmare Distiller](tech-nightmare_distiller.md) |

## Related item

| Item |
| --- |
| [Nightmare Casing](item-nightmare_casing.md) |

## Related recipe

| Recipe |
| --- |
| [Nightmare Casing](recipe-nightmare_casing.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"blacksmith\"",
  "IconName": "\"Icons3_89\"",
  "AdditionalRequirements": "new List<string> { \"nightmare_distiller\" }",
  "CostTier": "12"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:210`
- `Assets.Source.Player/TechNode.cs:1`
