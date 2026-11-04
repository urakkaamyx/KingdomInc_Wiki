# War: Ironcrag Siege

Ironcrag has been revealed as our enemy's stronghold. Lay siege to the mountain and clear a path for your adventurers to enter.

## Research effect

Ironcrag has been revealed as our enemy's stronghold. Lay siege to the mountain and clear a path for your adventurers to enter.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | war_effort_north |
| Type | War |
| Cost tier | 12 |

## Prerequisites

| Required research |
| --- |
| [Shrine](tech-shrine.md) |

## Additional condition

Requires war progress: Throne Room

## Campaign condition

yensburg:4 (campaign ID : completed stage)

## Leads to

| Research |
| --- |
| [Timeless Archive](tech-dungeon_archive.md) |
| [Tomb of Sholrath](tech-dungeon_endgame.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.War",
  "Previous": "\"shrine\"",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons2_68\"",
  "ForceRootNode": "true",
  "CostTier": "12",
  "CustomRequirement": "(GamePlayer ply) => ply.HasWarStage(\"yensburg\", 4)",
  "CustomRequirementDesc": "\"@war_north_unlock\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tGamePlayer.Current.UnlockWar(\"north\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:212`
- `Assets.Source.Player/TechNode.cs:1`
