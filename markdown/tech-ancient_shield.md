# Bulwark of Ancients

An impenetrable shield to protect the innocent and smite the villainous.

## Research effect

An impenetrable shield to protect the innocent and smite the villainous.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | ancient_shield |
| Type | Recipe |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Carpenter](tech-carpenter.md) |
| [Ancient Wood Plank](tech-ancient_wood_plank.md) |

## Related item

| Item |
| --- |
| [Bulwark of Ancients](item-ancient_shield.md) |

## Related recipe

| Recipe |
| --- |
| [Bulwark of Ancients](recipe-ancient_shield.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"carpenter\"",
  "CostTier": "6",
  "AdditionalRequirements": "new List<string> { \"ancient_wood_plank\" }",
  "IconName": "\"Icons2_25\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Carpenter.cs:93`
- `Assets.Source.Player/TechNode.cs:1`
