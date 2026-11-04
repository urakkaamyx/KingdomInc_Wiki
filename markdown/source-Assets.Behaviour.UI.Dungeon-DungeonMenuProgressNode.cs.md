# DungeonMenuProgressNode — source reference

Assets.Behaviour.UI.Dungeon/DungeonMenuProgressNode.cs · 71 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 10 | public class DungeonMenuProgressNode : MonoBehaviour, ITooltipTitleSource, ITooltipCustomSource, IPointerClickHandler, IEventSystemHandler |
| 24 | public void SetStage(DungeonProgress d, DungeonStage stage) |
| 47 | public string GetTooltipTitle() |
| 52 | public void AddTooltipCustomContent(UITooltip tooltip) |
| 58 | public void OnPointerClick(PointerEventData eventData) |

## Documented by

| Wiki article |
| --- |
| [Dungeon selection and expedition display](dungeon-panel-controls.md) |

## Sources

- `Assets.Behaviour.UI.Dungeon/DungeonMenuProgressNode.cs:1`
