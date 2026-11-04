# Nightmare adventure scaling and final rewards

How repeated endgame victories change Ironcrag Siege and Tomb of Sholrath.

## Active scaling

When Nightmare is active, Tomb of Sholrath uses these multipliers based on total NightmareCount N: stage difficulty ×(1 + 0.01N), stage health additionally ×(1 + 0.05N), and supply cost ×(1 + 0.1N). Difficulty is rounded first, then health is calculated and cast to a long after the extra health multiplier.

Because stage health already multiplies BaseHealth by the scaled difficulty, effective health grows from both the difficulty and dedicated health factors. Dungeon challenge checks and damage also rise with the scaled difficulty.

Ironcrag Siege is the endgame war. While Nightmare is active, its maximum progress uses ×(1 + 0.05N); enemy strength and damage use ×(1 + 0.01N). Its stage-completion branch still compares progress to the stage’s declared ProgressAmount, so do not interpret the scaled MaxProgress property as an unconditional replacement of every completion threshold.

## Reward readiness

Fragmented Nightmare rewards are ready while Nightmare is active, or for the very first victory when NightmareCount is zero. Their base reward is two items.

Distilled Nightmare is ready for the first victory regardless of activity state, or afterward when Nightmare is active and NightmareProgress exceeds 0.99. When ready it increases NightmareCount by one and subtracts one progress only if progress is at least 1.

A Distilled Nightmare reward resets Ironcrag’s final hold: a completed front is moved back to zero-based stage 3, and that stage’s progress is set to 10. The Tomb’s current availability requirement is final Ironcrag completion, so another attempt depends on restoring that war condition.

The first ready Distilled reward also opens the game’s victory popup. Reaching the last boss is therefore distinct from qualifying for every repeat reward.

## Sources

- `Assets.Source.Adventure.Dungeons/Endgame.cs:142`
- `Assets.Source.Adventure.Dungeons/Endgame.cs:147`
- `Assets.Source.Adventure.Dungeons/Endgame.cs:152`
- `Assets.Source.Adventure.Dungeons/Endgame.cs:128`
- `Assets.Source.Adventure/DungeonProgress.cs:41`
- `Assets.Source.Adventure/DungeonProgress.cs:314`
- `Assets.Source.Adventure/WarProgress.cs:41`
- `Assets.Source.Adventure/WarProgress.cs:248`
- `Assets.Source.Adventure.Rewards/FragmentedNightmareReward.cs:10`
- `Assets.Source.Adventure.Rewards/DistilledNightmareReward.cs:14`
- `Assets.Source.Adventure.Rewards/DistilledNightmareReward.cs:46`
