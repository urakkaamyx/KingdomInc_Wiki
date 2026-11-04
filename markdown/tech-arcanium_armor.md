# Arcanite Chestguard

If you're going into battle, you might as well do it in style.

## Research effect

If you're going into battle, you might as well do it in style.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | arcanium_armor |
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
| [Arcanite Chestguard](item-arcanium_armor.md) |

## Related recipe

| Recipe |
| --- |
| [Arcanite Chestguard](recipe-arcanium_armor.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"blacksmith\"",
  "IconName": "\"Icons2_17\"",
  "CostTier": "6",
  "AdditionalRequirements": "new List<string> { \"arcanium_ingot\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:106`
- `Assets.Source.Player/TechNode.cs:1`
