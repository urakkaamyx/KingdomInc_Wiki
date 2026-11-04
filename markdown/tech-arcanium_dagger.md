# Arcanite Backstabber

Its thin blade easily passes through even the sturdiest armor without snapping.

## Research effect

Its thin blade easily passes through even the sturdiest armor without snapping.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | arcanium_dagger |
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
| [Arcanite Backstabber](item-arcanium_dagger.md) |

## Related recipe

| Recipe |
| --- |
| [Arcanite Backstabber](recipe-arcanium_dagger.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"blacksmith\"",
  "IconName": "\"Icons2_14\"",
  "CostTier": "6",
  "AdditionalRequirements": "new List<string> { \"arcanium_ingot\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:130`
- `Assets.Source.Player/TechNode.cs:1`
