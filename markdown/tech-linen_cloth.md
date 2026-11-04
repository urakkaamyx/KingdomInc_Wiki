# Linen Cloth

Coarse and crude, but provides protection from the elements.

## Research effect

Coarse and crude, but provides protection from the elements.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | linen_cloth |
| Type | Recipe |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Tailor](tech-tailor.md) |
| [Flax Cultivation](tech-farm_flax.md) |

## Related item

| Item |
| --- |
| [Linen Cloth](item-linen_cloth.md) |

## Related recipe

| Recipe |
| --- |
| [Linen Cloth](recipe-linen_cloth.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"tailor\"",
  "AdditionalRequirements": "new List<string> { \"farm_flax\" }",
  "IconName": "\"Icons_49\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Tailor.cs:39`
- `Assets.Source.Player/TechNode.cs:1`
