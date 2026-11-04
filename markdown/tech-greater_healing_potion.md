# Greater Healing Potion

A brilliant red potion that can instantly restore grievous wounds.

## Research effect

A brilliant red potion that can instantly restore grievous wounds.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | greater_healing_potion |
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
| [Greater Healing Potion](item-greater_healing_potion.md) |

## Related recipe

| Recipe |
| --- |
| [Greater Healing Potion](recipe-greater_healing_potion.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"alchemist\"",
  "IconName": "\"Icons2_155\"",
  "AdditionalRequirements": "new List<string> { \"dungeon_feral_den\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T9Alchemist.cs:94`
- `Assets.Source.Player/TechNode.cs:1`
