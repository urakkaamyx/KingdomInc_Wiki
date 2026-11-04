# Turtle Statue

An ancient monument, preserved through time. Perhaps a forgotten deity was worshipped here?

## Research effect

An ancient monument, preserved through time. Perhaps a forgotten deity was worshipped here?

## Research data

| Property | Value |
| --- | --- |
| Internal ID | turtle_statue |
| Type | Flow Element |
| Cost tier | 5 |
| Visibility | Hidden by code |

## Prerequisites

| Required research |
| --- |
| [Forest](tech-forest.md) |

## Additional condition

Requires war progress: Yensmouth

## Campaign condition

forest:4 (campaign ID : completed stage)

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"forest\"",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons_131\"",
  "ForceRootNode": "true",
  "Hidden": "(GamePlayer ply) => true",
  "CostTier": "5",
  "CostCurrency": "CurrencyCollection.GoldMedal",
  "CostMultiplier": "8.0",
  "CustomRequirement": "(GamePlayer ply) => ply.HasWarStage(\"forest\", 4)",
  "CustomRequirementDesc": "\"@adventurers_guild_unlock\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5AdventurersGuild.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
