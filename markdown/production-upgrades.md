# Workers, upgrades, stacking, and refunds

The common upgrade system used by production and service buildings.

## Worker and speed

The first Worker enables CanAutoCraft and adds no speed bonus. Each additional Worker of that exact type adds 0.5 Speed. Speed bonuses add to a base of 1, then the result is multiplied by StackSize.

Repeat Workers are permitted on resource buildings, recipe buildings, Shops, Forests, Training Grounds, and Disenchanters. Other building types normally allow only one Worker. Some services, including Inn, Luxury Shop, and Mercenary Guild, are intrinsically automatic.

## Upgrade slots and costs

Technology grants upgrade slots and the set of available upgrades separately for each building type. Upgrade effects are recalculated from the installed upgrades. The nth copy of a particular upgrade type is counted independently of other types.

The shared upgrade price uses a base of 858, the upgrade's CostMultiplier, and a ×1.5 price factor for each existing upgrade of the same exact type. Its cost tier is the larger of the upgrade's minimum tier and building cost tier plus that existing count. Currency conversion, rounding, and deterministic identifier variation also affect the displayed price.

## Stacking and construction prices

The base building price uses 780 and its configured CostMultiplier. Repeated Resource buildings use a 1.04 count multiplier, Crafting buildings 1.02, and Consumption buildings 1.10. Utility buildings use 1.00. Counts include stack sizes across all diagrams.

The declared maximum stack size is five. Stackable families include resources, forests, recipes, and Shops. Stacking multiplies computed Speed; it does not automatically enlarge their IO buffers or a Shop's gold capacity.

## Refunds and artisans

Building refunds are half the previous-count purchase price plus half-price refunds for installed upgrades, with repeated upgrades accounted for by type. Copy prices include the copied stack and installed upgrades.

Artisans add 0.1 Quality, with the ordinary Artisan availability requiring forest war stage 2. Training Artisan also subtracts 0.2 Speed per copy. Resource Artisan variants apply the resource-specific extra production costs described on the resource pages.

## Sources

- `Assets.Source.Flow/FlowElement.cs:14`
- `Assets.Source.Flow/FlowElement.cs:156`
- `Assets.Source.Flow/FlowElement.cs:303`
- `Assets.Source.Flow/FlowUpgrade.cs:44`
- `Assets.Source.Flow.Upgrades/Worker.cs:15`
- `Assets.Source.Flow.Upgrades/Worker.cs:33`
- `Assets.Source.Flow.Upgrades/Artisan.cs:23`
- `Assets.Source.Flow.Upgrades/TrainingArtisan.cs:18`
