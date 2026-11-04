# Silver Ingot

A small bar of purified silver, ready to be turned into art.

## Research effect

A small bar of purified silver, ready to be turned into art.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | silver_ingot |
| Type | Recipe |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Forge](tech-forge.md) |
| [Mine Silver Ore](tech-mine_silver_ore.md) |

## Related item

| Item |
| --- |
| [Silver Ingot](item-silver_ingot.md) |

## Related recipe

| Recipe |
| --- |
| [Silver Ingot](recipe-silver_ingot.md) |

## Leads to

| Research |
| --- |
| [Parade Armor](tech-gold_armor.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"forge\"",
  "IconName": "\"Icons_86\"",
  "AdditionalRequirements": "new List<string> { \"mine_silver_ore\" }",
  "CostTier": "3"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Forge.cs:33`
- `Assets.Source.Player/TechNode.cs:1`
