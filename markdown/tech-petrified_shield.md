# Petrified Shield

An impenetrable bulwark safeguarding the wielder and their allies.

## Research effect

An impenetrable bulwark safeguarding the wielder and their allies.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | petrified_shield |
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
| [Petrified Shield](item-petrified_shield.md) |

## Related recipe

| Recipe |
| --- |
| [Petrified Shield](recipe-petrified_shield.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"carpenter\"",
  "CostTier": "10",
  "AdditionalRequirements": "new List<string> { \"inventor\" }",
  "IconName": "\"Icons3_27\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Carpenter.cs:125`
- `Assets.Source.Player/TechNode.cs:1`
