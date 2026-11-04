# Sapphire Crown

An ornate piece of jewelry, sometimes worn by the aristocracy in honor of the late King.

## Research effect

An ornate piece of jewelry, sometimes worn by the aristocracy in honor of the late King.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | gold_crown |
| Type | Recipe |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Blacksmith](tech-blacksmith.md) |
| [Gold Ingot](tech-gold_ingot.md) |
| [Mine Sapphire](tech-mine_sapphire.md) |

## Related item

| Item |
| --- |
| [Sapphire Crown](item-gold_crown.md) |

## Related recipe

| Recipe |
| --- |
| [Sapphire Crown](recipe-gold_crown.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"blacksmith\"",
  "IconName": "\"Icons_108\"",
  "CostTier": "3",
  "AdditionalRequirements": "new List<string> { \"gold_ingot\", \"mine_sapphire\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:82`
- `Assets.Source.Player/TechNode.cs:1`
