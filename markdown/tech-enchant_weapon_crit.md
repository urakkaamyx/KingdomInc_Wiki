# Enchant Weapon - Critical Hit

Enchants any weapon to add a chance to deal double damage.

A character can only benefit from a single source of Critical Hit.

## Research effect

Enchants any weapon to add a chance to deal double damage.

A character can only benefit from a single source of Critical Hit.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | enchant_weapon_crit |
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
| [Enchant Weapon - Critical Hit](recipe-enchant_weapon_crit.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"enchanter\"",
  "IconName": "\"Icons2_181\"",
  "AdditionalRequirements": "new List<string> { \"butcher_stalker\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T6Enchanter.cs:92`
- `Assets.Source.Player/TechNode.cs:1`
