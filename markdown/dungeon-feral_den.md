# Feral Den

The vast network of caves known as the Feral Den lies deep beneath the roots of Byrgenwald Forest. Its wild denizens rarely interact with the surface world.

Recent reports show that a strange corruption is seeping from deep within the cave, driving the beasts upwards towards the surface, driven mad with rage.

## Overview

The vast network of caves known as the Feral Den lies deep beneath the roots of Byrgenwald Forest. Its wild denizens rarely interact with the surface world.

Recent reports show that a strange corruption is seeping from deep within the cave, driving the beasts upwards towards the surface, driven mad with rage.

## Entry requirements

| Property | Value |
| --- | --- |
| Unlock Tech | dungeon_feral |
| Unavailable Text | Requires war progress: Feral Den |
| Supplies per run | 320 Rings |
| Availability condition | (GamePlayer ply) => ply.HasWarStage("forest", 3) |

## Stages in order

| Stage | Base difficulty | Base health | Challenges |
| --- | --- | --- | --- |
| [Forest Floor](stage-feral_1_trash.md) | 1400 | 50L | Exhausting |
| [Corrupted Guardian](stage-feral_1_boss.md) | 1600 | 30L | Flailing Strike, Acid Rain |
| [Den Entrance](stage-feral_2_trash.md) | 1700 | 50L | Clear Rubble |
| [Alpha Beast](stage-feral_2_boss.md) | 2000 | 30L | Reckless Charge, Dilute Poison |
| [Contaminated Aquifer](stage-feral_3_trash.md) | 2200 | 50L | Major Poison |
| [Patient Zero](stage-feral_3_boss.md) | 2400 | 30L | Major Poison, Chilling Howl |
| [Ratling Burrows](stage-feral_4_trash.md) | 2500 | 50L | Tremors |
| [Gnawtooth the Toxiferous](stage-feral_4_boss.md) | 2900 | 30L | Inject Poison, Extract Vigor |

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@dungeon_feral\"",
  "Description": "\"@dungeon_feral_desc\"",
  "IconName": "\"Icons2_62\"",
  "UnlockTech": "\"dungeon_feral\"",
  "IsAvailable": "(GamePlayer ply) => ply.HasWarStage(\"forest\", 3)",
  "UnavailableText": "\"@dungeon_feral_blocked\"",
  "SupplyCost": "new CurrencyCollection(Currency.Ring, 320L)"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/FeralDen.cs:11`
