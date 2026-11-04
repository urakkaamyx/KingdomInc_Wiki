# Forests and forest crews

Crew allocation, harvest capacity, and workforce costs.

## Crew roles and war gate

The forest workforce has Unassigned, Forager, Logger, and Hunter roles. Assigning workers to an active role consumes the same number of unassigned workers; removing them returns that number to the unassigned pool.

Harvesting is blocked until forest war stage 1. Each forest resource defines its worker role and WorkersPerItem requirement. Forest buildings requesting the same role compete for that role's assigned crew.

## Capacity formula

For each role, desired workforce is the sum of each active forest's desired items per second × that resource's WorkersPerItem. If demand is above assigned workers, the production multiplier is assigned workers divided by demand. Otherwise it is 1. Actual building output is Speed × that role multiplier.

Forest orders are paid when queued and have the same five-order manual queue, separate productivity counter, and five-item output buffer as ordinary resource buildings. Quality is sampled between square root of Quality and Quality. Each Forest Artisan adds 20% of resource value in extra gold to each paid order.

## Buying workers

Base worker price is 12 Requisition and 12 Medals. The price multiplier grows by 1.08 raised to total workers, including unassigned workers. Resource Cost Reduction prestige reduces the growth above 1.

The forest-worker quest discount multiplies price by 0.5 × 0.95 raised to its repeat counter. Forest Workforce technology supplies an additional ×0.5 multiplier.

## Sources

- `Assets.Source.Player/ForestSettings.cs:14`
- `Assets.Source.Player/ForestSettings.cs:53`
- `Assets.Source.Player/ForestSettings.cs:70`
- `Assets.Source.Player/ForestSettings.cs:131`
- `Assets.Source.Flow.Elements/Forest.cs:65`
- `Assets.Source.Flow.Elements/Forest.cs:138`
