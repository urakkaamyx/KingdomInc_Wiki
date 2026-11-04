# Energy, death, and dungeon limit breaks

What exhaustion removes, how recovery works, and when Faith can prolong an expedition.

## Health and exhaustion

Health and Energy initialize at full fractions. A combatant is Dead when its health fraction is zero. A character with a positive energy pool is Exhausted at zero energy unless its LimitBreak flag is active. Nonhumans normally have no energy pool, and ordinary humans with zero base Energy ignore Energy equipment.

Energy loss is clamped to the 0–100% fraction. Positive loss passes through energy-loss traits; negative loss restores energy without those modifiers. Healing passes through healing-taken traits and clamps to maximum health. No separate persistent injury-status system is present in these core combatant classes; remaining health is the injury measure.

Quest and training systems remove exhausted participants instead of automatically resting them. Arena only returns living, non-Exhausted eligible humans. War removes soldiers on death. Dungeon parties are consumed by defeat, victory, or retreat rather than sent through a survivor output.

## Limit Break

With Dungeon Limit Break, a member at zero energy can remain active while other party members still have energy. Its human combat power is reduced to 75%. If the whole party reaches zero energy, the run records a wipe and resets even with Limit Break.

With the Faith-based second limit break, an energy-loss call that reaches zero tries to spend round(requested energy loss × 5) Faith. On success it sets the member to exactly 1 CurrentEnergy. This is not a full refill and is not priced only on the missing portion. It can be invoked by stage costs or challenge losses.

A stage completion deducts energy before CheckForLimitBreak; this check can remove zero-energy members or end a fully exhausted run. Consumables that restore energy during later healing hooks cannot be assumed to rescue members already removed by earlier checks.

## Completion recovery

ActivityCompleted raises Level, clears temporary buffs, and fully heals full Healers; it does not restore Energy. Potions, energy amulets, and energy scrolls supply explicit recovery effects. Other humans retain their remaining health when returned from training, quest, or arena activities.

## Sources

- `Assets.Source.Items.Data/CombatantItemData.cs:42`
- `Assets.Source.Items.Data/CombatantItemData.cs:44`
- `Assets.Source.Items.Data/CombatantItemData.cs:181`
- `Assets.Source.Items.Data/CombatantItemData.cs:190`
- `Assets.Source.Items.Data/CombatantItemData.cs:207`
- `Assets.Source.Adventure/DungeonProgress.cs:237`
- `Assets.Source.Items.Data/HumanItemData.cs:314`
- `Assets.Source.Items.Data/HumanItemData.cs:244`
- `Assets.Source.Flow.Upgrades/DungeonLimitBreak2.cs:8`
