# Resource quotas and harvesting

The shared capacity rules behind mines, suppliers, farms, and recruitment.

## Quota is shared production capacity

Each resource has a global available quota. Approximately every 0.1 seconds the player totals the desired output of every matching resource building in every diagram. If demand exceeds quota, all those buildings receive the same multiplier: quota divided by total demand. Otherwise the multiplier is 1.

Desired output is zero when a resource building has no queued work or its normal progress is already at least 1. A completed building waiting for output space stops requesting further normal progress. Quota utilization shown in the interface averages recorded demand samples.

## Production and payment

A resource building queues and pays for a normal item before producing it. An automatic Worker queues a new order when the normal queue becomes empty; manual clicks can queue up to five paid orders. Failed payment leaves the order unqueued.

Actual progress per second is building OutputPerSecond multiplied by the resource quota multiplier. Most resource buildings start at 1 × Speed items per second; Barracks and Adventurers Guild use 0.5 × Speed. Output is blocked when its five-place buffer is full.

## Bonus output and quality

Productivity advances a separate counter using the same quota-adjusted production progress. When the bonus counter reaches 1, the next available output consumes bonus progress instead of normal progress or a paid queued order.

Resource quality is sampled between square root of building Quality and building Quality. Human recruits also receive the Human Quality prestige bonus before their character data is initialized.

## Quota upgrades

A quota upgrade adds the resource's configured QuotaAmount. Its price is QuotaBaseCost multiplied by the resource's quota growth factor raised to the number of previous quota upgrades. Resource Cost Reduction prestige reduces only the amount above 1 in that growth factor.

The iron-ore quest discount multiplies quota upgrade prices by 0.25 × 0.95 raised to the repeat discount counter. Resource Artisan variants add a gold surcharge per normal order: resource value × 0.2 per upgrade for ordinary resources, or × 2 per upgrade for recruits.

## Sources

- `Assets.Source.Player/GamePlayer.cs:338`
- `Assets.Source.Player/GamePlayer.cs:410`
- `Assets.Source.Flow.Elements/ResourceElement.cs:62`
- `Assets.Source.Flow.Elements/ResourceElement.cs:98`
- `Assets.Source.Flow.Elements/ResourceElement.cs:177`
- `Assets.Source.Flow.Elements/ResourceElement.cs:203`
