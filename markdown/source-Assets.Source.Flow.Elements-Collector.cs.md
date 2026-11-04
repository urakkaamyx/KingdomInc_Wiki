# Collector — source reference

Assets.Source.Flow.Elements/Collector.cs · 137 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public class Collector : FlowElement |
| 10 | public int InputCount = 2 |
| 12 | public int CurrentInput |
| 14 | public InventoryItem LastItem |
| 16 | public override string Label => "@collector" |
| 18 | public override ElementCategory Category => ElementCategory.Utility |
| 20 | public override string IconName => "Icons_28" |
| 22 | public override Sprite Icon => LastItem?.Icon ?? base.Icon |
| 24 | public override bool HasCraftButton => false |
| 26 | public Collector() |
| 57 | public void AddInputSlot() |
| 76 | public void Collapse() |
| 88 | public override void Update(float delta) |
| 107 | public void NextInput() |
| 118 | protected override void CopySettingsTo(FlowElement copy) |
| 125 | protected override void DataToJson(JsonObject data) |
| 131 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Collector](building-Collector.md) |
| [Collectors, Distributors, and Manifolds](production-routing.md) |

## Sources

- `Assets.Source.Flow.Elements/Collector.cs:1`
