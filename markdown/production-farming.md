# Farming and field expansion

Plots establish farm capacity; farm buildings harvest that capacity.

## Fields and quota

The field begins 3 columns wide and 2 rows high. Each cell can hold a selected unlocked farm resource. Every matching planted cell contributes that resource's configured PlotYield to its global production quota.

Farms are blocked until eastern war stage 1. Field quota is zero while blocked, and Farm buildings separately check the same war gate approximately once per second. A planted field establishes available capacity; a Farm building still queues and pays for harvested items.

## Expansion costs

A field expansion is priced from 12 Rings and 12 Crowns multiplied by a sum of escalating terms. UpgradeCount is current width + current height − 5. For a request of n new plots, the multiplier is the sum of growth^(UpgradeCount + i), for i from 0 through n − 1.

The normal growth is 1.2. Resource Cost Reduction prestige reduces the amount of that growth above 1. The farm data declares a maximum width of 6; field dimensions and selected cells are saved.

## Farm output

Each Farm is a standard ResourceElement tagged Farm, with a base desired speed of 1 × Speed while its war gate is open. All Farms harvesting the same crop share the crop quota. Farm Artisan quality and extra order cost follow the resource rules.

## Sources

- `Assets.Source.Player/FarmSettings.cs:11`
- `Assets.Source.Player/FarmSettings.cs:68`
- `Assets.Source.Player/FarmSettings.cs:96`
- `Assets.Source.Flow.Elements/Farm.cs:20`
- `Assets.Source.Flow.Elements/Farm.cs:42`
