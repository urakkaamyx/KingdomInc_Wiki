# Enchant Shield - Shadow Ward

Enchants any Shield to reduce shadow damage taken in battle.

## Research effect

Enchants any Shield to reduce shadow damage taken in battle.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | enchant_armor_shadow_resist |
| Type | Recipe |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Enchanter](tech-enchanter.md) |
| [Butcher Stalker](tech-butcher_stalker.md) |

## Related recipe

| Recipe |
| --- |
| [Enchant Shield - Shadow Ward](recipe-enchant_armor_shadow_resist.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"enchanter\"",
  "IconName": "\"Icons2_178\"",
  "AdditionalRequirements": "new List<string> { \"butcher_stalker\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T6Enchanter.cs:85`
- `Assets.Source.Player/TechNode.cs:1`
