# QuestMetadata — source reference

Assets.Source.Adventure/QuestMetadata.cs · 32 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 5 | public class QuestMetadata : IJsonSource |
| 7 | public readonly Quest Quest |
| 9 | public int CompletedCount |
| 11 | public QuestMetadata(Quest q) |
| 16 | public JsonValue ToJson() |
| 25 | public static QuestMetadata FromJson(JsonValue json) |

## Documented by

| Wiki article |
| --- |
| [Data records, serialization, and implementation limits](implementation-data-and-serialization.md) |

## Sources

- `Assets.Source.Adventure/QuestMetadata.cs:1`
