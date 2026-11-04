# Enchanting, engraving, and blessings

Enhancement slots, eligible inputs, and preservation of the original equipment.

## Slots and restrictions

Enhancements are stored by EnhancementType. Before Enhance Multiple technology, any existing enhancement blocks another enhancement. After the technology, the item may receive one of each enhancement type, but cannot receive a second of the same type.

Engraver recipes distinguish heavy armor, light or medium armor, weapons, and jewelry. Enchanter recipes use filters for weapons, shields, armor, food, and other recipe-specific targets. Shrine blessings distinguish weapons from nonweapon equipment. A valid item must also pass CanEnhance for that enhancement type.

## Applying an enhancement

An enhancement recipe returns the original item from reagent slot zero and adds an ItemEnhancementData object whose quality is the craft's rolled output quality. This preserves the item's identity and existing data.

For enhancements with AddQuality, the base item receives that fixed bonus plus a random value between (enhancement quality − 1)/2 and enhancement quality − 1. The item-quality enchant also adds Dark Essence Quality prestige to the fixed increase.

Enhancement result recipes disable bonus productivity progress, even though Overseer may be available in their upgrade list. New material recipes at the same stations still use their own recipe's normal productivity rules.

## Value and equipment

Equipment SellValue is its normal rounded base value × quality plus every enhancement's sell value. Enhancement stats are added to the equipment's base rolled stats. Filling all enhancement slots triggers the Full Enhance achievement.

## Sources

- `Assets.Source.Items.Data/EquipmentItemData.cs:44`
- `Assets.Source.Items.Data/EquipmentItemData.cs:105`
- `Assets.Source.Items.Data/EquipmentItemData.cs:131`
- `Assets.Source.Items/CraftingResult.cs:43`
- `Assets.Source.Flow.Elements/RecipeElement.cs:166`
- `Assets.Source.Items.Recipes/Engraver.cs:10`
- `Assets.Source.Items.Recipes/Enchanter.cs:11`
- `Assets.Source.Items.Recipes/Shrine.cs:17`
