# WorldFlowArmory — source reference

Assets.Behaviour.Flow.Elements/WorldFlowArmory.cs · 131 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 17 | public class WorldFlowArmory : MonoBehaviour, ITooltipTitleSource, ITooltipCustomSource |
| 27 | public Armory Element { get; private set; } |
| 59 | public void UpdateChannel() |
| 65 | public void DelayTogglePopup() |
| 76 | public void TogglePopup() |
| 83 | public void CycleArmory() |
| 97 | public string GetTooltipTitle() |
| 102 | public void AddTooltipCustomContent(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Armory and Portal configuration](storage-panel-controls.md) |

## Sources

- `Assets.Behaviour.Flow.Elements/WorldFlowArmory.cs:1`
