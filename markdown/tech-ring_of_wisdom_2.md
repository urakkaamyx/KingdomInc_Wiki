# Band of Tranquility

The ring constantly sheds tiny seeds that drift off on the wind and sprout alien flowers in the countryside.

## Research effect

The ring constantly sheds tiny seeds that drift off on the wind and sprout alien flowers in the countryside.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | ring_of_wisdom_2 |
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
| [Band of Tranquility](item-ring_of_wisdom_2.md) |

## Related recipe

| Recipe |
| --- |
| [Band of Tranquility](recipe-ring_of_wisdom_2.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"jeweler\"",
  "IconName": "\"Icons2_209\"",
  "AdditionalRequirements": "new List<string> { \"dungeon_temple\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8Jeweler.cs:100`
- `Assets.Source.Player/TechNode.cs:1`
