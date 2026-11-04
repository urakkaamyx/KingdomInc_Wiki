# Decoded Writings

After many attempts, the infernal runes have been translated into a form that mortal humans can comprehend.

## Research effect

After many attempts, the infernal runes have been translated into a form that mortal humans can comprehend.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | decoded_writings |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Scribe](tech-scribe.md) |
| [Yensburg Catacombs](tech-dungeon_catacombs.md) |

## Related item

| Item |
| --- |
| [Decoded Writings](item-decoded_writings.md) |

## Related recipe

| Recipe |
| --- |
| [Decoded Writings](recipe-decoded_writings.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"scribe\"",
  "IconName": "\"Icons3_37\"",
  "CostCurrency": "CurrencyCollection.GoldIngenuity",
  "AdditionalRequirements": "new List<string> { \"dungeon_catacombs\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Scribe.cs:118`
- `Assets.Source.Player/TechNode.cs:1`
