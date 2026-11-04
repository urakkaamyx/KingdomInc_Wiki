# Undying Band

The hungry ring slowly binds itself to the wearer's soul until the two are inseperable.

## Research effect

The hungry ring slowly binds itself to the wearer's soul until the two are inseperable.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | ring_of_health_2 |
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
| [Undying Band](item-ring_of_health_2.md) |

## Related recipe

| Recipe |
| --- |
| [Undying Band](recipe-ring_of_health_2.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"jeweler\"",
  "IconName": "\"Icons2_210\"",
  "AdditionalRequirements": "new List<string> { \"dungeon_temple\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8Jeweler.cs:107`
- `Assets.Source.Player/TechNode.cs:1`
