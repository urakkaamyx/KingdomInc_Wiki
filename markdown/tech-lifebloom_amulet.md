# Lifebloom Amulet

Exudes a gentle soothing aura that intermittently heals the wearer's allies for a small amount.

## Research effect

Exudes a gentle soothing aura that intermittently heals the wearer's allies for a small amount.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | lifebloom_amulet |
| Type | Recipe |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Jeweler](tech-jeweler.md) |
| [Alchemist](tech-alchemist.md) |

## Related item

| Item |
| --- |
| [Lifebloom Amulet](item-lifebloom_amulet.md) |

## Related recipe

| Recipe |
| --- |
| [Lifebloom Amulet](recipe-lifebloom_amulet.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"jeweler\"",
  "IconName": "\"Icons2_213\"",
  "AdditionalRequirements": "new List<string> { \"alchemist\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8Jeweler.cs:152`
- `Assets.Source.Player/TechNode.cs:1`
