# Arcanite Casque

A helmet fit for a champion.

## Research effect

A helmet fit for a champion.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | arcanium_helm |
| Type | Recipe |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Blacksmith](tech-blacksmith.md) |
| [Arcanite Ingot](tech-arcanium_ingot.md) |

## Related item

| Item |
| --- |
| [Arcanite Casque](item-arcanium_helm.md) |

## Related recipe

| Recipe |
| --- |
| [Arcanite Casque](recipe-arcanium_helm.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"blacksmith\"",
  "IconName": "\"Icons2_16\"",
  "CostTier": "6",
  "AdditionalRequirements": "new List<string> { \"arcanium_ingot\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:114`
- `Assets.Source.Player/TechNode.cs:1`
