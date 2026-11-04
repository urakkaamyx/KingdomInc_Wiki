# The in-game item encyclopedia

Find an item’s sources, recipes, and configured machine shortcuts.

## Unlock-aware item list

ItemMenu builds rows from ItemType.Unlocked. Clicking expands a row; expanding another collapses the previous row. Search requires all words in the translated item name, case-insensitively. It searches names rather than every recipe description.

## Sources and uses

An expanded row lists item description, crafting recipes producing it, resource suppliers, Forest, source quests/dungeons, training, or Arena where applicable. A second list shows recipes that consume it. Empty categories show a no-source/no-recipe message. Source lists are populated lazily when first expanded.

## Build directly from a source

Click or drag an available source entry to buy a machine preconfigured for that recipe/resource/quest/dungeon. Affordability is checked before the purchase ghost opens. Locked entries display their research requirement if available, otherwise a generic locked label. An item appearing in the encyclopedia does not grant every recipe that uses it.

## Implementation detail affecting expectations

ItemMenu keeps built rows and toggles their visibility during search. Blank active search returns early, rather than explicitly restoring every row; turning search off calls ShowAll. Recipe availability and dungeon unlock sets independently control whether a source can be placed.

## Sources

- `Assets.Behaviour.UI.ItemList/ItemMenu.cs:34`
- `Assets.Behaviour.UI.ItemList/ItemMenuRow.cs:57`
- `Assets.Behaviour.UI.ItemList/ItemMenuRecipe.cs:39`
