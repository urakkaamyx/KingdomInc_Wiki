# SelectDungeonPopup — source reference

Assets.Behaviour.UI.Dungeon/SelectDungeonPopup.cs · 45 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public class SelectDungeonPopup : UIPopupMenu |
| 16 | public bool ReopenBuyMenu { get; set; } |
| 18 | public WorldFlowDungeon Element { get; private set; } |
| 20 | public void SetElement(WorldFlowDungeon element) |
| 34 | public void DungeonSelected(DungeonType dpr) |
| 41 | public void GoToWarEffortMenu() |

## Documented by

| Wiki article |
| --- |
| [Dungeon selection and expedition display](dungeon-panel-controls.md) |

## Sources

- `Assets.Behaviour.UI.Dungeon/SelectDungeonPopup.cs:1`
