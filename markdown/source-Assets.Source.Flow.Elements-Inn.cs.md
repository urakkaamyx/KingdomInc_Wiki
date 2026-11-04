# Inn — source reference

Assets.Source.Flow.Elements/Inn.cs · 189 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public class Inn : FlowElement |
| 13 | public const int Capacity = 5 |
| 17 | public float EnergyPerTick = 0.4f |
| 19 | public float MaxQuality = 1.2f |
| 21 | public readonly InnSlot[] Contents = new InnSlot[5] |
| 25 | public float FoodGoldMultiplier = 0.5f |
| 27 | public int TickCount => 20 |
| 29 | public float TickDelay => 2f |
| 31 | public override string Label => "@inn" |
| 33 | public override ElementCategory Category => ElementCategory.Utility |
| 35 | public override string IconName => "Icons_154" |
| 37 | public override string MusicTrack => "Minimal Dungeon LOOP BPM100" |
| 39 | public override bool CanAutoCraft => true |
| 41 | public int InnGold => 200 |
| 43 | public override bool CanManualCraft() |
| 55 | public override void DoManualCraft() |
| 67 | public Inn() |
| 87 | public void UpdateFoodInput() |
| 105 | public override void Update(float delta) |
| 174 | public InnSlot GetSlot(int idx) |
| 179 | protected override void DataToJson(JsonObject data) |
| 184 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Inn](building-Inn.md) |
| [Inns, healing, and food](production-inn.md) |

## Sources

- `Assets.Source.Flow.Elements/Inn.cs:1`
