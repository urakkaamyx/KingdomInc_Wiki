# Crafting workshops and their roles

The recipe stations and the shared rules they use.

## Station families

Forge, Blacksmith, Tailor, Leatherworker, Carpenter, Engraver, Campfire, Enchanter, Butcher, Kitchen, Jeweler, Summoning Circle, Alchemist, Inventor, Scribe, Shrine, Graveyard, and Necromancer all derive from RecipeElement. Their recipes use the shared timing, input quality, manual crafting, worker, and output-blocking rules.

Each station normally offers only its own RecipeTag. The Kitchen is the exception: its recipe menu also offers Campfire recipes, and its computed Speed is doubled after upgrades. This makes it a faster replacement for campfire cooking as well as the station for kitchen-specific meals.

## Purchase currencies

Forge and Blacksmith use Gold. Tailor, Leatherworker, and Carpenter use Gold and Requisition. Campfire and Engraver use Gold and Medals. Enchanter, Butcher, and Kitchen use Gold and Rings. Jeweler, Summoning Circle, Alchemist, Inventor, Scribe, Shrine, Graveyard, and Necromancer use Gold and Ducats.

The first Forge is free. Crafting stations are stackable; stacking increases Speed, while individual recipe unlocks and per-craft currency costs remain relevant.

## Sources

- `Assets.Source.Items/CraftingRecipe.cs:130`
- `Assets.Source.Flow.Elements/Kitchen.cs:14`
- `Assets.Source.Flow.Elements/Kitchen.cs:23`
- `Assets.Source.Flow.Elements/Forge.cs:25`
- `Assets.Source.Flow.Elements/RecipeElement.cs:56`
