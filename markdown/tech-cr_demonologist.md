# Demonic Initiation

A secret ritual known only to the hermit allows a warlock to train as a Demonologist.

## Research effect

A secret ritual known only to the hermit allows a warlock to train as a Demonologist.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | cr_demonologist |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Summoning Circle](tech-summoning_circle.md) |
| [Scribe](tech-scribe.md) |

## Related recipe

| Recipe |
| --- |
| [Demonic Initiation](recipe-cr_demonologist.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"summoning_circle\"",
  "IconName": "\"Icons2_134\"",
  "CostTier": "10",
  "AdditionalRequirements": "new List<string> { \"scribe\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8SummoningCircle.cs:76`
- `Assets.Source.Player/TechNode.cs:1`
