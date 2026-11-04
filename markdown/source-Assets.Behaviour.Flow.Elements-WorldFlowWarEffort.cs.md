# WorldFlowWarEffort — source reference

Assets.Behaviour.Flow.Elements/WorldFlowWarEffort.cs · 149 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 14 | public class WorldFlowWarEffort : MonoBehaviour, ITooltipTitleSource, ITooltipCustomSource |
| 41 | public WarEffort Element { get; private set; } |
| 95 | public void SetWarType(WarType wt) |
| 102 | public void OpenWarEffortPopup() |
| 109 | public void DelayOpenWarEffortPopup() |
| 121 | public void OpenWarEffortDetails() |
| 133 | public string GetTooltipTitle() |
| 138 | public void AddTooltipCustomContent(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [War selection and status panels](war-panel-controls.md) |

## Sources

- `Assets.Behaviour.Flow.Elements/WorldFlowWarEffort.cs:1`
