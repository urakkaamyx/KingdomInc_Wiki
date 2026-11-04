# Elixir of Shadow Resistance

A dark purple brew. Trying to drink it evokes an almost primal fear in most people.

## Research effect

A dark purple brew. Trying to drink it evokes an almost primal fear in most people.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | shadow_resist_potion |
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
| [Elixir of Shadow Resistance](item-shadow_resist_potion.md) |

## Related recipe

| Recipe |
| --- |
| [Elixir of Shadow Resistance](recipe-shadow_resist_potion.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"alchemist\"",
  "IconName": "\"Icons2_183\"",
  "AdditionalRequirements": "new List<string> { \"dungeon_feral_den\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T9Alchemist.cs:73`
- `Assets.Source.Player/TechNode.cs:1`
