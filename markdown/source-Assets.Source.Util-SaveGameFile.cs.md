# SaveGameFile — source reference

Assets.Source.Util/SaveGameFile.cs · 54 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 9 | public class SaveGameFile |
| 11 | public readonly FileInfo File |
| 13 | public readonly string Name |
| 15 | public DateTime Timestamp => File.LastWriteTime |
| 17 | public SaveGameFile(FileInfo file) |
| 23 | public void LoadSaveGame() |
| 28 | public JsonObject Recall() |

## Documented by

| Wiki article |
| --- |
| [Saves, autosaves, pause, and offline behavior](saves-time-and-offline.md) |

## Sources

- `Assets.Source.Util/SaveGameFile.cs:1`
