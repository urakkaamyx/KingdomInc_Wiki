# Prayer Beads

An ornate necklace of blessed gold and silver beads, intended to be used in ritualized prayer.

## Research effect

An ornate necklace of blessed gold and silver beads, intended to be used in ritualized prayer.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | prayer_beads |
| Type | Recipe |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Jeweler](tech-jeweler.md) |
| [Shrine](tech-shrine.md) |

## Related item

| Item |
| --- |
| [Prayer Beads](item-prayer_beads.md) |

## Related recipe

| Recipe |
| --- |
| [Prayer Beads](recipe-prayer_beads.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"jeweler\"",
  "IconName": "\"Icons3_70\"",
  "CostTier": "11",
  "CostCurrency": "CurrencyCollection.GoldFaith",
  "CostMultiplier": "0.5",
  "AdditionalRequirements": "new List<string> { \"shrine\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8Jeweler.cs:172`
- `Assets.Source.Player/TechNode.cs:1`
