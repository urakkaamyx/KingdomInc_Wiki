# Sanctified Equipment

Extends a holy blessing over any non-weapon piece of equipment, increasing its Quality.

## Research effect

Extends a holy blessing over any non-weapon piece of equipment, increasing its Quality.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | blessed_equipment |
| Type | Recipe |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Shrine](tech-shrine.md) |

## Related recipe

| Recipe |
| --- |
| [Sanctified Equipment](recipe-blessed_equipment.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"shrine\"",
  "IconName": "\"Icons3_76\"",
  "CostCurrency": "CurrencyCollection.GoldFaith"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:69`
- `Assets.Source.Player/TechNode.cs:1`
