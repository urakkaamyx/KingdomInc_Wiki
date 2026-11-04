# Archmage's Staff

A high-ranking mage's beacon of authority, as well as the main source of their power.

## Research effect

A high-ranking mage's beacon of authority, as well as the main source of their power.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | archmage_staff |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Carpenter](tech-carpenter.md) |
| [Inventor](tech-inventor.md) |

## Related item

| Item |
| --- |
| [Archmage's Staff](item-archmage_staff.md) |

## Related recipe

| Recipe |
| --- |
| [Archmage's Staff](recipe-archmage_staff.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"carpenter\"",
  "CostTier": "10",
  "AdditionalRequirements": "new List<string> { \"inventor\" }",
  "IconName": "\"Icons3_29\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Carpenter.cs:133`
- `Assets.Source.Player/TechNode.cs:1`
