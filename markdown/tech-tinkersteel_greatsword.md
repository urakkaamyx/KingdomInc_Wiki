# Tinkersteel Greatsword

Even though the edge doesn't seem to be particularly sharp, it still slices through almost anything with ease.

## Research effect

Even though the edge doesn't seem to be particularly sharp, it still slices through almost anything with ease.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | tinkersteel_greatsword |
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
| [Tinkersteel Greatsword](item-tinkersteel_greatsword.md) |

## Related recipe

| Recipe |
| --- |
| [Tinkersteel Greatsword](recipe-tinkersteel_greatsword.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"blacksmith\"",
  "IconName": "\"Icons3_15\"",
  "CostTier": "10",
  "AdditionalRequirements": "new List<string> { \"inventor\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:194`
- `Assets.Source.Player/TechNode.cs:1`
