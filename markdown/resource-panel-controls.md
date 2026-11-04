# Resource quotas and supplier configuration

Read resource demand and buy capacity without confusing it with item inventory.

## Quota panel

ResourcesMenu lists available resources except Farm resources and AdventureSupplies. Each row refreshes available capacity and demand, highlights demand red above supply, and offers the next quota increase at GamePlayer.GetResourceUpgrade’s current cost. Buying spends that collection and adds the quota with isUpgrade=true.

## Supplier choice

The selector shows the machine’s current resource first, then other resources available for its supply tag. Resource demand is live; available capacity is shown explicitly below 5000. Selection clears/rebuilds that resource machine’s IO and refreshes its label/icon.

## Costs and output warnings

Hover a resource for its description and per-resource collection cost where applicable. The world adapter shows queue count only above 1, hides it when Output Full is displayed, and marks blocked output when OutputPerSecond is zero. Capacity and demand are rate/quota information, not a count of loose items waiting in storage.

## Shortcut

The resource-window shortcut is visible only after unlock_supply_window and is omitted for Farm and AdventureSupplies.

## Sources

- `Assets.Behaviour.UI.Resources/ResourcesMenu.cs:16`
- `Assets.Behaviour.UI.Resources/ResourceQuotaRow.cs:37`
- `Assets.Behaviour.UI.Resources/SelectResourcePopup.cs:27`
- `Assets.Behaviour.UI.Resources/SelectResourceRow.cs:34`
- `Assets.Behaviour.Flow.Elements/WorldFlowResource.cs:37`
