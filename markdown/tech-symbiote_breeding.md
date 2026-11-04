# Sinister Prodigy

Breeds more Symbionts by exposing them to the corrupting essence of darkness.

## Research effect

Breeds more Symbionts by exposing them to the corrupting essence of darkness.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | symbiote_breeding |
| Type | Recipe |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Enchanter](tech-enchanter.md) |
| [Temple of the Last Rite](tech-dungeon_temple.md) |

## Related recipe

| Recipe |
| --- |
| [Sinister Prodigy](recipe-symbiote_breeding.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"enchanter\"",
  "IconName": "\"Icons2_212\"",
  "AdditionalRequirements": "new List<string> { \"dungeon_temple\" }",
  "CostTier": "9",
  "CostCurrency": "CurrencyCollection.GoldMana"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T6Enchanter.cs:123`
- `Assets.Source.Player/TechNode.cs:1`
