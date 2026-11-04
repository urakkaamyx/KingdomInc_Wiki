# Mines and supply depots

Choosing raw materials and paying for resource orders.

## Mine

A Mine accepts resource selections tagged Mine. Its displayed name changes for iron ore, sapphire, gold ore, and silver ore. The first Mine is free; later Mines use the normal Resource building price escalation.

A Mine shares its resource's quota with all other buildings producing that resource. Building more Mines cannot by itself raise the global quota.

## Supply Depot and Adventure Supplies

Supply Depot selects resources tagged Supply and is purchased with Gold. Adventure Supplies selects resources tagged AdventureSupplies and is purchased with Gold and Rings. Both use the standard ResourceElement order, quota, five-item output, quality, and productivity systems.

Resource selection is restricted to the currently available resources. Quota must be positive for ordinary resources to appear in that list; unlocked farm resources are a special exception.

## Sources

- `Assets.Source.Flow.Elements/Mine.cs:16`
- `Assets.Source.Flow.Elements/Mine.cs:33`
- `Assets.Source.Flow.Elements/SupplyDepot.cs:18`
- `Assets.Source.Flow.Elements/AdventureSupplies.cs:18`
- `Assets.Source.Flow.Elements/ResourceElement.cs:223`
- `Assets.Source.Player/GamePlayer.cs:395`
