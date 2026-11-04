# Disenchanter — source reference

Assets.Source.Flow.Elements/Disenchanter.cs · 126 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 13 | public class Disenchanter : FlowElement |
| 15 | public const float MinQuality = 1.04f |
| 23 | public int CollectedMana |
| 25 | public List<InventoryItem> RecentItems = new List<InventoryItem>() |
| 27 | public override string Label => "@disenchanter" |
| 29 | public override string IconName => "Icons_156" |
| 31 | public override string MusicTrack => "Magical World LOOP BPM80" |
| 33 | public override ElementCategory Category => ElementCategory.Consumption |
| 35 | public Disenchanter() |
| 49 | public override void UpdateUpgrades() |
| 56 | public override void Update(float delta) |
| 88 | public void DoCollect() |
| 96 | public override bool CanManualCraft() |
| 101 | public override void DoManualCraft() |
| 108 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |
| 113 | protected override void DataToJson(JsonObject data) |
| 118 | public static bool CanSellItem(InventoryItem item) |

## Documented by

| Wiki article |
| --- |
| [Disenchanter](building-Disenchanter.md) |
| [Disenchanting and mana production](production-mana.md) |

## Sources

- `Assets.Source.Flow.Elements/Disenchanter.cs:1`
