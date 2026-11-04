# Traits and party buffs

Where trait strength comes from and how repeated effects combine.

## Sources

Traits come from archetypes, classes, equipment, enhancements, and temporary party buffs. Archetype traits use character quality. Declared class traits are instantiated at quality 1, so training does not directly strengthen their percentage formulas; it still improves underlying stats.

Equipment traits use item quality; enhancement traits use enhancement quality. A group buff retains its source trait quality. Repeated copies of the same trait keep only the highest quality. Different traits modify their shared value in stored order.

## Party application and clearing

At dungeon start every member applies group effects to every member, including themselves. Quest and War Effort intake apply the current members’ effects to the incoming member. Thus a newly added aura source should not be assumed to buff all earlier quest or war members retroactively.

ActivityCompleted increments Level and refreshes traits while clearing temporary buffs. Full Healers are healed completely. The Level counter itself is not an automatic per-level stat formula here; quality training is separate.

Equipment changes refresh traits while retaining stored buffs. Removing a buff removes one stored entry; consumed-aura behavior also depends on refresh and cleanup calls.

## Sources

- `Assets.Source.Items.Data/HumanItemData.cs:274`
- `Assets.Source.Items.Data/CombatantItemData.cs:304`
- `Assets.Source.Adventure/ActiveTraitSet.cs:27`
- `Assets.Source.Adventure/ActiveTrait.cs:96`
- `Assets.Source.Items.Data/HumanItemData.cs:314`
- `Assets.Source.Flow.Elements/QuestBoard.cs:151`
- `Assets.Source.Flow.Elements/WarEffort.cs:100`
