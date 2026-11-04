# Salamander Skewer

A delicious fiery treat.

## Research effect

A delicious fiery treat.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | salamander_skewer |
| Type | Recipe |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Kitchen](tech-kitchen.md) |
| [Butcher Salamander](tech-butcher_salamander.md) |

## Related item

| Item |
| --- |
| [Salamander Skewer](item-salamander_skewer.md) |

## Related recipe

| Recipe |
| --- |
| [Salamander Skewer](recipe-salamander_skewer.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"kitchen\"",
  "IconName": "\"Icons2_174\"",
  "AdditionalRequirements": "new List<string> { \"butcher_salamander\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Kitchen.cs:31`
- `Assets.Source.Player/TechNode.cs:1`
