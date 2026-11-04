# Quest — source reference

Assets.Source.Adventure/Quest.cs · 109 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 10 | public class Quest |
| 16 | public readonly string Identifier |
| 18 | public string DisplayName |
| 20 | public string Description |
| 22 | public string Category |
| 24 | public string IconName |
| 26 | public int Difficulty |
| 28 | public int BaseDuration |
| 30 | public float EnergyPerTick = 0.2f |
| 32 | public float TrainingAdded = 0.12f |
| 34 | public float DurationMultiplier = 1f |
| 36 | public IReadOnlyList<QuestReward> FirstRewards |
| 38 | public IReadOnlyList<QuestReward> RepeatableRewards |
| 40 | public IReadOnlyList<QuestChallenge> Challenges |
| 42 | public Action<HumanItemData> OnComplete |
| 44 | public TechNode RequiredTech |
| 46 | public static IReadOnlyList<Quest> All => _orderedQuests |
| 48 | public Sprite Icon => SpriteLibrary.Get(IconName) |
| 50 | public bool IsUnlocked |
| 62 | public int TickDuration => Mathf.RoundToInt((float)BaseDuration * Mathf.Pow(DurationMultiplier, GetMetadata().CompletedCount)) |
| 72 | public Quest(string id) |
| 80 | public QuestMetadata GetMetadata() |
| 85 | public IReadOnlyList<QuestReward> GetRewards(int completedCount) |
| 94 | public static void Add(Quest q) |
| 100 | public static Quest Get(string id) |
| 105 | public static implicit operator Quest(string id) |

## Documented by

| Wiki article |
| --- |
| [Quest Board progress and repeat costs](quest-board-mechanics.md) |

## Sources

- `Assets.Source.Adventure/Quest.cs:1`
