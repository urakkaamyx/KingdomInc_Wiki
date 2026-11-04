# Manifold — source reference

Assets.Source.Flow.Elements/Manifold.cs · 128 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public class Manifold : FlowElement |
| 10 | public int InputCount = 2 |
| 12 | public InventoryItem LastItem |
| 14 | public override string Label => "@manifold" |
| 16 | public override ElementCategory Category => ElementCategory.Utility |
| 18 | public override string IconName => "Icons_104" |
| 20 | public override Sprite Icon => LastItem?.Icon ?? base.Icon |
| 22 | public override bool HasCraftButton => false |
| 24 | public Manifold() |
| 63 | public void AddInputSlot() |
| 78 | public void Collapse() |
| 90 | public override void Update(float delta) |
| 111 | protected override void CopySettingsTo(FlowElement copy) |
| 118 | protected override void DataToJson(JsonObject data) |
| 123 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Manifold](building-Manifold.md) |
| [Collectors, Distributors, and Manifolds](production-routing.md) |

## Sources

- `Assets.Source.Flow.Elements/Manifold.cs:1`
