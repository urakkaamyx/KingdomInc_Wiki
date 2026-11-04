# Nightmares and the endgame loop

Distilled nightmares, fragments, distiller charging, and enemy scaling.

## Earning nightmares

The endgame dungeon final boss lists FragmentedNightmareReward and DistilledNightmareReward. Distilled reward is ready when NightmareActive and NightmareProgress>0.99, or unconditionally when total nightmares are zero. Receiving it increases the total, updates the Steam stat, subtracts 1 charge if charge≥1, partially resets North war, and opens the victory popup for the first nightmare.

Fragmented reward creates fragmented_nightmare with chance 1 and amount 2. It is enabled while nightmare mode is active, or while the total is zero. The quest overloads for both rewards are empty; their dungeon overloads perform the reward.

## The distiller

nightmare_distiller follows dungeon_endgame and additionally checks that the last endgame CompletedCount entry is positive. The machine class is NightmareCollector, displayed as nightmare_distiller. Its one-item input consumes nightmare_collector items.

Below full charge, each consumed item adds 1/floor(sqrt(totalNightmares)). Values between 0.985 and 1 are snapped to 1. At 1–3 nightmares each item fills a charge, at 4–8 it fills half, and at 9–15 it fills one-third. The machine Update itself does not check NightmareActive; reward eligibility and enemy multipliers do.

## Endgame scaling

| Value | Multiplier at total count N |
| --- | --- |
| Dungeon health | 1+0.05N |
| Dungeon damage | 1+0.01N |
| Dungeon cost | 1+0.10N |
| War enemy health/strength | 1+0.05N |
| War damage | 1+0.01N |

## Toggle and repeat access

The distiller UI toggles NightmareActive. Difficulty readers require IsEndgame and NightmareActive. A distilled reward changes North war from stage index 4 back to 3; when at index 3, progress is set to 10. This partial reset requires the final war section to be secured again, independently of ascension.

## Sources

- `Assets.Source.Adventure.Rewards/DistilledNightmareReward.cs:14`
- `Assets.Source.Adventure.Rewards/DistilledNightmareReward.cs:46`
- `Assets.Source.Adventure.Rewards/FragmentedNightmareReward.cs:36`
- `Assets.Source.Flow.Elements/NightmareCollector.cs:19`
- `Assets.Source.Flow.Elements/NightmareCollector.cs:35`
- `Assets.Behaviour.Flow.Elements/WorldFlowNightmareCollector.cs:34`
- `Assets.Source.Player.Tech/T11Shrine.cs:254`
- `Assets.Source.Adventure.Dungeons/Endgame.cs:128`
- `Assets.Source.Adventure/DungeonProgress.cs:46`
- `Assets.Source.Adventure/WarProgress.cs:46`
