# Demonsteel Armor

Blood drips continuously from tiny holes in the armor's surface with no indication of where it's coming from.

## Research effect

Blood drips continuously from tiny holes in the armor's surface with no indication of where it's coming from.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | demonsteel_armor |
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
| [Demonsteel Armor](item-demonsteel_armor.md) |

## Related recipe

| Recipe |
| --- |
| [Demonsteel Armor](recipe-demonsteel_armor.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"scribe\"",
  "IconName": "\"Icons3_4\"",
  "CostCurrency": "CurrencyCollection.GoldIngenuity",
  "AdditionalRequirements": "new List<string> { \"dungeon_catacombs\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Scribe.cs:134`
- `Assets.Source.Player/TechNode.cs:1`
