# DungeonType — source reference

Assets.Source.Adventure/DungeonType.cs · 114 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public class DungeonType |
| 10 | public delegate bool DungeonAvailable(GamePlayer ply) |
| 16 | public readonly string Identifier |
| 18 | public string DisplayName |
| 20 | public string Description |
| 22 | public string IconName |
| 24 | public bool IsEndgame |
| 26 | public DungeonAvailable IsAvailable |
| 28 | public string UnavailableText |
| 30 | public string UnlockTech |
| 32 | public CurrencyCollection SupplyCost |
| 34 | public readonly List<DungeonStage> Stages = new List<DungeonStage>() |
| 36 | public static IEnumerable<DungeonType> All => _ordered |
| 38 | public static IEnumerable<DungeonType> Unlocked |
| 52 | public Sprite Icon => SpriteLibrary.Get(IconName) |
| 54 | public DungeonProgress DefaultProgress => GamePlayer.Current.GetDungeonProgress(this) |
| 56 | public CurrencyCollection TotalSupplyCost |
| 81 | public DungeonType(string id) |
| 86 | public void AddStage(DungeonStage trash, DungeonStage boss) |
| 94 | public static void Add(DungeonType dng) |
| 100 | public static DungeonType Get(string id) |
| 105 | public bool IsAvailableFor(GamePlayer current) |
| 110 | public static implicit operator DungeonType(string id) |

## Documented by

| Wiki article |
| --- |
| [Dungeon selection and expedition display](dungeon-panel-controls.md) |

## Sources

- `Assets.Source.Adventure/DungeonType.cs:1`
