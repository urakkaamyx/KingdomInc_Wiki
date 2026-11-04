# Tanks, healers, and party formation

Tank qualification, targeting odds, and automatic healing.

## Tank role

Fighter-archetype humans qualify as Tanks with an offhand Shield and Heavy armor qualification. This includes Fighter-derived classes. Tank reduces damage taken by 25%. The first qualifying member is the dungeon’s designated tank.

Ordinary dungeon hits select that tank with 85% probability on bosses or 65% on other stages, otherwise they select a random member. The random selection can also choose the tank. Scripted tank hazards use their own direct selection.

The displayed distance rank puts Tanks first, then melee or unarmed humans, then ranged humans. Ordinary targeting uses the probabilities above rather than a general front-row shield rule.

## Standard healing

Base healing starts at Wisdom. If the caster has Healer and combat power exceeds Wisdom, add half the difference using integer division. Apply healing-done multipliers and round. The normal spell heals base healing ÷ 10 using integer division, with the recipient’s healing-taken traits applied afterward.

It chooses the eligible member with the lowest health fraction; full-health and Exhausted members are excluded. A dungeon uses its first Healer, and can stay on a cleared stage while that caster continues finding wounded targets. The final stage ends before this healing phase.

Quest progress ticks have a 25% chance to request that spell. Wars allow a rounded one-Healer-per-five-soldiers limit, clamped to 1–10, randomly excluding excess healers each tick. Inquisitor has Minor Healer rather than the full role.

## Sources

- `Assets.Source.Items.Data/HumanItemData.cs:285`
- `Assets.Source.Items.Data/HumanItemData.cs:69`
- `Assets.Source.Adventure/DungeonProgress.cs:333`
- `Assets.Source.Adventure/DungeonProgress.cs:364`
- `Assets.Source.Items.Data/HumanItemData.cs:397`
- `Assets.Source.Items.Data/CombatantItemData.cs:263`
- `Assets.Source.Adventure/WarProgress.cs:171`
- `Assets.Source.Adventure/AdventurerTrait.cs:71`
- `Assets.Source.Items.Impl/Adventurers.cs:645`
