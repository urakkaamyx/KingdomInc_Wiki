# SelectRequisitionRow — source reference

Assets.Behaviour.UI.Requisition/SelectRequisitionRow.cs · 74 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public class SelectRequisitionRow : MonoBehaviour, IPointerClickHandler, IEventSystemHandler |
| 28 | public int Index { get; private set; } |
| 30 | public ItemType Contract { get; private set; } |
| 32 | public void SetContract(int idx, ItemType contract, bool selected) |
| 45 | public void RerollClicked() |
| 67 | public void OnPointerClick(PointerEventData eventData) |

## Documented by

| Wiki article |
| --- |
| [Production status, routing buttons, and recent results](production-status-and-controls.md) |

## Sources

- `Assets.Behaviour.UI.Requisition/SelectRequisitionRow.cs:1`
