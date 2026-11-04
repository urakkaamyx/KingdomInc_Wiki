# Elixir of Fire Resistance

A vial of swirling orange liquid. Looks like you're drinking liquid fire, but the taste is surprisingly pleasant.

## Research effect

A vial of swirling orange liquid. Looks like you're drinking liquid fire, but the taste is surprisingly pleasant.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | fire_resist_potion |
| Type | Recipe |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Alchemist](tech-alchemist.md) |
| [Feral Den](tech-dungeon_feral_den.md) |

## Related item

| Item |
| --- |
| [Elixir of Fire Resistance](item-fire_resist_potion.md) |

## Related recipe

| Recipe |
| --- |
| [Elixir of Fire Resistance](recipe-fire_resist_potion.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"alchemist\"",
  "IconName": "\"Icons2_146\"",
  "AdditionalRequirements": "new List<string> { \"dungeon_feral_den\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T9Alchemist.cs:66`
- `Assets.Source.Player/TechNode.cs:1`
