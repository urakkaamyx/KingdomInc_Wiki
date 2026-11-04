# Yensburg Catacombs

The labyrinthine tunnels beneath Yensburg Castle are still crawling with demonic entities. Send your adventurers down to clear them out and discover their origin.

## Overview

The labyrinthine tunnels beneath Yensburg Castle are still crawling with demonic entities. Send your adventurers down to clear them out and discover their origin.

## Entry requirements

| Property | Value |
| --- | --- |
| Unlock Tech | dungeon_catacombs |
| Unavailable Text | Retake the Castle District to continue. |
| Supplies per run | 320 Crowns |
| Availability condition | (GamePlayer ply) => ply.HasWarStage("yensburg", 3) |

## Stages in order

| Stage | Base difficulty | Base health | Challenges |
| --- | --- | --- | --- |
| [Sewer Tunnels](stage-catacombs_1_trash.md) | 3500 | 50L | Dilute Poison |
| [Uzgrim the Hermit](stage-catacombs_1_boss.md) | 3200 | 30L | Mana Poison, Tank Fire Damage |
| [Hall of Bones](stage-catacombs_2_trash.md) | 3800 | 50L | Caltrops |
| [Bone Golem](stage-catacombs_2_boss.md) | 4100 | 30L | Brutal Slam, Flailing Strike |
| [Mausoleum of Heroes](stage-catacombs_3_trash.md) | 4200 | 50L | Exhausting |
| [Guardian of the Ninth Gate](stage-catacombs_3_boss.md) | 4500 | 30L | Tank Fire Damage, Pyroclasm |
| [Sanctum of Saint Ilonia](stage-catacombs_4_trash.md) | 4700 | 50L | Arcane Traps |
| [Herald of the Legion](stage-catacombs_4_boss.md) | 5000 | 30L | Tank Fire Damage, Reaping Strike |

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@dungeon_catacombs\"",
  "Description": "\"@dungeon_catacombs_desc\"",
  "IconName": "\"Icons2_69\"",
  "UnlockTech": "\"dungeon_catacombs\"",
  "IsAvailable": "(GamePlayer ply) => ply.HasWarStage(\"yensburg\", 3)",
  "UnavailableText": "\"@dungeon_catacombs_blocked\"",
  "SupplyCost": "new CurrencyCollection(Currency.Crown, 320L)"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Catacombs.cs:11`
