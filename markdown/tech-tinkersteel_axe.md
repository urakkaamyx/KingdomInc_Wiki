# Tinkersteel Battleaxe

The weapon's mass appears to increase significantly before impact, inflicting both slashing and bludgeoning mayhem.

## Research effect

The weapon's mass appears to increase significantly before impact, inflicting both slashing and bludgeoning mayhem.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | tinkersteel_axe |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Blacksmith](tech-blacksmith.md) |
| [Inventor](tech-inventor.md) |

## Related item

| Item |
| --- |
| [Tinkersteel Battleaxe](item-tinkersteel_axe.md) |

## Related recipe

| Recipe |
| --- |
| [Tinkersteel Battleaxe](recipe-tinkersteel_axe.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"blacksmith\"",
  "IconName": "\"Icons3_19\"",
  "CostTier": "10",
  "AdditionalRequirements": "new List<string> { \"inventor\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:202`
- `Assets.Source.Player/TechNode.cs:1`
