# FlowOptionsPopup — source reference

Assets.Behaviour.UI.SwapFlow/FlowOptionsPopup.cs · 111 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 12 | public class FlowOptionsPopup : UIPopupMenu |
| 35 | public void SetFlow(FlowDiagram flow) |
| 45 | public void IconSelected(string iconName) |
| 56 | public override void PopupClosed() |
| 61 | public void ButtonSave() |
| 67 | public void EndEdit() |
| 75 | public void ToggleSearch() |
| 91 | public void UpdateIcons() |
| 107 | public static IEnumerable<(string icon, string name)> GetAvailableFlowIcons() |

## Documented by

| Wiki article |
| --- |
| [Workflow tabs, names, icons, and ordering](workflow-tabs-and-labels.md) |

## Sources

- `Assets.Behaviour.UI.SwapFlow/FlowOptionsPopup.cs:1`
