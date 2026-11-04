# Distributor — source reference

Assets.Source.Flow.Elements/Distributor.cs · 135 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public class Distributor : FlowElement |
| 10 | public int OutputCount = 2 |
| 12 | public int CurrentOutput |
| 14 | public InventoryItem LastItem |
| 16 | public override string Label => "@distributor" |
| 18 | public override ElementCategory Category => ElementCategory.Utility |
| 20 | public override string IconName => "Icons_29" |
| 22 | public override Sprite Icon => LastItem?.Icon ?? base.Icon |
| 24 | public override bool HasCraftButton => false |
| 26 | public Distributor() |
| 57 | public void AddOutputSlot() |
| 76 | public void Collapse() |
| 88 | protected override void CopySettingsTo(FlowElement copy) |
| 95 | public override void Update(float delta) |
| 123 | protected override void DataToJson(JsonObject data) |
| 129 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Distributor](building-Distributor.md) |
| [Collectors, Distributors, and Manifolds](production-routing.md) |

## Sources

- `Assets.Source.Flow.Elements/Distributor.cs:1`
