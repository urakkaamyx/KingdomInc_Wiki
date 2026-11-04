# Skill tests and elemental resistances

Check probability, group checks, and the scope of resistance.

## Checks

Base success chance = clamp(stat ÷ difficulty, 5%, 95%). Skill-test traits modify this afterward. The four skill-critical traits each add 0.4 × trait quality for their matching stat; the final chance is not re-clamped to 95%. The random helper guarantees success when a final probability reaches 1.

Dungeon individual difficulty is integer StageDifficulty ÷ 4; group difficulty is integer StageDifficulty ÷ 3. Most group challenges let members try in order until one succeeds. Clear Rubble instead uses individual difficulty even though any member can save the group.

## Resistance

Fire, Shadow, and Poison resistance each use reduction = 0.3 + 0.2 × active trait quality, giving 50% at quality 1. The matching hazard multiplies its damage by 1 − reduction. Identical resistance traits keep the highest-quality source, not their sum.

Resistance is requested explicitly by particular hazards rather than universally applied to every elemental-sounding attack. Tank Shadow Damage computes Shadow resistance for its display but does not multiply the actual damage by it in this implementation. The formula contains no explicit upper clamp.

## Sources

- `Assets.Source.Items.Data/CombatantItemData.cs:139`
- `Assets.Source.Items.Data/CombatantItemData.cs:253`
- `Assets.Source.Adventure/AdventurerTrait.cs:664`
- `Assets.Source.Adventure/AdventurerTrait.cs:536`
- `Assets.Source.Adventure/QuestChallenge.cs:145`
- `Assets.Source.Adventure/DungeonProgress.cs:56`
- `SeededRandom.cs:78`
