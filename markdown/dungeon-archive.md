# Timeless Archive

An ancient lich lord has been building an archive of human history in this hidden mountain fortress for centuries. Break through the defenses, slay the mad Archivist, and recover powerful items to aid in your battle.

## Overview

An ancient lich lord has been building an archive of human history in this hidden mountain fortress for centuries. Break through the defenses, slay the mad Archivist, and recover powerful items to aid in your battle.

## Entry requirements

| Property | Value |
| --- | --- |
| Unlock Tech | dungeon_archive |
| Unavailable Text | Retake the Old Guildhouse to continue. |
| Supplies per run | 180 Ducats |
| Availability condition | (GamePlayer ply) => ply.HasWarStage("north", 1) |

## Stages in order

| Stage | Base difficulty | Base health | Challenges |
| --- | --- | --- | --- |
| [Vault Entrance](stage-archive_1_trash.md) | 5000 | 50L | Caltrops |
| [Champion of the Vault](stage-archive_1_boss.md) | 5300 | 40L | Reaping Strike, Barreling Charge |
| [Librarium](stage-archive_2_trash.md) | 5300 | 50L | Animated Books |
| [Cannaan the Librarian](stage-archive_2_boss.md) | 5700 | 40L | Brutal Slam, Muscle Magic |
| [Holding Cells](stage-archive_3_trash.md) | 5700 | 50L | Clear Rubble |
| [Pelonnar the Dragonlord](stage-archive_3_boss.md) | 6200 | 40L | Acid Rain, Chilling Howl |
| [Private Collection](stage-archive_4_trash.md) | 6200 | 50L | Animated Guardians |
| [The Mad Archivist](stage-archive_4_boss.md) | 6600 | 40L | Consuming Shadows, Extract Vigor |

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@dungeon_archive\"",
  "Description": "\"@dungeon_archive_desc\"",
  "IconName": "\"Icons2_70\"",
  "UnlockTech": "\"dungeon_archive\"",
  "IsAvailable": "(GamePlayer ply) => ply.HasWarStage(\"north\", 1)",
  "UnavailableText": "\"@dungeon_archive_blocked\"",
  "SupplyCost": "new CurrencyCollection(Currency.Ducat, 180L)"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Archive.cs:11`
