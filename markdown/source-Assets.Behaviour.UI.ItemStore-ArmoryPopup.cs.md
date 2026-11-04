# ArmoryPopup — source reference

Assets.Behaviour.UI.ItemStore/ArmoryPopup.cs · 157 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 14 | public class ArmoryPopup : UIPopupMenu |
| 48 | public static ArmoryPopup Instance { get; private set; } |
| 50 | public WorldFlowArmory Element { get; private set; } |
| 57 | public void SetElement(WorldFlowArmory element) |
| 112 | public void ChannelSelected(int ch) |
| 126 | public void ItemSelected(ItemType item, bool close = true) |

## Documented by

| Wiki article |
| --- |
| [Armory and Portal configuration](storage-panel-controls.md) |

## Sources

- `Assets.Behaviour.UI.ItemStore/ArmoryPopup.cs:1`
