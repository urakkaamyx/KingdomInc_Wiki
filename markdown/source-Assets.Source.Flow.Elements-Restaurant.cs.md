# Restaurant — source reference

Assets.Source.Flow.Elements/Restaurant.cs · 166 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 14 | public class Restaurant : FlowElement |
| 16 | public const float AutoCollectTimer = 10f |
| 18 | public int CollectedCrowns |
| 20 | public long CollectedGold |
| 28 | public List<(InventoryItem item, int crowns, int gold)> RecentItems = new List<(InventoryItem, int, int)>() |
| 30 | public override string Label => "@restaurant" |
| 32 | public override string IconName => "Icons_185" |
| 34 | public override ElementCategory Category => ElementCategory.Consumption |
| 36 | public override string MusicTrack => "This Town LOOP BPM130" |
| 38 | public Restaurant() |
| 51 | public override void Update(float delta) |
| 102 | public override void UpdateUpgrades() |
| 110 | public void DoCollect(bool autoCraftEffect) |
| 134 | public override bool CanManualCraft() |
| 139 | public override void DoManualCraft() |
| 146 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |
| 152 | protected override void DataToJson(JsonObject data) |
| 158 | public static bool CanSellItem(InventoryItem item) |

## Documented by

| Wiki article |
| --- |
| [Restaurant](building-Restaurant.md) |
| [Restaurants, food, and Crowns](production-restaurants.md) |

## Sources

- `Assets.Source.Flow.Elements/Restaurant.cs:1`
