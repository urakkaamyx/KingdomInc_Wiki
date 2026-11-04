# Ironcrag Siege

A hidden army has struck at the heart of Yensburg, pouring from the catacombs below the city and establishing control over the wealthy northern districts.

## Campaign

A hidden army has struck at the heart of Yensburg, pouring from the catacombs below the city and establishing control over the wealthy northern districts.

## Stages

| Stage | Progress | Enemy damage | Starting strength | Ending strength |
| --- | --- | --- | --- | --- |
| [The Old Guildhouse](war-stage-north-1.md) | 100 | 42 | 12000 | 14000 |
| [Deadrock Pass](war-stage-north-2.md) | 150 | 44 | 14000 | 17000 |
| [Ironcrag Summit](war-stage-north-3.md) | 200 | 46 | 17000 | 19000 |
| [Pinnacle Ruins](war-stage-north-4.md) | 250 | 47 | 19000 | 21000 |

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@war_north\"",
  "Description": "\"@war_north_desc\"",
  "IconName": "\"Icons2_68\"",
  "EnemyIconName": "\"Icons2_68\"",
  "MedalsMultiplier": "2f",
  "IsEndgame": "true",
  "CanProgress": "() => GamePlayer.Current.HasWarStage(\"yensburg\", 4)",
  "ProgressBlockedReason": "\"@war_north_blocked\""
}
```

</details>

## Sources

- `Assets.Source.Adventure.Wars/North.cs:9`
