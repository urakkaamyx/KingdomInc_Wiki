# Tomb of Sholrath

Deep beneath the mountain, an ancient evil waits dreaming.

## Research effect

Deep beneath the mountain, an ancient evil waits dreaming.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | dungeon_endgame |
| Type | Dungeon |
| Cost tier | 12 |

## Prerequisites

| Required research |
| --- |
| [War: Ironcrag Siege](tech-war_effort_north.md) |

## Additional condition

Requires war progress: Pinnacle Ruins

## Campaign condition

north:4 (campaign ID : completed stage)

## Leads to

| Research |
| --- |
| [Nightmare Distiller](tech-nightmare_distiller.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Dungeon",
  "Previous": "\"war_effort_north\"",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons2_71\"",
  "CostTier": "12",
  "CustomRequirement": "(GamePlayer ply) => ply.HasWarStage(\"north\", 4)",
  "CustomRequirementDesc": "\"@dungeon_endgame_unlock\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.UnlockDungeon(\"endgame\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:240`
- `Assets.Source.Player/TechNode.cs:1`
