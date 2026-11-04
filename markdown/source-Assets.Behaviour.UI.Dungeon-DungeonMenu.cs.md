# DungeonMenu — source reference

Assets.Behaviour.UI.Dungeon/DungeonMenu.cs · 402 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 17 | public class DungeonMenu : MonoBehaviour |
| 119 | public static DungeonMenu Instance { get; private set; } |
| 121 | public DungeonProgress SelectedDungeon { get; private set; } |
| 123 | public int VisibleStage { get; private set; } |
| 174 | public void ShowDungeonProgress(DungeonProgress progress, int stage = -1) |
| 219 | public void ShowDungeonType(DungeonType dungeon, int stage = -1) |
| 224 | public void UpdateProgressSprites() |
| 238 | public void ShowStage(int stageIdx, bool manualSwitch) |
| 330 | public void UpdateStageStats() |
| 338 | public void ShowChallengeTick(QuestChallenge challenge, CombatantItemData target, bool success) |
| 350 | public void DoRetreat() |

## Documented by

| Wiki article |
| --- |
| [Dungeon selection and expedition display](dungeon-panel-controls.md) |

## Sources

- `Assets.Behaviour.UI.Dungeon/DungeonMenu.cs:1`
