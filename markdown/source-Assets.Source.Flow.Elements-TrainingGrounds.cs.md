# TrainingGrounds — source reference

Assets.Source.Flow.Elements/TrainingGrounds.cs · 271 lines · 3 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public class TrainingGrounds : FlowElement |
| 13 | public const int BaseCapacity = 3 |
| 15 | public static TechNode SpecUnlock = "training_grounds_spec" |
| 25 | public float EnergyPerTick = 2f |
| 27 | public readonly TrainingGroundsSlot[] Contents = new TrainingGroundsSlot[5] |
| 29 | public CombatantItemData TrainingDummy |
| 33 | public int Capacity => 3 + (_slot1 ? 1 : 0) + (_slot2 ? 1 : 0) |
| 35 | public int TickCount => 10 |
| 37 | public float TickDelay => 2f |
| 39 | public float QualityPerTick |
| 51 | public override string Label => "@training_grounds" |
| 53 | public override ElementCategory Category => ElementCategory.Utility |
| 55 | public override string IconName => "Icons_137" |
| 57 | public override string MusicTrack => "Deep Dungeon LOOP BPM90" |
| 59 | public override bool CanManualCraft() |
| 71 | public override void DoManualCraft() |
| 83 | public TrainingGrounds() |
| 119 | public override void Start() |
| 128 | public void UpdateSlotCount() |
| 133 | public void UpdateInput() |
| 151 | public bool GetFreeSlot(out int slot) |
| 165 | public override void Update(float delta) |
| 244 | public TrainingGroundsSlot GetSlot(int idx) |
| 253 | protected override void DataToJson(JsonObject data) |
| 262 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Training Grounds](building-TrainingGrounds.md) |
| [Training Grounds and diminishing returns](production-training.md) |
| [Training Grounds and quality growth](training-grounds-mechanics.md) |

## Sources

- `Assets.Source.Flow.Elements/TrainingGrounds.cs:1`
