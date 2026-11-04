# Band of the Cyclops

The unblinking eye that adorns this ring stares back at the wearer incessantly.

## Research effect

The unblinking eye that adorns this ring stares back at the wearer incessantly.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | ring_of_strength_2 |
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
| [Band of the Cyclops](item-ring_of_strength_2.md) |

## Related recipe

| Recipe |
| --- |
| [Band of the Cyclops](recipe-ring_of_strength_2.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"jeweler\"",
  "IconName": "\"Icons2_206\"",
  "AdditionalRequirements": "new List<string> { \"dungeon_temple\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8Jeweler.cs:79`
- `Assets.Source.Player/TechNode.cs:1`
