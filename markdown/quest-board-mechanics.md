# Quest Board progress and repeat costs

Five-adventurer work groups, progress-based hazards, energy, training, and blocked outputs.

## Progress

A Quest Board holds up to five adventurers and updates once per second. Each living, non-Exhausted participant contributes base damage ÷ its individually adjusted quest difficulty. For quests with DurationMultiplier exactly 1, the contribution is capped at 2 per participant per update.

A contribution below 1 is penalized: the adventurer takes a random damage roll around 0.5 ÷ its original contribution (range ÷1.5 to ×1.5), then contributes only half the original amount. This makes badly underpowered adventurers both slower and vulnerable.

Progress is shared. Challenges and trait hooks execute once for each whole progress boundary crossed, not once per real second. Faster groups therefore run more hazard and energy ticks per second while finishing sooner. Progress may overshoot the target.

## Energy and completion

Each whole progress tick costs EnergyPerTick × (1 + that adventurer’s QuestCount), before positive-energy-loss trait modifiers. The default EnergyPerTick is 0.2. Hazards may add to it. A 25% chance on each progress tick asks the first Healer to cast.

Completion waits until every output buffer is empty. It subtracts the quest’s current TickDuration from shared progress, grants first or repeat rewards, increments global completion count, then returns all current members through the adventurer output.

Each returned member receives the quest’s completion callback, ActivityCompleted, +1 QuestCount, and a random half-to-full quality gain from TrainingAdded × training upgrade multiplier. Default TrainingAdded is 0.12; each Quest Training upgrade adds +0.5 to the multiplier. Coin upgrades add +0.1 each to the currency multiplier.

## Repeated duration

TickDuration = round(BaseDuration × DurationMultiplier^global completion count). Only quests with a multiplier other than 1 grow this way, and those quests also bypass the normal contribution cap of 2. This count belongs to the quest metadata, so different boards share its first-clear and repeat history.

Dead or Exhausted participants are removed on progress processing. Completion checks and per-progress hazard loops have a specific ordering; avoid assuming survival and removal happen immediately after each individual hazard.

## Sources

- `Assets.Source.Flow.Elements/QuestBoard.cs:166`
- `Assets.Source.Flow.Elements/QuestBoard.cs:223`
- `Assets.Source.Flow.Elements/QuestBoard.cs:83`
- `Assets.Source.Adventure/QuestProgress.cs:38`
- `Assets.Source.Adventure/QuestProgress.cs:58`
- `Assets.Source.Adventure/QuestProgress.cs:63`
- `Assets.Source.Adventure/Quest.cs:62`
