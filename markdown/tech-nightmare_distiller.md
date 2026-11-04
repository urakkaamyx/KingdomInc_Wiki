# Nightmare Distiller

Allows you collect more Distilled Nightmare prestige currency. Requires a steady supply of Nightmare Collectors.

## Research effect

Allows you collect more Distilled Nightmare prestige currency. Requires a steady supply of Nightmare Collectors.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | nightmare_distiller |
| Type | Flow Element |
| Cost tier | 12 |

## Prerequisites

| Required research |
| --- |
| [Tomb of Sholrath](tech-dungeon_endgame.md) |

## Additional condition

Requires dungeon progress: Tendril of Sholrath

## Leads to

| Research |
| --- |
| [Nightmare Casing](tech-nightmare_casing.md) |
| [Reconstructed Nightmare](tech-reconstructed_nightmare.md) |
| [Nightmare Collector](tech-nightmare_collector.md) |
| [Cleansed Nightmare](tech-cleansed_nightmare.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"dungeon_endgame\"",
  "RelativePosition": "new Vector2Int(0, 290)",
  "IconName": "\"Icons3_92\"",
  "CustomRequirement": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tDungeonMetadata dungeonMetadata = ply.GetDungeonMetadata(DungeonType.Get(\"endgame\"));\n\t\t\t\treturn dungeonMetadata.CompletedCount[dungeonMetadata.CompletedCount.Length - 1] > 0;\n\t\t\t}",
  "CustomRequirementDesc": "\"@nightmare_distiller_locked\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:254`
- `Assets.Source.Player/TechNode.cs:1`
