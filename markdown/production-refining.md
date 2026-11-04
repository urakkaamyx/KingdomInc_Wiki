# Refining and destruction risk

A Refiner trades items and optional Mana for incremental quality.

## Cycle and eligibility

A Refiner processes a buffered item in three seconds and requires its output slot to be free before resolving. Its cycle does not use the building's Speed. Failure consumes the item permanently; success returns the same item with higher quality.

Without the appropriate Mana technology mode, combatants are rejected. With Mana mode and Refiner Demon, nonhuman combatants become eligible; Refiner Human allows all items while Mana mode is active. Refiner Mana defaults Mana use on for newly created refiners unless a copied preference overrides it.

## Failure and Mana formulas

Without Mana, failure chance is min(max(Quality − 1, 0.25) × human factor, 0.95), where the human factor is 2 for HumanItemType and 1 otherwise. With Mana the max(...) value is divided by four before the human factor and 95% cap.

Mana cost is round(SellValue × 0.25 ÷ 11). If payment fails, the item still resolves using the non-Mana failure chance. At quality 1, ordinary items fail 25% without Mana or 6.25% with paid Mana; humans fail 50% or 12.5%.

## Success

A successful refine adds a random 0.05 to 0.10 quality. Critical Craft technology adds an independent 1% chance to double that increase. Increasing quality rerolls base equipment stats through SetQuality.

The Refiner uses no automatic Worker check. Connecting a loop can repeatedly refine the same item, but its failure probability generally rises with quality and eventually reaches the cap.

## Sources

- `Assets.Source.Flow.Elements/Refiner.cs:43`
- `Assets.Source.Flow.Elements/Refiner.cs:77`
- `Assets.Source.Flow.Elements/Refiner.cs:90`
- `Assets.Source.Flow.Elements/Refiner.cs:145`
- `Assets.Source.Flow.Elements/Refiner.cs:160`
- `Assets.Source.Items.Data/EquipmentItemData.cs:57`
