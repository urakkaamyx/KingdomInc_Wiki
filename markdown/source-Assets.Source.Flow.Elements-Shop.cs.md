# Shop — source reference

Assets.Source.Flow.Elements/Shop.cs · 165 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 14 | public class Shop : FlowElement |
| 16 | public const float AutoCollectTimer = 10f |
| 18 | public const int BaseGoldCap = 10000 |
| 22 | public long MaxGold |
| 24 | public long CollectedGold |
| 28 | public List<(InventoryItem Item, int Value)> RecentItems = new List<(InventoryItem, int)>() |
| 30 | public override string Label => "@shop" |
| 32 | public override string IconName => "Icons_3" |
| 34 | public override string MusicTrack => "This Town LOOP BPM130" |
| 36 | public override ElementCategory Category => ElementCategory.Consumption |
| 38 | public int GoldCap |
| 50 | public override bool Stackable => true |
| 52 | public Shop() |
| 66 | public override void Update(float delta) |
| 99 | public override void UpdateUpgrades() |
| 106 | public void DoCollect(bool autoCraftEffect) |
| 123 | public override bool CanManualCraft() |
| 128 | public override void DoManualCraft() |
| 135 | public override CurrencyCollection GetPurchaseCost(int numElements) |
| 144 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |
| 152 | protected override void DataToJson(JsonObject data) |
| 157 | public static bool CanSellItem(InventoryItem item) |

## Documented by

| Wiki article |
| --- |
| [Item Shop](building-Shop.md) |
| [Shops and gold collection](production-shops.md) |

## Sources

- `Assets.Source.Flow.Elements/Shop.cs:1`
