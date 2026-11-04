# Gold Ingot

A small bar of purified gold, ready to be turned into art.

## Research effect

A small bar of purified gold, ready to be turned into art.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | gold_ingot |
| Type | Recipe |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Forge](tech-forge.md) |
| [Mine Gold Ore](tech-mine_gold_ore.md) |

## Related item

| Item |
| --- |
| [Gold Ingot](item-gold_ingot.md) |

## Related recipe

| Recipe |
| --- |
| [Gold Ingot](recipe-gold_ingot.md) |

## Leads to

| Research |
| --- |
| [Ceremonial Sword](tech-gold_sword.md) |
| [Parade Armor](tech-gold_armor.md) |
| [Sapphire Crown](tech-gold_crown.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"forge\"",
  "IconName": "\"Icons_85\"",
  "AdditionalRequirements": "new List<string> { \"mine_gold_ore\" }",
  "CostTier": "3"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Forge.cs:25`
- `Assets.Source.Player/TechNode.cs:1`
