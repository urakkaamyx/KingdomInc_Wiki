# Gilded Coffin

A wooden coffin decorated with a copious amount of gold, destined to hold the remains of someone important.

## Research effect

A wooden coffin decorated with a copious amount of gold, destined to hold the remains of someone important.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | gilded_coffin |
| Type | Recipe |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Engraver](tech-engraver.md) |
| [Graveyard](tech-graveyard.md) |

## Related item

| Item |
| --- |
| [Gilded Coffin](item-gilded_coffin.md) |

## Related recipe

| Recipe |
| --- |
| [Gilded Coffin](recipe-gilded_coffin.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"engraver\"",
  "CostTier": "7",
  "AdditionalRequirements": "new List<string> { \"graveyard\" }",
  "IconName": "\"Icons2_87\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3Engraver.cs:135`
- `Assets.Source.Player/TechNode.cs:1`
