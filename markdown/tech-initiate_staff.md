# Initiate's Staff

Initiate wizards are given a staff during their training, adding their own magic over time.

## Research effect

Initiate wizards are given a staff during their training, adding their own magic over time.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | initiate_staff |
| Type | Recipe |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Carpenter](tech-carpenter.md) |
| [Mine Sapphire](tech-mine_sapphire.md) |

## Related item

| Item |
| --- |
| [Initiate's Staff](item-initiate_staff.md) |

## Related recipe

| Recipe |
| --- |
| [Initiate's Staff](recipe-initiate_staff.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"carpenter\"",
  "IconName": "\"Icons_50\"",
  "AdditionalRequirements": "new List<string> { \"mine_sapphire\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Carpenter.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
