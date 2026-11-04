# MercenaryGuild — source reference

Assets.Source.Flow.Elements/MercenaryGuild.cs · 97 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public class MercenaryGuild : FlowElement |
| 15 | public List<(InventoryItem item, long gold, int ducats)> RecentItems = new List<(InventoryItem, long, int)>() |
| 17 | public override string Label => "@mercenary_guild" |
| 19 | public override string IconName => "Icons_200" |
| 21 | public override ElementCategory Category => ElementCategory.Consumption |
| 23 | public override bool CanAutoCraft => true |
| 25 | public MercenaryGuild() |
| 38 | public override void Start() |
| 46 | public override void Update(float delta) |
| 73 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |
| 77 | protected override void DataToJson(JsonObject data) |
| 81 | public static bool CanSellItem(InventoryItem item) |

## Documented by

| Wiki article |
| --- |
| [Mercenary Guild](building-MercenaryGuild.md) |
| [Barracks, Adventurers Guilds, and mercenaries](production-recruitment.md) |

## Sources

- `Assets.Source.Flow.Elements/MercenaryGuild.cs:1`
