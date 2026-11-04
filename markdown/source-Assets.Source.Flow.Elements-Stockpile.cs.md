# Stockpile — source reference

Assets.Source.Flow.Elements/Stockpile.cs · 113 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 9 | public class Stockpile : FlowElement |
| 11 | public const int BaseCapacity = 10 |
| 13 | public int Capacity = 10 |
| 15 | public readonly List<InventoryItem> Contents = new List<InventoryItem>() |
| 17 | public override string Label => "@stockpile" |
| 19 | public override ElementCategory Category => ElementCategory.Utility |
| 21 | public override string IconName => "Icons_105" |
| 23 | public override bool HasCraftButton => false |
| 25 | public InventoryItem FirstItem |
| 37 | public override Sprite Icon => FirstItem?.Icon ?? base.Icon |
| 39 | public Stockpile() |
| 59 | public void UpdateOutput() |
| 76 | public override void Update(float delta) |
| 94 | protected override void CopySettingsTo(FlowElement copy) |
| 99 | protected override void DataToJson(JsonObject data) |
| 105 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Stockpile](building-Stockpile.md) |
| [Stockpiles and overflow](production-stockpiles.md) |

## Sources

- `Assets.Source.Flow.Elements/Stockpile.cs:1`
