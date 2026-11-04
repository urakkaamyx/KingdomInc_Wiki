# Elixir of Regeneration

The thick liquid burns on the way down, in a pleasant way. The drinker feels continuously reinvigorated, an effect that can last for days.

## Research effect

The thick liquid burns on the way down, in a pleasant way. The drinker feels continuously reinvigorated, an effect that can last for days.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | regen_potion |
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
| [Elixir of Regeneration](item-regen_potion.md) |

## Related recipe

| Recipe |
| --- |
| [Elixir of Regeneration](recipe-regen_potion.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"alchemist\"",
  "IconName": "\"Icons2_159\"",
  "AdditionalRequirements": "new List<string> { \"dungeon_feral_den\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T9Alchemist.cs:115`
- `Assets.Source.Player/TechNode.cs:1`
