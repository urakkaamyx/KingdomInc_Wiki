# Dark Prophet's Robe

A beguiling aura draws the attention of allies and foes alike, turning even the most hardened skeptic into a devout follower.

## Research effect

A beguiling aura draws the attention of allies and foes alike, turning even the most hardened skeptic into a devout follower.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | prophet_robe |
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
| [Dark Prophet's Robe](item-prophet_robe.md) |

## Related recipe

| Recipe |
| --- |
| [Dark Prophet's Robe](recipe-prophet_robe.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"scribe\"",
  "IconName": "\"Icons3_14\"",
  "CostCurrency": "CurrencyCollection.GoldIngenuity",
  "AdditionalRequirements": "new List<string> { \"dungeon_catacombs\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Scribe.cs:190`
- `Assets.Source.Player/TechNode.cs:1`
