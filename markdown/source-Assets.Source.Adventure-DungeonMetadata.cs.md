# DungeonMetadata — source reference

Assets.Source.Adventure/DungeonMetadata.cs · 58 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 5 | public class DungeonMetadata : IJsonSource |
| 7 | public readonly DungeonType Dungeon |
| 9 | public readonly int[] CompletedCount |
| 11 | public readonly int[] WipeCount |
| 13 | public DungeonMetadata(DungeonType dungeon) |
| 20 | public JsonValue ToJson() |
| 42 | public static DungeonMetadata FromJson(JsonValue data) |

## Documented by

| Wiki article |
| --- |
| [Dungeon selection and expedition display](dungeon-panel-controls.md) |

## Sources

- `Assets.Source.Adventure/DungeonMetadata.cs:1`
