# WarProgress — source reference

Assets.Source.Adventure/WarProgress.cs · 385 lines · 4 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 17 | public class WarProgress : IJsonSource |
| 25 | public readonly WarType War |
| 27 | public readonly List<CombatantItemData> Soldiers = new List<CombatantItemData>() |
| 29 | public int CurrentStage |
| 31 | public int StageProgress |
| 33 | public int PartialProgress |
| 35 | public int NotifiedStage |
| 41 | public int MaxProgress |
| 54 | public float StageProgress01 => Mathf.Clamp01((float)StageProgress / (float)MaxProgress) |
| 56 | public WarProgress(WarType war) |
| 61 | public void UpdateWar() |
| 219 | public CombatantItemData GetHealingTarget(CombatantItemData exclude = null) |
| 232 | public void AddProgress(int amt) |
| 295 | public void NotifyStageComplete() |
| 320 | public void NotifyStageLost() |
| 341 | public void NotifyDefense() |
| 358 | public int GetProgressTracker() |
| 363 | public JsonValue ToJson() |
| 375 | public static WarProgress FromJson(JsonValue json) |

## Documented by

| Wiki article |
| --- |
| [Nightmare adventure scaling and final rewards](nightmare-adventure-scaling.md) |
| [Nightmares and the endgame loop](nightmare-loop.md) |
| [Tanks, healers, and party formation](tank-and-healer.md) |
| [War Effort combat, medals, and defense](war-effort-mechanics.md) |

## Sources

- `Assets.Source.Adventure/WarProgress.cs:1`
