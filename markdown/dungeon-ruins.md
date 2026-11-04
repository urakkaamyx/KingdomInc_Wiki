# Ruins of Arlingen

The remnants of an ancient treasure vault, repurposed into a high-security prison after the flow of valuables from the east dried up. 

Scouting reports indicate that the surface is crawling with orcs, while the lower levels are controlled by the shambling remains of former inmates.

## Overview

The remnants of an ancient treasure vault, repurposed into a high-security prison after the flow of valuables from the east dried up. 

Scouting reports indicate that the surface is crawling with orcs, while the lower levels are controlled by the shambling remains of former inmates.

## Entry requirements

| Property | Value |
| --- | --- |
| Unlock Tech | dungeon |
| Unavailable Text | Requires war progress: Ruins of Arlingen |
| Supplies per run | 210 Rings |
| Availability condition | (GamePlayer ply) => ply.HasWarStage("eastern", 2) |

## Stages in order

| Stage | Base difficulty | Base health | Challenges |
| --- | --- | --- | --- |
| [Ruined Hall](stage-ruins_1_trash.md) | 1000 | 50L | Clear Rubble |
| [Crull the Defiler](stage-ruins_1_boss.md) | 1300 | 30L | Tank Fire Damage, Acid Rain |
| [Armory Wing](stage-ruins_2_trash.md) | 1300 | 50L | Arcane Traps |
| [Quartermaster Vadric](stage-ruins_2_boss.md) | 1600 | 30L | Reaping Strike, Soul Reave |
| [Cell Block Z](stage-ruins_3_trash.md) | 1600 | 50L | Caltrops |
| ["Black Eye" Marlowe](stage-ruins_3_boss.md) | 1800 | 30L | Flailing Strike, Reckless Charge |
| [Solitary Confinement](stage-ruins_4_trash.md) | 1800 | 50L | Exhausting |
| [Watcher of Tomorrows](stage-ruins_4_boss.md) | 2000 | 30L | Tank Shadow Damage, Scatter Beam |

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@dungeon_ruins\"",
  "Description": "\"@dungeon_ruins_desc\"",
  "IconName": "\"Icons_178\"",
  "UnlockTech": "\"dungeon\"",
  "IsAvailable": "(GamePlayer ply) => ply.HasWarStage(\"eastern\", 2)",
  "UnavailableText": "\"@dungeon_ruins_blocked\"",
  "SupplyCost": "new CurrencyCollection(Currency.Ring, 210L)"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Ruins.cs:11`
