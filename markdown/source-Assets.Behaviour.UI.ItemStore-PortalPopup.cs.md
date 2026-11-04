# PortalPopup — source reference

Assets.Behaviour.UI.ItemStore/PortalPopup.cs · 149 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 10 | public class PortalPopup : UIPopupMenu |
| 39 | public static PortalPopup Instance { get; private set; } |
| 41 | public WorldFlowPortal Element { get; private set; } |
| 65 | public void SetElement(WorldFlowPortal element) |
| 103 | public void ChannelSelected(int ch) |
| 119 | public void IndexSelected(int ch) |
| 134 | public void SetAsInput() |
| 142 | public void SetAsOutput() |

## Documented by

| Wiki article |
| --- |
| [Armory and Portal configuration](storage-panel-controls.md) |

## Sources

- `Assets.Behaviour.UI.ItemStore/PortalPopup.cs:1`
