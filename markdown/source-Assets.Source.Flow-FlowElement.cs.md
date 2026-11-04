# FlowElement — source reference

Assets.Source.Flow/FlowElement.cs · 632 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 12 | public abstract class FlowElement : IJsonSource |
| 14 | public const double BaseCost = 780.0 |
| 16 | public const int MaxStackSize = 5 |
| 20 | public Vector2Int Size |
| 22 | public Vector2Int Position |
| 24 | public string Description |
| 26 | public TechNode RequiredTech |
| 28 | public IReadOnlyList<Currency> CostCurrency |
| 30 | public double CostMultiplier = 1.0 |
| 32 | public double GoldMultiplier = 1.0 |
| 34 | public WorldFlowElement World |
| 36 | public float Progress |
| 38 | public float ProductivityProgress |
| 40 | public int StackSize = 1 |
| 42 | public readonly List<FlowInput> Inputs = new List<FlowInput>() |
| 44 | public readonly List<FlowOutput> Outputs = new List<FlowOutput>() |
| 46 | public bool Mirrored |
| 52 | public float MouseProximity |
| 58 | public string Guid { get; private set; } |
| 60 | public int CostTier => RequiredTech?.CostTier ?? 1 |
| 62 | public double CostPower => Category switch |
| 70 | public virtual bool HasCraftButton => !CanAutoCraft |
| 72 | public virtual string ElementType => GetType().Name |
| 74 | public abstract string Label { get; } |
| 76 | public abstract ElementCategory Category { get; } |
| 78 | public abstract string IconName { get; } |
| 80 | public virtual Sprite Icon |
| 93 | public IEnumerable<FlowIO> IO |
| 108 | public virtual int UpgradeSlots => GamePlayer.Current.GetUpgradeSlotCount(ElementType) |
| 110 | public virtual bool CanAutoCraft => _hasWorker |
| 112 | public float Quality { get; protected set; } = 1f |
| 114 | public float Speed { get; protected set; } = 1f |
| 116 | public float Productivity { get; protected set; } |
| 118 | public virtual bool Stackable => false |
| 120 | public virtual string MusicTrack => null |
| 122 | public FlowDiagram ParentFlow |
| 137 | public FlowElement() |
| 142 | public virtual void Start() |
| 146 | public abstract void Update(float delta) |
| 148 | public virtual void OnCreateElement() |
| 152 | public virtual void OnRemoveElement() |
| 156 | public CurrencyCollection GetPurchaseCost() |
| 161 | public virtual CurrencyCollection GetPurchaseCost(int numElements) |
| 166 | public virtual CurrencyCollection GetRefund(int alreadyRefunded = 0) |
| 185 | public virtual bool IsPurchaseable(GamePlayer ply) |
| 194 | public virtual bool CanManualCraft() |
| 199 | public virtual void DoManualCraft() |
| 203 | public FlowUpgrade GetUpgrade(int idx) |
| 212 | public void SetUpgrade(int idx, FlowUpgrade upgrade) |
| 232 | public bool HasUpgrade<T>() where T : FlowUpgrade |
| 248 | public int CountUpgrades<T>() where T : FlowUpgrade |
| 265 | public int CountUpgrades(Type t) |
| 282 | public virtual FlowElement CreateCopy() |
| 299 | protected virtual void CopySettingsTo(FlowElement copy) |
| 303 | public virtual void UpdateUpgrades() |
| 329 | public int NthUpgrade(int slot, FlowUpgrade checkUpgrade = null) |
| 354 | public IEnumerable<FlowUpgrade> GetAvailableUpgrades() |
| 366 | public virtual FlowUpgrade GetAutoFlowUpgrade() |
| 392 | public CurrencyCollection GetCopyCost(int nthCopy = 0) |
| 428 | public CurrencyCollection GetSingleCopyCost(int nthCopy = 0) |
| 433 | public virtual bool HandleReopenBuyMenu() |
| 438 | public virtual float GetCraftEffectsVolume() |
| 457 | public FlowOutput GetOutput(ItemType item) |
| 469 | public void ClearOutputs() |
| 474 | public void ClearInputs() |
| 479 | public void ClearIO() |
| 516 | protected abstract void DataToJson(JsonObject data) |
| 518 | protected abstract void DataFromJson(JsonObject data, FlowDiagram parent) |
| 520 | public JsonValue ToJson() |
| 568 | public static FlowElement FromJson(JsonValue data, FlowDiagram parent) |
| 604 | public static FlowElement Create(string name) |
| 609 | public static IEnumerable<FlowElement> GetAllTypes() |
| 622 | public static IEnumerable<FlowElement> GetBuildableTypes() |

## Documented by

| Wiki article |
| --- |
| [Workers, upgrades, stacking, and refunds](production-upgrades.md) |

## Sources

- `Assets.Source.Flow/FlowElement.cs:1`
