# Arcanite Blade

The magical properties of this sword cause its edge to always stay razor-sharp.

## Research effect

The magical properties of this sword cause its edge to always stay razor-sharp.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | arcanium_sword |
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
| [Arcanite Blade](item-arcanium_sword.md) |

## Related recipe

| Recipe |
| --- |
| [Arcanite Blade](recipe-arcanium_sword.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"blacksmith\"",
  "IconName": "\"Icons2_12\"",
  "CostTier": "6",
  "AdditionalRequirements": "new List<string> { \"arcanium_ingot\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:122`
- `Assets.Source.Player/TechNode.cs:1`
