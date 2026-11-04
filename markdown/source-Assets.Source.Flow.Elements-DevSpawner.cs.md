# DevSpawner — source reference

Assets.Source.Flow.Elements/DevSpawner.cs · 72 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public class DevSpawner : FlowElement |
| 10 | public ItemType Item |
| 12 | public override string Label => "Spawner" |
| 14 | public override ElementCategory Category => ElementCategory.Resource |
| 16 | public override string IconName => "Icons_18" |
| 18 | public override bool HasCraftButton => false |
| 20 | public DevSpawner() |
| 31 | public override void Update(float delta) |
| 57 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |
| 65 | protected override void DataToJson(JsonObject data) |

## Documented by

| Wiki article |
| --- |
| [DevSpawner](building-DevSpawner.md) |

## Sources

- `Assets.Source.Flow.Elements/DevSpawner.cs:1`
