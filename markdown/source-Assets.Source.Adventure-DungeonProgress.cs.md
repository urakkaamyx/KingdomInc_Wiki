# DungeonProgress — source reference

Assets.Source.Adventure/DungeonProgress.cs · 424 lines · 14 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 19 | public class DungeonProgress : IJsonSource |
| 21 | public readonly DungeonType Dungeon |
| 23 | public int CurrentStage |
| 25 | public int StageTick |
| 27 | public bool Looted |
| 29 | public double StageProgress |
| 31 | public int CooldownTicks |
| 33 | public readonly List<HumanItemData> Party = new List<HumanItemData>() |
| 35 | public readonly Dungeon ParentDungeon |
| 37 | public string StatusText |
| 39 | public float Progress01 => Mathf.Clamp01((float)(StageProgress / (double)StageHealth)) |
| 41 | public long StageHealth |
| 54 | public int StageDifficulty => GetStageDifficulty(CurrentStage) |
| 56 | public int IndividualDifficulty => StageDifficulty / 4 |
| 58 | public int GroupTestDifficulty => StageDifficulty / 3 |
| 60 | public int PartyDamage |
| 73 | public DungeonStage Stage => Dungeon.Stages[CurrentStage] |
| 75 | public IEnumerable<CombatantItemData> Combatants => Party |
| 77 | public DungeonProgress(Dungeon parent, DungeonType dungeon) |
| 83 | public void DungeonTick() |
| 237 | public void CheckForLimitBreak() |
| 268 | public void ClearDungeonProgress() |
| 277 | public void DoRetreat() |
| 314 | public int GetStageDifficulty(int stageIdx) |
| 324 | public int GetDungeonDamage(float multiplier = 1f) |
| 333 | public void DealDamageToParty(int dmg, bool tankDamage) |
| 348 | public CombatantItemData GetTank(bool orRandom = false) |
| 364 | public HumanItemData GetHealer() |
| 376 | public CombatantItemData GetHealingTarget(CombatantItemData exclude = null) |
| 389 | public CombatantItemData GetRandomTarget() |
| 394 | public JsonValue ToJson() |
| 412 | public static DungeonProgress FromJson(Dungeon parent, JsonValue json) |

## Documented by

| Wiki article |
| --- |
| [Achievements, Steam statistics, and integration](achievements-and-steam.md) |
| [Timeless Archive — expedition guide](dungeon-guide-archive.md) |
| [Yensburg Catacombs — expedition guide](dungeon-guide-catacombs.md) |
| [Feral Den — expedition guide](dungeon-guide-feral-den.md) |
| [Ruins of Arlingen — expedition guide](dungeon-guide-ruins.md) |
| [Temple of the Last Rite — expedition guide](dungeon-guide-temple.md) |
| [Tomb of Sholrath — expedition guide](dungeon-guide-tomb-of-sholrath.md) |
| [Dungeon challenge reference](dungeon-hazard-reference.md) |
| [Dungeon runs, stages, loot, and retreat](dungeon-run-mechanics.md) |
| [Energy, death, and dungeon limit breaks](energy-death-and-limit-break.md) |
| [Nightmare adventure scaling and final rewards](nightmare-adventure-scaling.md) |
| [Nightmares and the endgame loop](nightmare-loop.md) |
| [Skill tests and elemental resistances](skill-tests-and-resistances.md) |
| [Tanks, healers, and party formation](tank-and-healer.md) |

## Sources

- `Assets.Source.Adventure/DungeonProgress.cs:1`
