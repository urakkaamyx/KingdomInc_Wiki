# Possessed Shield

The demonic creature trapped inside the shield threatens to curse anyone that dares to strike it.

## Research effect

The demonic creature trapped inside the shield threatens to curse anyone that dares to strike it.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | infected_shield |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Scribe](tech-scribe.md) |
| [Yensburg Catacombs](tech-dungeon_catacombs.md) |

## Related item

| Item |
| --- |
| [Possessed Shield](item-infected_shield.md) |

## Related recipe

| Recipe |
| --- |
| [Possessed Shield](recipe-infected_shield.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"scribe\"",
  "IconName": "\"Icons3_28\"",
  "CostCurrency": "CurrencyCollection.GoldIngenuity",
  "AdditionalRequirements": "new List<string> { \"dungeon_catacombs\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Scribe.cs:142`
- `Assets.Source.Player/TechNode.cs:1`
