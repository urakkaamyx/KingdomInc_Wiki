# Crystalline Staff

A solid wood staff adorned with fragmented mana crystals and delicate gold detailing.

## Research effect

A solid wood staff adorned with fragmented mana crystals and delicate gold detailing.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | ancient_int_staff |
| Type | Recipe |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Carpenter](tech-carpenter.md) |
| [Dungeon](tech-dungeon.md) |

## Related item

| Item |
| --- |
| [Crystalline Staff](item-ancient_int_staff.md) |

## Related recipe

| Recipe |
| --- |
| [Crystalline Staff](recipe-ancient_int_staff.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"carpenter\"",
  "CostTier": "8",
  "AdditionalRequirements": "new List<string> { \"dungeon\" }",
  "IconName": "\"Icons2_22\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Carpenter.cs:101`
- `Assets.Source.Player/TechNode.cs:1`
