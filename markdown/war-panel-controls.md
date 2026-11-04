# War selection and status panels

Choose a campaign, read progress trends, inspect stage rewards, and examine soldiers.

## Campaign choice

The machine popup lists wars already present in GamePlayer.Wars. Select assigns the machine’s WarType; Inspect opens the campaign panel. Rows refresh current stage and stage progress. A completed North campaign has its own status wording. The world machine opens its selector if no campaign is set, otherwise its details.

## Status colors

The war panel creates tabs for available wars, stage nodes and a progress strip. Blocked progression is red with ProgressBlockedReason. Tracker above 2 is green, below 2 red, and exactly 2 neutral blue. After the final stage, a complete status replaces the current-stage line.

## Stage rewards

Hover a stage node for description and reward text. Secured stages show RewardComplete; others show the prospective RewardDescription. Stage icons become colored when HasWarStage reports them secured. Terrain and enemy artwork are selected from campaign data.

## Soldiers

The soldier panel shows at most its MaxCount (default 10), plus an overflow count; this is a display limit rather than an army cap. Sprites show weapon and health. Tooltips warn humans lacking weapons and combatants lacking armor. Right click a human for details and return to the war panel on closing. Health gains flash green, losses pale red; death/exhaustion fades the portrait.

## Sources

- `Assets.Behaviour.UI.WarEffort/SelectWarEffortPopup.cs:21`
- `Assets.Behaviour.UI.WarEffort/SelectWarEffortRow.cs:28`
- `Assets.Behaviour.UI.WarEffort/SelectWarEffortTooltip.cs:11`
- `Assets.Behaviour.UI.WarEffort/WarEffortMenu.cs:68`
- `Assets.Behaviour.UI.WarEffort/WarEffortMenuNode.cs:24`
- `Assets.Behaviour.UI.WarEffort/WarEffortMenuTab.cs:28`
- `Assets.Behaviour.UI.WarEffort/WarEffortSoldierContainer.cs:30`
- `Assets.Behaviour.UI.WarEffort/WarEffortSoldierSprite.cs:50`
- `Assets.Behaviour.UI.WarEffort/WarEffortTerrainType.cs:7`
- `Assets.Behaviour.Flow.Elements/WorldFlowWarEffort.cs:43`
- `Assets.Behaviour.Flow.Elements/WorldFlowWarEffortConscript.cs:29`
- `Assets.Behaviour.Flow.Elements/WorldFlowWarEffortSprite.cs:7`
- `Assets.Source.Adventure/WarType.cs:63`
- `Assets.Source.Adventure/WarStage.cs:7`
