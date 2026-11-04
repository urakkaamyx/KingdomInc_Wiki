# Identify Plants

Your expert alchemist takes a good look at the plant samples collected by your adventurers and sorts them by type.

## Research effect

Your expert alchemist takes a good look at the plant samples collected by your adventurers and sorts them by type.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | identify_plants |
| Type | Recipe |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Alchemist](tech-alchemist.md) |
| [Feral Den](tech-dungeon_feral_den.md) |

## Related recipe

| Recipe |
| --- |
| [Identify Plants](recipe-identify_plants.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"alchemist\"",
  "IconName": "\"Icons2_148\"",
  "AdditionalRequirements": "new List<string> { \"dungeon_feral_den\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T9Alchemist.cs:59`
- `Assets.Source.Player/TechNode.cs:1`
