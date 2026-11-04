# Tomb of Sholrath

Deep beneath the mountain, an ancient evil waits dreaming.

## Overview

Deep beneath the mountain, an ancient evil waits dreaming.

## Entry requirements

| Property | Value |
| --- | --- |
| Unlock Tech | dungeon_endgame |
| Is Endgame | true |
| Unavailable Text | Retake the Pinnacle Ruins to continue. |
| Supplies per run | 380 Ducats |
| Availability condition | (GamePlayer ply) => ply.HasWarStage("north", 4) |

## Stages in order

| Stage | Base difficulty | Base health | Challenges |
| --- | --- | --- | --- |
| [Lake of Fire](stage-endgame_1_trash.md) | 6400 | 50L | Pyroclasm |
| [Belgor the Infernal](stage-endgame_1_boss.md) | 7200 | 40L | Pyroclasm, Tank Fire Damage |
| [Halls of Sacrifice](stage-endgame_2_trash.md) | 7400 | 50L | Desert Sun |
| [The Last High Priest](stage-endgame_2_boss.md) | 8000 | 40L | Desert Sun, Mana Poison |
| [Obsidian Fortress](stage-endgame_3_trash.md) | 8400 | 50L | Animated Guardians |
| [Herald of Sholrath](stage-endgame_3_boss.md) | 9200 | 40L | Consuming Shadows, Reap Soul |
| [Crystalline Prison](stage-endgame_4_trash.md) | 9400 | 50L | Animated Books |
| [Tendril of Sholrath](stage-endgame_4_boss.md) | 10000 | 40L | Tank Shadow Damage, Waking Nightmare |

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@dungeon_endgame\"",
  "Description": "\"@dungeon_endgame_desc\"",
  "IconName": "\"Icons2_71\"",
  "UnlockTech": "\"dungeon_endgame\"",
  "IsEndgame": "true",
  "IsAvailable": "(GamePlayer ply) => ply.HasWarStage(\"north\", 4)",
  "UnavailableText": "\"@dungeon_endgame_blocked\"",
  "SupplyCost": "new CurrencyCollection(Currency.Ducat, 380L)"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Endgame.cs:11`
