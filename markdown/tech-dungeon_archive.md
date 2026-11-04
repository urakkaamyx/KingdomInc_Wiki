# Timeless Archive

An ancient lich lord has been building an archive of human history in this hidden mountain fortress for centuries. Break through the defenses, slay the mad Archivist, and recover powerful items to aid in your battle.

## Research effect

An ancient lich lord has been building an archive of human history in this hidden mountain fortress for centuries. Break through the defenses, slay the mad Archivist, and recover powerful items to aid in your battle.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | dungeon_archive |
| Type | Dungeon |
| Cost tier | 12 |

## Prerequisites

| Required research |
| --- |
| [War: Ironcrag Siege](tech-war_effort_north.md) |

## Additional condition

Requires war progress: The Old Guildhouse

## Campaign condition

north:1 (campaign ID : completed stage)

## Leads to

| Research |
| --- |
| [Purified Mago-tech](tech-purified_tech.md) |
| [Vanquisher's Sword](tech-vanquisher_sword.md) |
| [Blighted Dagger](tech-blighted_dagger.md) |
| [Ethereal Rapier](tech-blink_rapier.md) |
| [Flenser's Sword](tech-flenser_greatsword.md) |
| [Cyclopean Battleaxe](tech-unblinking_axe.md) |
| [Deadeye Bow](tech-deadeye_bow.md) |
| [Splintered Staff](tech-fragment_staff.md) |
| [Unlife Staff](tech-unlife_staff.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Dungeon",
  "Previous": "\"war_effort_north\"",
  "RelativePosition": "new Vector2Int(-450, 17)",
  "IconName": "\"Icons2_70\"",
  "CustomRequirement": "(GamePlayer ply) => ply.HasWarStage(\"north\", 1)",
  "CustomRequirementDesc": "\"@dungeon_archive_unlock\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.UnlockDungeon(\"archive\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:227`
- `Assets.Source.Player/TechNode.cs:1`
