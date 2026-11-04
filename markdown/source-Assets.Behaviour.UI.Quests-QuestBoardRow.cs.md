# QuestBoardRow — source reference

Assets.Behaviour.UI.Quests/QuestBoardRow.cs · 183 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 14 | public class QuestBoardRow : MonoBehaviour, IPointerClickHandler, IEventSystemHandler |
| 81 | public Quest Quest { get; private set; } |
| 93 | public void SetQuest(QuestBoard parent, Quest q, QuestProgress progress) |
| 143 | public void SetExpanded(bool exp) |
| 169 | public void OnPointerClick(PointerEventData eventData) |
| 178 | public void AcceptQuest() |

## Documented by

| Wiki article |
| --- |
| [Quest Board panel controls](quest-panel-controls.md) |

## Sources

- `Assets.Behaviour.UI.Quests/QuestBoardRow.cs:1`
