# SaveGame — source reference

Assets.Source.Util/SaveGame.cs · 210 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 13 | public class SaveGame |
| 15 | public const string DefaultSaveFile = "autosave" |
| 17 | public const int AutosaveSlots = 3 |
| 19 | public static float AutosaveFrequency |
| 21 | public static string SavesPath |
| 23 | public const SaveGameFormat DefaultSaveFormat = SaveGameFormat.Compressed |
| 25 | public const string SaveFileExtension = ".save" |
| 42 | public static JsonObject SaveCurrentState() |
| 57 | public static void LoadState(JsonObject data) |
| 102 | public static void StoreAutosaveState(string saveFile = null) |
| 107 | public static void DoSave(string saveFile) |
| 137 | public static void Store(JsonObject data, string saveName, SaveGameFormat format = SaveGameFormat.Compressed) |
| 160 | public static List<SaveGameFile> GetSaveGames() |
| 177 | public static SaveGameFile GetSaveGame(string name) |
| 189 | public static SaveGameFile GetLatestSave() |
| 200 | public static bool LoadLatestSave() |

## Documented by

| Wiki article |
| --- |
| [Saves, autosaves, pause, and offline behavior](saves-time-and-offline.md) |

## Sources

- `Assets.Source.Util/SaveGame.cs:1`
