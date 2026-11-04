# Training Grounds and diminishing returns

Ten training ticks improve humans while consuming energy.

## Training cycle

Training Grounds accepts HumanItemType. With a Worker, it ticks on a shared timer every 2 ÷ Speed seconds. Each admitted character begins with ten ticks remaining. A manual click independently gives each occupied slot a 50% chance of one additional tick.

Each training tick passes Parent.QualityPerTick × building Quality × repetition factor to AddTraining. QualityPerTick is 0.02 without a training dummy and 0.04 with one. AddTraining first applies trait modifiers, then actually increases item quality by a random amount between half and the full modified parameter; the upper endpoint is excluded.

## Repeating training

Adventurers always use repetition factor 1. Other humans use 1 on their first training visit, 0.5 on their second, and 0 afterwards. Completing a stay calls ActivityCompleted and increments TrainingCount for Adventurers, or for other humans while TrainingCount is below 3.

Energy lost per tick is 2 × (1 + TrainingCount), halved when the food technology is in use and the character has equipped food. Exhausted characters are removed from the training contents instead of output.

Training Grounds Food makes automatic ticks perform a second tick for a character with food, and equipped food is consumed when the stay completes. Specialization technology checks eligible TrainingGrounds advancements at the halfway tick if the character has not exhausted.

## Dummy and capacity caveat

Training Grounds Dummy adds an input for nonhuman combatants. A dummy doubles base training gain; trainees that still have positive repetition factor damage it by base damage ÷ 10 each tick. A dead dummy is removed.

The displayed Capacity property is three plus two possible slot technologies. However, GetFreeSlot scans the entire five-element Contents array rather than checking Capacity. This implementation can admit characters into backing slots beyond the displayed capacity; the distinction is relevant when comparing observed behavior with the menu.

Boot Camp has a 10% chance to award one Medal when an exactly quality-1 conscript enters.

## Sources

- `Assets.Source.Flow.Elements/TrainingGrounds.cs:25`
- `Assets.Source.Flow.Elements/TrainingGrounds.cs:133`
- `Assets.Source.Flow.Elements/TrainingGrounds.cs:151`
- `Assets.Source.Flow.Elements/TrainingGrounds.cs:165`
- `Assets.Source.Flow.Elements/TrainingGroundsSlot.cs:41`
- `Assets.Source.Items.Data/CombatantItemData.cs:340`
