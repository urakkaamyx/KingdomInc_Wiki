# Arena — source reference

Assets.Source.Flow.Elements/Arena.cs · 394 lines · 5 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 13 | public class Arena : FlowElement |
| 15 | public const int BaseCapacity = 3 |
| 17 | public float EnergyPerTick = 3f |
| 19 | public CombatantItemData Slot1 |
| 21 | public CombatantItemData Slot2 |
| 23 | public bool Fighting |
| 25 | public bool FightToTheDeath |
| 27 | public int TicksRemaining |
| 29 | public float CooldownTimer |
| 31 | public float RewardMultiplier |
| 33 | public bool CanOutput = true |
| 35 | public bool BlockedByWar |
| 43 | public int TickCount => 10 |
| 45 | public float TickDelay => 2f |
| 47 | public float QualityPerTick |
| 63 | public override string Label => "@arena" |
| 65 | public override ElementCategory Category => ElementCategory.Utility |
| 67 | public override string IconName => "Icons2_0" |
| 69 | public override bool HasCraftButton |
| 81 | public override string MusicTrack => "Deep Dungeon LOOP BPM90" |
| 83 | public override bool CanManualCraft() |
| 92 | public override void DoManualCraft() |
| 98 | public Arena() |
| 129 | public override void Start() |
| 135 | public void StartFight() |
| 155 | public override void UpdateUpgrades() |
| 162 | public override void Update(float delta) |
| 366 | protected override void DataToJson(JsonObject data) |
| 380 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Arena combat and training](arena-combat-and-training.md) |
| [Arena audience income](arena-income.md) |
| [Arena](building-Arena.md) |
| [Adventurer classes and advancement routes](class-progression.md) |
| [Arena battles, training, and rewards](production-arena.md) |

## Sources

- `Assets.Source.Flow.Elements/Arena.cs:1`
