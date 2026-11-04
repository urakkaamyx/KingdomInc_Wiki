# Arena combat and training

Damage, bout-ending conditions, training ticks, and survivor outputs.

## Attacks

Arena accepts two combatants and its normal update is blocked until Eastern war stage 4 is held. Each fighter applies group buffs only to itself. Attacks occur every 2 ÷ Speed seconds.

Each base damage is integer-divided by 10, then rolled from that value ÷ 1.2 to ×1.2 before armor and damage-taken traits. Both attack values are calculated before damage is applied. Trait hooks run after both hits.

## Ending a fight

Normal bouts end when a human is below 10% health or a nonhuman dies. Humans that reached zero in normal mode receive a small 2–4 health heal at the next stopping check. Blood Sport waits for a death; if both die, one randomly receives the small heal.

The 10-tick counter limits training and energy deductions, not total bout duration. After it reaches zero, attacks continue until a health ending condition. Opponents whose damage rounds to zero or whose healing outpaces damage may stall.

Eligible humans gain a random half-to-full share of the quality request for each of those first 10 attacks. They pay 3 × (1 + ArenaCount) Energy. Adventurers stay eligible across bouts; ordinary humans train only on their first. Other combatants pay the base energy cost when they have an energy pool.

| Mode | QualityPerTick request |
| --- | --- |
| Normal | 0.04 |
| Blood Sport with any human | 0.08 |
| Blood Sport with neither human | 0.06; actual quality gain still requires an eligible human |

## Outputs

Only living, non-Exhausted humans return: adventurers repeatedly, ordinary humans only from their first arena visit. Resolution waits for eligible outputs to have room. Returning humans receive ActivityCompleted and ArenaCount increases.

The winner uses higher health fraction; ties select slot 2. Arena and ArenaWin advancement routes are checked in declaration order after output handling. The bout then pays its audience reward and clears both slots.

## Sources

- `Assets.Source.Flow.Elements/Arena.cs:135`
- `Assets.Source.Flow.Elements/Arena.cs:173`
- `Assets.Source.Flow.Elements/Arena.cs:240`
- `Assets.Source.Flow.Elements/Arena.cs:201`
- `Assets.Source.Flow.Elements/Arena.cs:355`
- `Assets.Source.Flow.Elements/Arena.cs:296`
