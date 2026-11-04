# WarEffort — source reference

Assets.Source.Flow.Elements/WarEffort.cs · 185 lines · 6 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 14 | public class WarEffort : FlowElement |
| 22 | public WarType WarType |
| 24 | public bool TriggerAttack |
| 26 | public CombatantItemData CurrentSoldier |
| 28 | public List<CombatantItemData> Soldiers = new List<CombatantItemData>() |
| 30 | public override string Label => "@war_effort" |
| 32 | public override ElementCategory Category => ElementCategory.Consumption |
| 34 | public override string IconName => "Icons_58" |
| 36 | public override string MusicTrack => "Battle Is Here LOOP BPM100" |
| 38 | public override bool HasCraftButton => false |
| 40 | public override Sprite Icon => WarType?.Icon ?? base.Icon |
| 42 | public WarEffort() |
| 63 | public override void Start() |
| 72 | public void UpdateIO() |
| 92 | public override void Update(float delta) |
| 113 | public void CleanupSoldier(CombatantItemData soldier) |
| 122 | public void ShowIncome(int medals) |
| 135 | public void SoldierDied(CombatantItemData soldier) |
| 146 | public override bool HandleReopenBuyMenu() |
| 152 | protected override void CopySettingsTo(FlowElement copy) |
| 157 | protected override void DataToJson(JsonObject data) |
| 172 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [War Effort](achievement-WarEffort.md) |
| [Achievements, Steam statistics, and integration](achievements-and-steam.md) |
| [War Effort](building-WarEffort.md) |
| [Training Grounds and quality growth](training-grounds-mechanics.md) |
| [Traits and party buffs](traits-and-party-buffs.md) |
| [War Effort combat, medals, and defense](war-effort-mechanics.md) |

## Sources

- `Assets.Source.Flow.Elements/WarEffort.cs:1`
