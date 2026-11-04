# Necklace of Fireballs

The tiny beads on this necklace are, in fact, dangerous weapons: They spontaneously combust after being thrown.

## Research effect

The tiny beads on this necklace are, in fact, dangerous weapons: They spontaneously combust after being thrown.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | fireball_amulet |
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
| [Necklace of Fireballs](item-fireball_amulet.md) |

## Related recipe

| Recipe |
| --- |
| [Necklace of Fireballs](recipe-fireball_amulet.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"jeweler\"",
  "IconName": "\"Icons2_215\"",
  "AdditionalRequirements": "new List<string> { \"alchemist\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8Jeweler.cs:159`
- `Assets.Source.Player/TechNode.cs:1`
