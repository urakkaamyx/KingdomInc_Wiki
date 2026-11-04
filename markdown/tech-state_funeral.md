# State Funeral

A highly ornate funeral for only the most decorated of war heroes. Generates additional Faith based on the cleric's Wisdom.

## Research effect

A highly ornate funeral for only the most decorated of war heroes. Generates additional Faith based on the cleric's Wisdom.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | state_funeral |
| Type | Recipe |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Graveyard](tech-graveyard.md) |

## Related recipe

| Recipe |
| --- |
| [State Funeral](recipe-state_funeral.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"graveyard\"",
  "CostCurrency": "CurrencyCollection.GoldFaith",
  "IconName": "\"Icons2_90\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Graveyard.cs:50`
- `Assets.Source.Player/TechNode.cs:1`
