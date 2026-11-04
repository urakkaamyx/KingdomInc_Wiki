# Ancient Wood Longbow

The flexible-yet-sturdy limbs of this bow allow for both exceptional accuracy and astonishing rapid fire.

## Research effect

The flexible-yet-sturdy limbs of this bow allow for both exceptional accuracy and astonishing rapid fire.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | ancient_wood_bow |
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
| [Ancient Wood Longbow](item-ancient_wood_bow.md) |

## Related recipe

| Recipe |
| --- |
| [Ancient Wood Longbow](recipe-ancient_wood_bow.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"carpenter\"",
  "CostTier": "6",
  "AdditionalRequirements": "new List<string> { \"ancient_wood_plank\" }",
  "IconName": "\"Icons2_24\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Carpenter.cs:85`
- `Assets.Source.Player/TechNode.cs:1`
