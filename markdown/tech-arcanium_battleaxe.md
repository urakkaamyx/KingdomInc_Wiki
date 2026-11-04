# Arcanite Cleaver

For the mighty warrior that wants to fell trees and foes at the same time.

## Research effect

For the mighty warrior that wants to fell trees and foes at the same time.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | arcanium_battleaxe |
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
| [Arcanite Cleaver](item-arcanium_battleaxe.md) |

## Related recipe

| Recipe |
| --- |
| [Arcanite Cleaver](recipe-arcanium_battleaxe.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"blacksmith\"",
  "IconName": "\"Icons2_15\"",
  "CostTier": "6",
  "AdditionalRequirements": "new List<string> { \"arcanium_ingot\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:146`
- `Assets.Source.Player/TechNode.cs:1`
