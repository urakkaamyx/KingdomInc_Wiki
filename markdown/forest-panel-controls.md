# Forest crew and harvest controls

Assign workers, hire more crew, compare utilization, and select harvest outputs.

## Hiring and assigning

Hire Crew buys one unassigned worker at NextWorkerCost. A role’s + button assigns one unassigned worker; Ctrl assigns all unassigned workers. When none remain, + instead attempts to buy and assign one. The − button removes one worker; Ctrl removes the full role allocation. Subtract is disabled at zero.

## Utilization and blocking

Role tabs show utilization every 0.2 seconds and color it red above 100%. The menu and resource selector show the global blocked state. Animated work scenes are hidden when blocked or when that role has no workers. Tooltips list each role’s harvest items and WorkersPerItem.

## Choosing a Forest output

The selector groups resources by worker role and remembers the last category. It shows the currently selected resource first if it belongs to that category. Rows show description and harvest costs. Selecting another resource rebuilds the Forest machine’s IO. Its world tooltip includes quality, maximum output, harvest cost and role utilization.

## Sources

- `Assets.Behaviour.UI.Forest/ForestCrewAddButton.cs:13`
- `Assets.Behaviour.UI.Forest/ForestCrewMenu.cs:21`
- `Assets.Behaviour.UI.Forest/ForestCrewTab.cs:48`
- `Assets.Behaviour.UI.Forest/SelectForestHeader.cs:25`
- `Assets.Behaviour.UI.Forest/SelectForestResourcePopup.cs:44`
- `Assets.Behaviour.UI.Forest/SelectForestResourceRow.cs:32`
- `Assets.Behaviour.Flow.Elements/WorldFlowForest.cs:34`
- `Assets.Source.Player/ForestWorkerExtensions.cs:5`
