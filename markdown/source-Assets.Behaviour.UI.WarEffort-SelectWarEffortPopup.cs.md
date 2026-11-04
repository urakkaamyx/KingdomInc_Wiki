# SelectWarEffortPopup — source reference

Assets.Behaviour.UI.WarEffort/SelectWarEffortPopup.cs · 47 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 9 | public class SelectWarEffortPopup : UIPopupMenu |
| 17 | public bool ReopenBuyMenu { get; set; } |
| 19 | public WorldFlowWarEffort Element { get; private set; } |
| 21 | public void SetElement(WorldFlowWarEffort element) |
| 35 | public void WarEffortSelected(WarType war) |
| 43 | public void GoToWarEffortMenu() |

## Documented by

| Wiki article |
| --- |
| [War selection and status panels](war-panel-controls.md) |

## Sources

- `Assets.Behaviour.UI.WarEffort/SelectWarEffortPopup.cs:1`
