# QuestBoard — source reference

Assets.Source.Flow.Elements/QuestBoard.cs · 279 lines · 3 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 17 | public class QuestBoard : FlowElement |
| 19 | public const int SlotCount = 5 |
| 21 | public readonly List<HumanItemData> Contents = new List<HumanItemData>() |
| 23 | public float CoinLootMultiplier = 1f |
| 29 | public override string Label => "@quest_board" |
| 31 | public override ElementCategory Category => ElementCategory.Consumption |
| 33 | public override string IconName => SelectedQuest?.Quest.IconName ?? "Icons_136" |
| 35 | public override string MusicTrack => "Middle Earth LOOP BPM90" |
| 37 | public QuestProgress SelectedQuest { get; private set; } |
| 39 | public QuestBoard() |
| 60 | public override bool CanManualCraft() |
| 69 | public override void Start() |
| 77 | public override bool HandleReopenBuyMenu() |
| 83 | public override void UpdateUpgrades() |
| 90 | public void UpdateQuest(Quest q) |
| 129 | public override void Update(float delta) |
| 146 | public override void DoManualCraft() |
| 166 | public void UpdateQuestProgress() |
| 223 | public void QuestCompleted() |
| 242 | public HumanItemData GetHealer() |
| 254 | protected override void CopySettingsTo(FlowElement copy) |
| 259 | protected override void DataToJson(JsonObject data) |
| 270 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Quest Board](building-QuestBoard.md) |
| [Quest Board progress and repeat costs](quest-board-mechanics.md) |
| [Traits and party buffs](traits-and-party-buffs.md) |

## Sources

- `Assets.Source.Flow.Elements/QuestBoard.cs:1`
