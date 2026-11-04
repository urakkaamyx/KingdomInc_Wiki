# QuestProgress — source reference

Assets.Source.Adventure/QuestProgress.cs · 104 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 12 | public class QuestProgress : IJsonSource |
| 14 | public readonly QuestBoard Parent |
| 16 | public readonly Quest Quest |
| 18 | public float TickProgress |
| 20 | public int CompletedTimes => Quest.GetMetadata().CompletedCount |
| 22 | public float Progress01 => Mathf.Clamp01(TickProgress / (float)Quest.TickDuration) |
| 24 | public QuestProgress(QuestBoard parent, Quest q) |
| 30 | public void CheckProgressTick() |
| 38 | public float PenalizeLowPerformance(float addProgress, HumanItemData adv) |
| 45 | public int CalculateDifficulty(HumanItemData adv) |
| 58 | public float CalculateEnergyCost(HumanItemData adv, float energyMultiplier = 1f) |
| 63 | public bool QuestCompleted() |
| 88 | public JsonValue ToJson() |
| 97 | public static QuestProgress FromJson(QuestBoard parent, JsonValue data) |

## Documented by

| Wiki article |
| --- |
| [Achievements, Steam statistics, and integration](achievements-and-steam.md) |
| [Quest Board progress and repeat costs](quest-board-mechanics.md) |

## Sources

- `Assets.Source.Adventure/QuestProgress.cs:1`
