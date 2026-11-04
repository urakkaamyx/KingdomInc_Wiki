# Stoneskin Elixir

A disgustingly bitter potion. Shortly after consumption, the drinker feels impervious to harm.

## Research effect

A disgustingly bitter potion. Shortly after consumption, the drinker feels impervious to harm.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | armor_potion |
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
| [Stoneskin Elixir](item-armor_potion.md) |

## Related recipe

| Recipe |
| --- |
| [Stoneskin Elixir](recipe-armor_potion.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"alchemist\"",
  "IconName": "\"Icons2_154\"",
  "AdditionalRequirements": "new List<string> { \"dungeon_feral_den\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T9Alchemist.cs:87`
- `Assets.Source.Player/TechNode.cs:1`
