# Serpentine Band

The living metal slithers around the wearer's finger as it sucks their blood for sustenance.

## Research effect

The living metal slithers around the wearer's finger as it sucks their blood for sustenance.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | ring_of_dexterity_2 |
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
| [Serpentine Band](item-ring_of_dexterity_2.md) |

## Related recipe

| Recipe |
| --- |
| [Serpentine Band](recipe-ring_of_dexterity_2.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"jeweler\"",
  "IconName": "\"Icons2_207\"",
  "AdditionalRequirements": "new List<string> { \"dungeon_temple\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8Jeweler.cs:86`
- `Assets.Source.Player/TechNode.cs:1`
