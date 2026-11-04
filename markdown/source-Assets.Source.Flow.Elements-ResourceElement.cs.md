# ResourceElement — source reference

Assets.Source.Flow.Elements/ResourceElement.cs · 262 lines · 4 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 14 | public abstract class ResourceElement : FlowElement |
| 16 | public ResourceTag SupplyTag |
| 18 | public int QueuedCount |
| 24 | public ResourceItemType Resource { get; private set; } |
| 26 | public override string Label => Resource?.GetDisplayName() ?? DefaultLabel |
| 28 | public override Sprite Icon => Resource?.GetIcon() ?? base.Icon |
| 30 | public override string IconName => DefaultIconName |
| 32 | public abstract string DefaultLabel { get; } |
| 34 | public abstract string DefaultIconName { get; } |
| 36 | public abstract string ActionLabel { get; } |
| 38 | public override ElementCategory Category => ElementCategory.Resource |
| 40 | public override bool HasCraftButton |
| 52 | public virtual float OutputPerSecond => 1f * Speed |
| 54 | public virtual float QualityResourceCost => 0.2f |
| 56 | public override bool Stackable => true |
| 58 | public ResourceElement() |
| 62 | public virtual float GetDesiredOutput() |
| 71 | public virtual bool CanSupplyResource(ResourceItemType type) |
| 76 | public void SetupResource(ResourceItemType res, bool isNew = true) |
| 92 | public override void UpdateUpgrades() |
| 98 | public override void Update(float delta) |
| 154 | public override float GetCraftEffectsVolume() |
| 163 | public override bool CanManualCraft() |
| 168 | public override void DoManualCraft() |
| 203 | public CurrencyCollection GetResourceCost(ResourceItemType resource = null) |
| 223 | public IEnumerable<ResourceItemType> GetAvailableResources() |
| 234 | protected override void CopySettingsTo(FlowElement copy) |
| 242 | public override bool HandleReopenBuyMenu() |
| 248 | protected override void DataToJson(JsonObject data) |
| 254 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Mines and supply depots](production-mines-suppliers.md) |
| [Productivity and handcrafting](production-productivity.md) |
| [Barracks, Adventurers Guilds, and mercenaries](production-recruitment.md) |
| [Resource quotas and harvesting](production-resources.md) |

## Sources

- `Assets.Source.Flow.Elements/ResourceElement.cs:1`
