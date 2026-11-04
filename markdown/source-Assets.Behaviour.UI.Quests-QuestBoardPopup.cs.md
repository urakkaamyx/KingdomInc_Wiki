# QuestBoardPopup — source reference

Assets.Behaviour.UI.Quests/QuestBoardPopup.cs · 89 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 12 | public class QuestBoardPopup : UIPopupMenu |
| 24 | public WorldFlowQuestBoard Element => _activeBoard |
| 26 | public Quest SelectedQuest { get; private set; } |
| 28 | public override bool CanCancel => !UITooltip.Active |
| 30 | public void OnEnable() |
| 69 | public void SetElement(WorldFlowQuestBoard qb) |
| 74 | public void SetSelected(QuestBoardRow sel) |
| 83 | public void SetSelectedQuest(Quest quest) |

## Documented by

| Wiki article |
| --- |
| [Quest Board panel controls](quest-panel-controls.md) |

## Sources

- `Assets.Behaviour.UI.Quests/QuestBoardPopup.cs:1`
