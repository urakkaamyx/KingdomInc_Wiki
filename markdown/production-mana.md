# Disenchanting and mana production

Equipment converts into mana, with quality and enhancement adjustments.

## Eligible equipment and timing

A Disenchanter accepts positive-value, sellable EquipmentItemType except Food, Potion, and Scroll slots. The declared 1.04 quality constant is not used as an acceptance gate: low-quality equipment is accepted with a payout penalty.

An item takes 1 ÷ Speed seconds to process. Mana is stored locally, with no capacity check in this class. A Worker collects whenever the local balance is positive; manual collection transfers all stored Mana.

## Mana formula

Start with SellValue and a conversion multiplier of 0.9 ÷ 11. If item Quality is below 1.04, multiply by 0.75. For equipment without any enhancement, multiply by another 0.75. If it has an Enchant enhancement, subtract half that enhancement's sell value from the value being converted.

Item ManaValue is the ceiling of adjusted value × conversion multiplier. The Disenchanter then rounds ManaValue × (1 + 0.1 × Mana Cashier count). Each Mana Passive upgrade adds three local Mana per second regardless of item supply.

An ordinary quality-1 unenhanced item receives both 0.75 penalties. Enhancements and base quality are separate tests; a Blessing or Engraving is enough to avoid the no-enhancement penalty.

## Sources

- `Assets.Source.Flow.Elements/Disenchanter.cs:35`
- `Assets.Source.Flow.Elements/Disenchanter.cs:49`
- `Assets.Source.Flow.Elements/Disenchanter.cs:56`
- `Assets.Source.Flow.Elements/Disenchanter.cs:118`
- `Assets.Source.Items/InventoryItem.cs:27`
