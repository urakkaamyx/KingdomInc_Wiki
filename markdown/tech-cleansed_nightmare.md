# Cleansed Nightmare

The toxic negative energy has been purified by the grace of Saint Ilonia. By Her grace, it can be put to a better use.

## Research effect

The toxic negative energy has been purified by the grace of Saint Ilonia. By Her grace, it can be put to a better use.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | cleansed_nightmare |
| Type | Recipe |
| Cost tier | 12 |

## Prerequisites

| Required research |
| --- |
| [Shrine](tech-shrine.md) |
| [Nightmare Distiller](tech-nightmare_distiller.md) |

## Related item

| Item |
| --- |
| [Cleansed Nightmare](item-cleansed_nightmare.md) |

## Related recipe

| Recipe |
| --- |
| [Cleansed Nightmare](recipe-cleansed_nightmare.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"shrine\"",
  "IconName": "\"Icons3_90\"",
  "AdditionalRequirements": "new List<string> { \"nightmare_distiller\" }",
  "CostTier": "12"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:191`
- `Assets.Source.Player/TechNode.cs:1`
