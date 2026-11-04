# WorldFlowPortal — source reference

Assets.Behaviour.Flow.Elements/WorldFlowPortal.cs · 143 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 17 | public class WorldFlowPortal : MonoBehaviour, ITooltipTitleSource, ITooltipCustomSource |
| 44 | public Portal Element { get; private set; } |
| 68 | public void UpdateChannel() |
| 83 | public void TogglePopup() |
| 90 | public void DelayTogglePopup() |
| 101 | public void UpdateDirection() |
| 106 | public void CyclePortal() |
| 120 | public string GetTooltipTitle() |
| 125 | public void AddTooltipCustomContent(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Armory and Portal configuration](storage-panel-controls.md) |

## Sources

- `Assets.Behaviour.Flow.Elements/WorldFlowPortal.cs:1`
