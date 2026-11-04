# Leaden Band

The ring's magic slowly burrows into the wearer's skin, weaving impenetrable fibers into their very being.

## Research effect

The ring's magic slowly burrows into the wearer's skin, weaving impenetrable fibers into their very being.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | ring_of_armor_2 |
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
| [Leaden Band](item-ring_of_armor_2.md) |

## Related recipe

| Recipe |
| --- |
| [Leaden Band](recipe-ring_of_armor_2.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"jeweler\"",
  "IconName": "\"Icons2_211\"",
  "AdditionalRequirements": "new List<string> { \"dungeon_temple\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8Jeweler.cs:114`
- `Assets.Source.Player/TechNode.cs:1`
