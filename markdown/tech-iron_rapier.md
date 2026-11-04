# Iron Rapier

A nimble blade designed for dueling. Its decorative bone crossguard is reinforced to protect the wielder's hand.

## Research effect

A nimble blade designed for dueling. Its decorative bone crossguard is reinforced to protect the wielder's hand.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | iron_rapier |
| Type | Recipe |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Blacksmith](tech-blacksmith.md) |
| [Harvest Bone](tech-forest_bone.md) |
| [Harvest Resin](tech-forest_resin.md) |

## Related item

| Item |
| --- |
| [Iron Rapier](item-iron_rapier.md) |

## Related recipe

| Recipe |
| --- |
| [Iron Rapier](recipe-iron_rapier.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"blacksmith\"",
  "IconName": "\"Icons2_36\"",
  "CostTier": "4",
  "AdditionalRequirements": "new List<string> { \"forest_bone\", \"forest_resin\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:90`
- `Assets.Source.Player/TechNode.cs:1`
