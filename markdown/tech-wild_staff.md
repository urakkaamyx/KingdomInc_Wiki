# Staff of the Wild

A simple staff that serves as a focus for nature-based divine magic.

## Research effect

A simple staff that serves as a focus for nature-based divine magic.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | wild_staff |
| Type | Recipe |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Carpenter](tech-carpenter.md) |
| [Harvest Bone](tech-forest_bone.md) |

## Related item

| Item |
| --- |
| [Staff of the Wild](item-wild_staff.md) |

## Related recipe

| Recipe |
| --- |
| [Staff of the Wild](recipe-wild_staff.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"carpenter\"",
  "CostTier": "4",
  "AdditionalRequirements": "new List<string> { \"forest_bone\" }",
  "IconName": "\"Icons_201\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Carpenter.cs:61`
- `Assets.Source.Player/TechNode.cs:1`
