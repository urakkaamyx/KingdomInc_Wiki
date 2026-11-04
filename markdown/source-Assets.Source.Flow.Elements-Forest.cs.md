# Forest — source reference

Assets.Source.Flow.Elements/Forest.cs · 238 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 13 | public class Forest : FlowElement |
| 17 | public int QueuedCount |
| 21 | public override string Label => "@forest" |
| 23 | public override ElementCategory Category => ElementCategory.Resource |
| 25 | public override Sprite Icon => SelectedResource?.GetIcon() ?? base.Icon |
| 27 | public override string IconName => "Icons_65" |
| 29 | public override string MusicTrack => "Explore The Forest LOOP BPM130" |
| 31 | public override bool HasCraftButton |
| 43 | public virtual float OutputPerSecond => 1f * Speed |
| 45 | public ForestItemType SelectedResource { get; private set; } |
| 47 | public override bool Stackable => true |
| 49 | public Forest() |
| 56 | public virtual float GetDesiredOutput() |
| 65 | public override void UpdateUpgrades() |
| 71 | public override void Update(float delta) |
| 122 | public void SetupResource(ForestItemType res, bool isNew = true) |
| 138 | public CurrencyCollection GetResourceCost(ForestItemType resource = null) |
| 158 | public override bool CanManualCraft() |
| 163 | public override void DoManualCraft() |
| 198 | public override bool HandleReopenBuyMenu() |
| 204 | public override float GetCraftEffectsVolume() |
| 213 | protected override void CopySettingsTo(FlowElement copy) |
| 221 | protected override void DataToJson(JsonObject data) |
| 230 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Forest](building-Forest.md) |
| [Forests and forest crews](production-forest.md) |

## Sources

- `Assets.Source.Flow.Elements/Forest.cs:1`
