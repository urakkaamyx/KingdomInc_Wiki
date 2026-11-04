# Elixir of Poison Resistance

A sickly-green potion. Drinking it makes you gag at first, before that nagging headache miraculously disappears.

## Research effect

A sickly-green potion. Drinking it makes you gag at first, before that nagging headache miraculously disappears.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | poison_resist_potion |
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
| [Elixir of Poison Resistance](item-poison_resist_potion.md) |

## Related recipe

| Recipe |
| --- |
| [Elixir of Poison Resistance](recipe-poison_resist_potion.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"alchemist\"",
  "IconName": "\"Icons2_157\"",
  "AdditionalRequirements": "new List<string> { \"dungeon_feral_den\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T9Alchemist.cs:80`
- `Assets.Source.Player/TechNode.cs:1`
