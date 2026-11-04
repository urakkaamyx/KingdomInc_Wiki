# Staff of Sages

A runecarved staff of ancient design, carried by sages and soothsayers for generations.

## Research effect

A runecarved staff of ancient design, carried by sages and soothsayers for generations.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | ancient_wis_staff |
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
| [Staff of Sages](item-ancient_wis_staff.md) |

## Related recipe

| Recipe |
| --- |
| [Staff of Sages](recipe-ancient_wis_staff.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"carpenter\"",
  "CostTier": "8",
  "AdditionalRequirements": "new List<string> { \"dungeon\" }",
  "IconName": "\"Icons2_23\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Carpenter.cs:109`
- `Assets.Source.Player/TechNode.cs:1`
