# FarmSettings — source reference

Assets.Source.Player/FarmSettings.cs · 154 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 9 | public class FarmSettings |
| 11 | public const int StartWidth = 3 |
| 13 | public const int StartHeight = 2 |
| 15 | public const int MaxWidth = 6 |
| 23 | public static FarmSettings Current => GamePlayer.Current.FarmSettings |
| 25 | public int Width => _field.GetLength(0) |
| 27 | public int Height => _field.GetLength(1) |
| 29 | public IEnumerable<FarmItemType> Resources => _unlockedItems |
| 31 | public bool IsBlocked => !GamePlayer.Current.HasWarStage("eastern", 1) |
| 33 | public int UpgradeCount => Width + Height - 3 - 2 |
| 35 | public FarmSettings() |
| 40 | public bool ItemUnlocked(FarmItemType type) |
| 45 | public void SetFieldSize(int w, int h) |
| 58 | public FarmItemType GetItem(int x, int y) |
| 63 | public void SetItem(int x, int y, FarmItemType item) |
| 68 | public void UpdateResourceQuota() |
| 91 | public void UnlockItem(FarmItemType item) |
| 96 | public CurrencyCollection GetPlotCost(int newPlots) |
| 112 | public JsonValue ToJson() |
| 139 | public static FarmSettings FromJson(JsonValue data) |

## Documented by

| Wiki article |
| --- |
| [Farming and field expansion](production-farming.md) |

## Sources

- `Assets.Source.Player/FarmSettings.cs:1`
