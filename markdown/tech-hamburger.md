# Hamburger

An exotic delicacy based off an ancient recipe.

## Research effect

An exotic delicacy based off an ancient recipe.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | hamburger |
| Type | Recipe |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Kitchen](tech-kitchen.md) |
| [Butcher Cattle](tech-butcher_cattle.md) |

## Related item

| Item |
| --- |
| [Hamburger](item-hamburger.md) |

## Related recipe

| Recipe |
| --- |
| [Hamburger](recipe-hamburger.md) |

## Leads to

| Research |
| --- |
| [Enchant Armor - Giant Strength](tech-enchant_armor_strength_skill_crit.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"kitchen\"",
  "IconName": "\"Icons_193\"",
  "AdditionalRequirements": "new List<string> { \"butcher_cattle\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Kitchen.cs:24`
- `Assets.Source.Player/TechNode.cs:1`
