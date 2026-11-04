# Officiated Burial

Send a Cleric to lead the mourners in solemn prayer. Generates additional Faith based on the cleric's Wisdom.

## Research effect

Send a Cleric to lead the mourners in solemn prayer. Generates additional Faith based on the cleric's Wisdom.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | officiated_burial |
| Type | Recipe |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Graveyard](tech-graveyard.md) |

## Related recipe

| Recipe |
| --- |
| [Officiated Burial](recipe-officiated_burial.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"graveyard\"",
  "CostCurrency": "CurrencyCollection.GoldFaith",
  "IconName": "\"Icons2_89\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Graveyard.cs:43`
- `Assets.Source.Player/TechNode.cs:1`
