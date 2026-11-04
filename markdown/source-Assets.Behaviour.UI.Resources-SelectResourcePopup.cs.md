# SelectResourcePopup — source reference

Assets.Behaviour.UI.Resources/SelectResourcePopup.cs · 68 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 9 | public class SelectResourcePopup : UIPopupMenu |
| 23 | public WorldFlowResource Element { get; private set; } |
| 25 | public bool ReopenBuyMenu { get; set; } |
| 27 | public void SetElement(WorldFlowResource el) |
| 52 | public void ResourceSelected(ResourceItemType res) |
| 64 | public void GoToResourceWindow() |

## Documented by

| Wiki article |
| --- |
| [Resource quotas and supplier configuration](resource-panel-controls.md) |

## Sources

- `Assets.Behaviour.UI.Resources/SelectResourcePopup.cs:1`
