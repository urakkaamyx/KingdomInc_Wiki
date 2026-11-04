# Shrines, prayer, and Faith

Clerics generate Faith, gain training, and lose increasing energy.

## Prayer inputs and rewards

Prayer recipes accept any HumanItemType whose Archetype is Cleric. Prayer 1 uses that cleric alone, has a threefold crafting-time multiplier, grants 0.1 training through AddTraining, and produces Faith from a base amount of 27.

Prayer 2 also consumes blessed prayer beads, has a sixfold crafting-time multiplier, grants 0.3 training, and produces Faith from a base amount of 214. Both suppress productivity with BaseProductivity −999.

## Cleric fatigue and Wisdom

On returning the cleric, OutputCleric(addQL) passes addQL to AddTraining, then costs addQL × 250 × (1 + SpecialCount) energy and increments SpecialCount. AddTraining applies trait modifiers and increases actual item quality by a random amount from half to the full modified training parameter. If the cleric is exhausted it is not returned to the output.

Faith is round(base Faith × craft output quality × max(1, cleric Wisdom ÷ 350)). Wisdom below 350 does not reduce the base reward, while higher Wisdom scales it upward. Faith is credited directly during recipe completion.

## Other Shrine work

The Shrine spends Faith on blessed prayer beads, indulgence, weapon or equipment blessings, pontiff ring, martyr relic, class transformations, purified technology, upgraded weapons, and cleansed nightmare.

Blessed Arms costs 195 Faith and accepts a weapon that can receive a Blessing; Blessed Equipment costs 145 Faith and accepts nonweapon equipment eligible for a Blessing. Prayer beads cost 84 Faith, indulgence 101, pontiff ring 565, and martyr relic 305 in addition to their listed material inputs.

Purified Tech costs 23 Faith and converts heretic tech with a 10% purified-tech result and 90% return-heretic-tech result. It also suppresses productivity. Cleansed Nightmare costs 1,298 Faith and one reconstructed nightmare.

## Sources

- `Assets.Source.Flow.Elements/Shrine.cs:14`
- `Assets.Source.Items.Recipes/Shrine.cs:17`
- `Assets.Source.Items.Recipes/Shrine.cs:46`
- `Assets.Source.Items.Recipes/Shrine.cs:77`
- `Assets.Source.Items.Recipes/Shrine.cs:185`
- `Assets.Source.Items.Recipes/Shrine.cs:354`
- `Assets.Source.Items.Recipes/Shrine.cs:370`
- `Assets.Source.Items.Recipes/Shrine.cs:385`
- `Assets.Source.Items.Data/CombatantItemData.cs:340`
