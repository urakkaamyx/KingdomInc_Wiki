# Item quality and critical crafting

How ingredient quality, artisans, equipment rolls, and critical crafts interact.

## Craft quality formula

Let A be the average quality of all input items whose reagent slots affect quality; use A = 1 if none qualify. Let B be the building's Quality stat. Set H = B + A − 1. If H < 1, output quality is exactly H. Otherwise output quality is sampled from (A + H)/2 through H.

For example, average ingredient quality 1.20 and building Quality 1.10 give an output range of 1.25 to 1.30. A plain building with B = 1 preserves uniform ingredient quality. New equipment additionally receives the Equipment Quality prestige bonus.

## Critical craft

With Critical Craft technology, each output quality roll has a 1% chance to add its rolled distance above the minimum a second time. A critical craft is not simply a flat quality multiplier and does nothing when the roll equals the minimum.

Inventory quality values less than 0.01 away from 1 are snapped to exactly 1. Ordinary item sell value is rounded BaseValue × Quality; equipment adds the sell values of its enhancements.

## Equipment stat rolls

Each equipment base stat rolls from floor(base stat × 0.9 × item quality) up to, but excluding, ceil(base stat × 1.1 × item quality), unless both bounds are equal. Updating quality clears and rerolls these base equipment stats, so a Refiner or quality enhancement can change the rolls as well as the quality number.

Artisan upgrades add 0.1 to building Quality per copy. Ordinary crafting Artisans also add 10% of the recipe base value per upgrade to per-craft costs, converted into each existing cost currency; recipes without an existing currency cost get a gold surcharge.

## Sources

- `Assets.Source.Flow.Elements/RecipeElement.cs:331`
- `Assets.Source.Flow.Elements/RecipeElement.cs:364`
- `Assets.Source.Flow.Elements/RecipeElement.cs:67`
- `Assets.Source.Items/CraftingResult.cs:67`
- `Assets.Source.Items/InventoryItem.cs:73`
- `Assets.Source.Items/ItemType.cs:292`
- `Assets.Source.Items.Type/EquipmentItemType.cs:43`
- `Assets.Source.Items.Data/EquipmentItemData.cs:57`
- `SeededRandom.cs:41`
