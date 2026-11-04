# ForestSettings — source reference

Assets.Source.Player/ForestSettings.cs · 189 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 12 | public class ForestSettings |
| 26 | public IEnumerable<ForestItemType> Resources => _unlockedItems |
| 28 | public int TotalWorkers => _workers.Sum() |
| 30 | public CurrencyCollection NextWorkerCost |
| 53 | public bool IsBlocked => !GamePlayer.Current.HasWarStage("forest", 1) |
| 55 | public ForestSettings() |
| 60 | public int GetWorkerCount(ForestWorker type) |
| 65 | public bool ItemUnlocked(ForestItemType type) |
| 70 | public void UpdateResourceQuota() |
| 98 | public float GetResourceOutput(Forest res) |
| 107 | public float GetResourceQuotaMultiplier(ForestWorker workerType) |
| 116 | public float GetUtilization(ForestWorker workerType) |
| 131 | public bool AddWorkerCount(ForestWorker type, int add) |
| 150 | public void UnlockItem(ForestItemType item) |
| 155 | public JsonValue ToJson() |
| 175 | public static ForestSettings FromJson(JsonValue data) |

## Documented by

| Wiki article |
| --- |
| [Forests and forest crews](production-forest.md) |
| [Quest challenges, rewards, and permanent discounts](quest-challenges-and-rewards.md) |

## Sources

- `Assets.Source.Player/ForestSettings.cs:1`
