# Cotton Cloth

A fine woven sheet of cotton fiber, ready to be processed into clothing.

## Research effect

A fine woven sheet of cotton fiber, ready to be processed into clothing.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | cotton_cloth |
| Type | Recipe |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Tailor](tech-tailor.md) |
| [Cotton Cultivation](tech-farm_cotton.md) |

## Related item

| Item |
| --- |
| [Cotton Cloth](item-cotton_cloth.md) |

## Related recipe

| Recipe |
| --- |
| [Cotton Cloth](recipe-cotton_cloth.md) |

## Leads to

| Research |
| --- |
| [Enchanted Thread](tech-enchanted_cotton_thread.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"tailor\"",
  "AdditionalRequirements": "new List<string> { \"farm_cotton\" }",
  "IconName": "\"Icons2_31\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Tailor.cs:46`
- `Assets.Source.Player/TechNode.cs:1`
