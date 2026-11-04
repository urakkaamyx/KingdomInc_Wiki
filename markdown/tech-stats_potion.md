# Elixir of Mastery

After drinking this concoction the user feels ever so slightly more proficient at anything they do.

## Research effect

After drinking this concoction the user feels ever so slightly more proficient at anything they do.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | stats_potion |
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
| [Elixir of Mastery](item-stats_potion.md) |

## Related recipe

| Recipe |
| --- |
| [Elixir of Mastery](recipe-stats_potion.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"alchemist\"",
  "IconName": "\"Icons2_156\"",
  "AdditionalRequirements": "new List<string> { \"dungeon_feral_den\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T9Alchemist.cs:101`
- `Assets.Source.Player/TechNode.cs:1`
