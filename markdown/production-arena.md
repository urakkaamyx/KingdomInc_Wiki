# Arena battles, training, and rewards

The Arena trains combatants and converts completed bouts into currency.

## Entry and combat

Arena accepts any CombatantItemType in each of two one-item inputs. Eastern war stage 4 must be reached before its update processes entrants. A Worker starts fights automatically; otherwise a bout can be started manually once both slots are filled.

At the start, RewardMultiplier is the product of both combatants' Health01. Each unarmed HumanItemData halves it. Ticks occur every 2 ÷ Speed seconds. Both combatants take simultaneous random damage based on one tenth of the opponent's base damage, with a range from that amount ÷ 1.2 through × 1.2.

Normal bouts stop when a human is below 10% health or a nonhuman is dead. A dead human at the normal stop check is healed by a small random amount. Blood Sport instead continues until a death; if both are dead the code randomly heals one.

## Training is limited, combat is not

Only the first ten active fight ticks train the slots and cost the normal training energy. After the ten training ticks, combat damage continues until the health/death stop condition is met.

The AddTraining parameter per tick is 0.04, or 0.06 in Blood Sport with two nonhumans, or 0.08 when Blood Sport includes a human. AddTraining applies trait modifiers and actually increases quality by a random amount from half to the full modified parameter. Training is granted only to Adventurers or humans with ArenaCount zero. Energy cost starts at 3 per training tick and scales with 1 + ArenaCount for the eligible humans.

Output eligibility requires a living, nonexhausted human that is an Adventurer or has never completed Arena before. Eligible humans receive ActivityCompleted and an ArenaCount increase. Nonhumans are not output. Nonadventurer humans after their first Arena visit are also not output. Applicable Arena or ArenaWin advancements are then tested.

## Reward formula

Multiply the starting RewardMultiplier by 1 + 0.1 × Arena Cashier count. For each participant multiply by 1.2 if it is an Adventurer, or 1.1 for other humans. In Blood Sport, multiply by another 1.25 only when the resulting multiplier is above 1.

Currency selection checks sequential thresholds: above 1.5, a 25% Ducat roll; otherwise above 1.25, a 25% Ring roll; otherwise above 1.09, a 25% Crown roll; otherwise Gold. A failed earlier roll can still reach a later eligible currency roll.

Payout is round(10,000 × final multiplier ÷ chosen currency's gold equivalent). Required eligible output slots must have room before completion. Both slots then clear and the Arena waits a four-second cooldown.

## Sources

- `Assets.Source.Flow.Elements/Arena.cs:43`
- `Assets.Source.Flow.Elements/Arena.cs:135`
- `Assets.Source.Flow.Elements/Arena.cs:155`
- `Assets.Source.Flow.Elements/Arena.cs:162`
- `Assets.Source.Flow.Elements/Arena.cs:238`
- `Assets.Source.Flow.Elements/Arena.cs:260`
- `Assets.Source.Flow.Elements/Arena.cs:299`
- `Assets.Source.Flow.Elements/Arena.cs:339`
- `Assets.Source.Flow.Elements/Arena.cs:355`
- `Assets.Source.Items.Data/CombatantItemData.cs:340`
