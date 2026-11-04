# SpriteLibrary — source reference

SpriteLibrary.cs · 65 lines · 3 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public class SpriteLibrary |
| 30 | public static Sprite Get(string name) |
| 35 | internal static Sprite Get(object iconName) |
| 40 | public static IEnumerable<(string icon, string name)> GetUsableIconNames() |

## Documented by

| Wiki article |
| --- |
| [Decorations, labels, colors, and stickers](decoration-labels-stickers.md) |
| [Data records, serialization, and implementation limits](implementation-data-and-serialization.md) |
| [Workflow tabs, names, icons, and ordering](workflow-tabs-and-labels.md) |

## Sources

- `SpriteLibrary.cs:1`
