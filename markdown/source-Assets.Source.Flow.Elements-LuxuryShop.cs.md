# LuxuryShop — source reference

Assets.Source.Flow.Elements/LuxuryShop.cs · 91 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 13 | public class LuxuryShop : FlowElement |
| 15 | public List<(InventoryItem item, long gold, int crowns)> RecentItems = new List<(InventoryItem, long, int)>() |
| 17 | public override string Label => "@luxury_shop" |
| 19 | public override string IconName => "Icons_189" |
| 21 | public override ElementCategory Category => ElementCategory.Consumption |
| 23 | public override bool CanAutoCraft => true |
| 25 | public LuxuryShop() |
| 38 | public override void Update(float delta) |
| 75 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |
| 79 | protected override void DataToJson(JsonObject data) |
| 83 | public static bool CanSellItem(InventoryItem item) |

## Documented by

| Wiki article |
| --- |
| [Luxury Shop](building-LuxuryShop.md) |
| [Luxury Shops and crown chances](production-luxury-shop.md) |

## Sources

- `Assets.Source.Flow.Elements/LuxuryShop.cs:1`
