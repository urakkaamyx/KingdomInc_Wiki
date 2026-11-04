# Vanquisher's Sword

Dark matter particles drift off its edge and embed themselves into the wounds of its victims, inflicting more suffering over time.

## Research effect

Dark matter particles drift off its edge and embed themselves into the wounds of its victims, inflicting more suffering over time.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | vanquisher_sword |
| Type | Recipe |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Shrine](tech-shrine.md) |
| [Timeless Archive](tech-dungeon_archive.md) |

## Related item

| Item |
| --- |
| [Vanquisher's Sword](item-vanquisher_sword.md) |

## Related recipe

| Recipe |
| --- |
| [Vanquisher's Sword](recipe-vanquisher_sword.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"shrine\"",
  "IconName": "\"Icons3_24\"",
  "CostCurrency": "CurrencyCollection.GoldFaith",
  "AdditionalRequirements": "new List<string> { \"dungeon_archive\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:127`
- `Assets.Source.Player/TechNode.cs:1`
