# New Hotness

Adventurers can now replace their existing equipment at the Outfitter. If an item of the exact same type is supplied, the Outfitter is skipped instead.

## Research effect

Adventurers can now replace their existing equipment at the Outfitter. If an item of the exact same type is supplied, the Outfitter is skipped instead.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | outfitter_skip_replace |
| Type | Utility |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Outfitter](tech-outfitter.md) |
| [Quest Board](tech-quest_board.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"outfitter\"",
  "RelativePosition": "new Vector2Int(-225, 26)",
  "CostTier": "5",
  "CostCurrency": "CurrencyCollection.GoldRing",
  "IconName": "\"Icons_221\"",
  "AdditionalRequirements": "new List<string> { \"quest_board\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3Barracks.cs:55`
- `Assets.Source.Player/TechNode.cs:1`
