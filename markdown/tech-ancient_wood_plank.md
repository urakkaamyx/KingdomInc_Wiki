# Ancient Wood Plank

Sawn from a titanic tree, ready to be processed into a variety of resilient wooden components.

## Research effect

Sawn from a titanic tree, ready to be processed into a variety of resilient wooden components.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | ancient_wood_plank |
| Type | Recipe |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Carpenter](tech-carpenter.md) |
| [Harvest Ancient Wood](tech-forest_ancient_wood.md) |

## Related item

| Item |
| --- |
| [Ancient Wood Plank](item-ancient_wood_plank.md) |

## Related recipe

| Recipe |
| --- |
| [Ancient Wood Plank](recipe-ancient_wood_plank.md) |

## Leads to

| Research |
| --- |
| [Ancient Wood Staff](tech-ancient_wood_staff.md) |
| [Ancient Wood Longbow](tech-ancient_wood_bow.md) |
| [Bulwark of Ancients](tech-ancient_shield.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"carpenter\"",
  "CostTier": "6",
  "AdditionalRequirements": "new List<string> { \"forest_ancient_wood\" }",
  "IconName": "\"Icons2_11\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Carpenter.cs:69`
- `Assets.Source.Player/TechNode.cs:1`
