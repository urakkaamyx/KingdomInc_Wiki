# WorldFlowResource — source reference

Assets.Behaviour.Flow.Elements/WorldFlowResource.cs · 159 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 16 | public class WorldFlowResource : MonoBehaviour, ITooltipTitleSource, ITooltipCustomSource |
| 35 | public ResourceElement Element { get; private set; } |
| 44 | public void SetResource(ResourceItemType res) |
| 57 | public void UpdateResource() |
| 86 | public void ShowResourcePopup() |
| 93 | public void DelayShowResourcePopup() |
| 105 | public string GetTooltipTitle() |
| 114 | public void AddTooltipCustomContent(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Resource quotas and supplier configuration](resource-panel-controls.md) |

## Sources

- `Assets.Behaviour.Flow.Elements/WorldFlowResource.cs:1`
