# DungeonStage — source reference

Assets.Source.Adventure/DungeonStage.cs · 43 lines · 7 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class DungeonStage |
| 9 | public int Index |
| 11 | public string DisplayName |
| 13 | public string Description |
| 15 | public string StatusText |
| 17 | public List<string> EnemySprites |
| 19 | public int BaseDifficulty |
| 21 | public long BaseHealth |
| 23 | public float EnergyCost = 10f |
| 25 | public List<QuestChallenge> Challenges |
| 27 | public List<QuestReward> Rewards |
| 29 | public Action<DungeonProgress> OnStageCompleted |
| 31 | public bool IsBoss => Index % 2 == 1 |
| 33 | public DungeonStage(string baseName) |
| 39 | public Sprite GetSprite() |

## Documented by

| Wiki article |
| --- |
| [Timeless Archive — expedition guide](dungeon-guide-archive.md) |
| [Yensburg Catacombs — expedition guide](dungeon-guide-catacombs.md) |
| [Feral Den — expedition guide](dungeon-guide-feral-den.md) |
| [Ruins of Arlingen — expedition guide](dungeon-guide-ruins.md) |
| [Temple of the Last Rite — expedition guide](dungeon-guide-temple.md) |
| [Tomb of Sholrath — expedition guide](dungeon-guide-tomb-of-sholrath.md) |
| [Dungeon runs, stages, loot, and retreat](dungeon-run-mechanics.md) |

## Sources

- `Assets.Source.Adventure/DungeonStage.cs:1`
