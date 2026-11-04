# WorldFlowQuestBoard — source reference

Assets.Behaviour.Flow.Elements/WorldFlowQuestBoard.cs · 178 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 15 | public class WorldFlowQuestBoard : MonoBehaviour, ITooltipTitleSource, ITooltipCustomSource |
| 36 | public QuestBoard Element { get; private set; } |
| 127 | public void ToggleQuestPopup() |
| 134 | public void DelayOpenPopup() |
| 145 | public void AdventurerAdded(HumanItemData adv) |
| 161 | public void QuestCompleted() |
| 169 | public string GetTooltipTitle() |
| 174 | public void AddTooltipCustomContent(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Quest Board panel controls](quest-panel-controls.md) |

## Sources

- `Assets.Behaviour.Flow.Elements/WorldFlowQuestBoard.cs:1`
