# Purified Mago-tech

The clerics at the Cathedral of Saint Ilonia swear that the heretical influence has been purged from this powerful arcane technology.

## Research effect

The clerics at the Cathedral of Saint Ilonia swear that the heretical influence has been purged from this powerful arcane technology.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | purified_tech |
| Type | Recipe |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Shrine](tech-shrine.md) |
| [Timeless Archive](tech-dungeon_archive.md) |

## Related item

| Item |
| --- |
| [Purified Mago-tech](item-purified_tech.md) |

## Related recipe

| Recipe |
| --- |
| [Purified Mago-tech](recipe-purified_tech.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"shrine\"",
  "IconName": "\"Icons3_39\"",
  "CostCurrency": "CurrencyCollection.GoldFaith",
  "AdditionalRequirements": "new List<string> { \"dungeon_archive\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:119`
- `Assets.Source.Player/TechNode.cs:1`
