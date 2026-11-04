# Enchant Armor - Giant Strength

Enchants any piece of Head or Chest armor to increase success chance on any Strength checks in combat. Also provides a small amount of Strength.

## Research effect

Enchants any piece of Head or Chest armor to increase success chance on any Strength checks in combat. Also provides a small amount of Strength.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | enchant_armor_strength_skill_crit |
| Type | Recipe |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Enchanter](tech-enchanter.md) |
| [Hamburger](tech-hamburger.md) |

## Related recipe

| Recipe |
| --- |
| [Enchant Armor - Giant Strength](recipe-enchant_armor_strength_skill_crit.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"enchanter\"",
  "IconName": "\"Icons2_184\"",
  "AdditionalRequirements": "new List<string> { \"hamburger\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T6Enchanter.cs:99`
- `Assets.Source.Player/TechNode.cs:1`
