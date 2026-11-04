# Temple of the Last Rite

Ages ago, a profane ritual was carried out here to imprison an ancient evil. Now, sinister forces are working to undo the ritual's magic.

## Overview

Ages ago, a profane ritual was carried out here to imprison an ancient evil. Now, sinister forces are working to undo the ritual's magic.

## Entry requirements

| Property | Value |
| --- | --- |
| Unlock Tech | dungeon_temple |
| Unavailable Text | Requires war progress: Bastion |
| Supplies per run | 220 Crowns |
| Availability condition | (GamePlayer ply) => ply.HasWarStage("eastern", 4) |

## Stages in order

| Stage | Base difficulty | Base health | Challenges |
| --- | --- | --- | --- |
| [Temple Grounds](stage-temple_1_trash.md) | 2200 | 50L | Desert Sun |
| [Jax the Stinger](stage-temple_1_boss.md) | 2400 | 30L | Desert Sun, Venom Barb |
| [The Great Pyramid](stage-temple_2_trash.md) | 2400 | 50L | Desert Sun |
| [Crystallax](stage-temple_2_boss.md) | 2600 | 30L | Brutal Slam, Flailing Strike |
| [Embalming Chamber](stage-temple_3_trash.md) | 2600 | 50L | Arcane Traps |
| [Amun the Orchestrator](stage-temple_3_boss.md) | 2800 | 30L | Tank Shadow Damage, Tremors |
| [Inner Sanctum](stage-temple_4_trash.md) | 3000 | 50L | Arcane Traps |
| [Sholrath's Chosen](stage-temple_4_boss.md) | 3300 | 30L | Tank Shadow Damage, Consuming Shadows |

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@dungeon_temple\"",
  "Description": "\"@dungeon_temple_desc\"",
  "IconName": "\"Icons2_61\"",
  "UnlockTech": "\"dungeon_temple\"",
  "IsAvailable": "(GamePlayer ply) => ply.HasWarStage(\"eastern\", 4)",
  "UnavailableText": "\"@dungeon_temple_blocked\"",
  "SupplyCost": "new CurrencyCollection(Currency.Crown, 220L)"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Temple.cs:11`
