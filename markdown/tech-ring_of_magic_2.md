# Monsoon Band

The elemental magic contained in this ring is constantly attempting to break free.

## Research effect

The elemental magic contained in this ring is constantly attempting to break free.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | ring_of_magic_2 |
| Type | Recipe |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Jeweler](tech-jeweler.md) |
| [Temple of the Last Rite](tech-dungeon_temple.md) |

## Related item

| Item |
| --- |
| [Monsoon Band](item-ring_of_magic_2.md) |

## Related recipe

| Recipe |
| --- |
| [Monsoon Band](recipe-ring_of_magic_2.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"jeweler\"",
  "IconName": "\"Icons2_208\"",
  "AdditionalRequirements": "new List<string> { \"dungeon_temple\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8Jeweler.cs:93`
- `Assets.Source.Player/TechNode.cs:1`
