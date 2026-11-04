# WorldFlowTrainingGroundsSlot — source reference

Assets.Behaviour.Flow.Elements/WorldFlowTrainingGroundsSlot.cs · 208 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 13 | public class WorldFlowTrainingGroundsSlot : MonoBehaviour, ITooltipTitleSource, ITooltipCustomSource, IPointerClickHandler, IEventSystemHandler |
| 41 | public TrainingGroundsSlot Slot |
| 68 | public void SetupSlot(TrainingGrounds parent, int idx) |
| 74 | public void SetupSlot(Inn parent, int idx) |
| 80 | public void UpdateSlot() |
| 181 | public string GetTooltipTitle() |
| 186 | public void AddTooltipCustomContent(UITooltip tooltip) |
| 201 | public void OnPointerClick(PointerEventData eventData) |

## Documented by

| Wiki article |
| --- |
| [Character, training, recovery, and Arena displays](character-and-training-displays.md) |

## Sources

- `Assets.Behaviour.Flow.Elements/WorldFlowTrainingGroundsSlot.cs:1`
