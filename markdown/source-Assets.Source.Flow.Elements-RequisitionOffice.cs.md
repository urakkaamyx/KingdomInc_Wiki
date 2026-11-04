# RequisitionOffice — source reference

Assets.Source.Flow.Elements/RequisitionOffice.cs · 260 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 14 | public class RequisitionOffice : FlowElement |
| 16 | public const int BaseReqCapacity = 10 |
| 18 | public int CollectedRequisition |
| 20 | public int MaxRequisition |
| 30 | public override string Label => "@requisition_office" |
| 32 | public override string IconName => "Icons_33" |
| 34 | public override string MusicTrack => "Mystical Lands LOOP BPM110" |
| 36 | public override ElementCategory Category => ElementCategory.Consumption |
| 38 | public int SelectedContract { get; private set; } = -1 |
| 40 | public int StoredValue { get; private set; } |
| 42 | public override Sprite Icon => ContractedItem?.GetIcon() ?? base.Icon |
| 44 | public ItemType ContractedItem |
| 56 | public RequisitionOffice() |
| 70 | public override void Start() |
| 75 | public override void UpdateUpgrades() |
| 88 | public void UpdateInput() |
| 95 | public void SetSelectedContract(int idx) |
| 101 | public override void Update(float delta) |
| 155 | public override bool CanManualCraft() |
| 160 | public override void DoManualCraft() |
| 171 | public override bool HandleReopenBuyMenu() |
| 177 | protected override void CopySettingsTo(FlowElement copy) |
| 182 | protected override void DataToJson(JsonObject data) |
| 189 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |
| 196 | public static void AddRequisitionContract() |
| 219 | public static ItemType GetRequisitionContract() |
| 251 | public static CurrencyCollection GetRerollCost() |

## Documented by

| Wiki article |
| --- |
| [Requisition Office](building-RequisitionOffice.md) |
| [Requisition Offices and contracts](production-requisitions.md) |

## Sources

- `Assets.Source.Flow.Elements/RequisitionOffice.cs:1`
