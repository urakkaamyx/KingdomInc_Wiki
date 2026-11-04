# Elixir of Alacrity

A highly concentrated emerald liquid. It hones the drinker's quick wit and reflexes, making rapid actions easier to execute.

## Research effect

A highly concentrated emerald liquid. It hones the drinker's quick wit and reflexes, making rapid actions easier to execute.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | swiftness_potion |
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
| [Elixir of Alacrity](item-swiftness_potion.md) |

## Related recipe

| Recipe |
| --- |
| [Elixir of Alacrity](recipe-swiftness_potion.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"alchemist\"",
  "IconName": "\"Icons2_158\"",
  "AdditionalRequirements": "new List<string> { \"dungeon_feral_den\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T9Alchemist.cs:108`
- `Assets.Source.Player/TechNode.cs:1`
