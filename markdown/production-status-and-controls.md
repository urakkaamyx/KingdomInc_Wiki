# Production status, routing buttons, and recent results

Read sales, refinery results, buffers, and the small controls built into machines.

## Sales and disenchanting

Shop shows collected Gold capped by MaxGold and a recent-sales tooltip with item quality and received value. Restaurant and Luxury Shop show Gold plus Crowns; Mercenary Guild shows Gold plus Ducats. Empty histories say no recent sales. Quality above baseline is green and below baseline red.

Disenchanter shows collected Mana and recent items with failure explanations: quality below 1.04, no enhancement, or both. The tooltip lists each item’s ManaValue.

## Refiner and Inspector

Refiner tooltip reports the last item, original/new quality, destruction when new quality is zero, and Mana spent. With refiner_mana, its control toggles Mana use. Inspector blinks when its last item changes, refreshes full item details, and opens human details from live item or the last item. Incinerator shows a fading red-tinted icon when it consumes a new last item.

## Collector, Distributor, Manifold

Their small plus control adds ports until four, then becomes a collapse control. Collector and Manifold add inputs; Distributor adds outputs. Despite its UI method name AddOutputSlot, Manifold’s adapter calls AddInputSlot. Hovering shows the last passing item when one exists.

## Track switch

Left click toggles SwitchPosition. Hover changes switch artwork; a missing secondary connection can gray its image. The switch’s routes and production model remain separate from the tooltip/animation adapter.

## Requisition Office

Its world display shows accumulated Requisition. Selecting a contract changes the shared index used by that office. Reroll costs currency and replaces that index across the kingdom; every placed office using the index updates its input. Reroll control is hidden before requisition_office_reroll. Conversion text is contract.BaseValue divided by Requisition reference value.

## Sources

- `Assets.Behaviour.Flow.Elements/WorldFlowShop.cs:29`
- `Assets.Behaviour.Flow.Elements/WorldFlowRestaurant.cs:28`
- `Assets.Behaviour.Flow.Elements/WorldFlowLuxuryShop.cs:19`
- `Assets.Behaviour.Flow.Elements/WorldFlowMercenaryGuild.cs:19`
- `Assets.Behaviour.Flow.Elements/WorldFlowDisenchanter.cs:27`
- `Assets.Behaviour.Flow.Elements/WorldFlowRefiner.cs:23`
- `Assets.Behaviour.Flow.Elements/WorldFlowInspector.cs:27`
- `Assets.Behaviour.Flow.Elements/WorldFlowIncinerator.cs:18`
- `Assets.Behaviour.Flow.Elements/WorldFlowCollector.cs:29`
- `Assets.Behaviour.Flow.Elements/WorldFlowDistributor.cs:29`
- `Assets.Behaviour.Flow.Elements/WorldFlowManifold.cs:29`
- `Assets.Behaviour.Flow.Elements/WorldFlowTrackSwitch.cs:30`
- `Assets.Behaviour.Flow.Elements/WorldFlowReqOffice.cs:21`
- `Assets.Behaviour.UI.Requisition/SelectReqContractPopup.cs:22`
- `Assets.Behaviour.UI.Requisition/SelectRequisitionReroll.cs:20`
- `Assets.Behaviour.UI.Requisition/SelectRequisitionRow.cs:32`
