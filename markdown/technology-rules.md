# Technology requirements and unlocking

Parents, prerequisite lists, special gates, hidden content, and purchases.

## Requirements combine

A node is locked when Root is unpurchased, Previous is unpurchased, any AdditionalRequirements entry is unpurchased, or CustomRequirement returns false. Root organizes the branch and also gates it; Previous expresses another purchase prerequisite. Available means unpurchased, unlocked, and not Hidden for this player.

HasWarStage(type,stage) checks current war stage index ≥ stage. Since completed stages advance the index, a requirement stated as stage 1 means finishing the first stage, not merely having the war unlocked.

## Branch tier versus cost tier

The eleven tier articles group declarations by their T1–T11 source-class prefix. An early branch can contain late-game recipes with higher explicit cost tiers. An unspecified cost tier inherits from Previous, otherwise Root. A missing Root inherits Previous.Root when available. Default currency is set from the resulting cost tier.

Tier tables list every explicit new TechNode declaration. Shared automation helpers add further nodes, explained in Automation technology. Declared cost overrides take precedence over defaults. Resolved entity data and the in-game tooltip give the final price.

## Purchases and grants

A left click on an available node spends its full currency collection, marks it unlocked, invokes OnUnlock, updates the tree, and refreshes the tooltip. Free technologies can still need a click unless an unlock callback grants them. AddTech rejects DevMode nodes.

## Hidden and developer content

dev_item_spawner is DevMode. turtle_statue is always hidden. Several store-channel technologies are also always hidden, and graveyard_productivity is hidden after its default upgrade is created. Tier tables mark explicit hidden declarations. The all-tech achievement excludes hidden and developer nodes. Code presence alone does not prove normal availability.

## Sources

- `Assets.Source.Player/TechNode.cs:128`
- `Assets.Source.Player/TechNode.cs:116`
- `Assets.Source.Player/TechNode.cs:280`
- `Assets.Source.Player/GamePlayer.cs:250`
- `Assets.Behaviour.UI.TechTree/UITechNode.cs:104`
- `Assets.Source.Player.Tech/T11Graveyard.cs:58`
- `Assets.Source.Player/GamePlayer.cs:542`
