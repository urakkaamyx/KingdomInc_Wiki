# Bring A Snack

Unlocks the Food equipment slot for the Outfitter.

## Research effect

Unlocks the Food equipment slot for the Outfitter.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | outfitter_2 |
| Type | Utility |
| Cost tier | 3 |
| Visibility | Hidden by code |

## Prerequisites

| Required research |
| --- |
| [Outfitter](tech-outfitter.md) |
| [Campfire](tech-campfire.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"outfitter\"",
  "RelativePosition": "new Vector2Int(-225, 26)",
  "IconName": "\"Icons_129\"",
  "Hidden": "(GamePlayer ply) => true",
  "AdditionalRequirements": "new List<string> { \"campfire\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3Barracks.cs:72`
- `Assets.Source.Player/TechNode.cs:1`
