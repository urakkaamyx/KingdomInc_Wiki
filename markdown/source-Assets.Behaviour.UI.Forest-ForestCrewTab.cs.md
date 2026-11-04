# ForestCrewTab — source reference

Assets.Behaviour.UI.Forest/ForestCrewTab.cs · 155 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 14 | public class ForestCrewTab : MonoBehaviour, ITooltipTitleSource, ITooltipCustomSource |
| 46 | public ForestWorker WorkerType => _workerType |
| 70 | public void StartAnimation() |
| 75 | public void UpdateWorkerCount() |
| 84 | public void ButtonAdd() |
| 118 | public void ButtonSubtract() |
| 131 | public string GetTooltipTitle() |
| 136 | public void AddTooltipCustomContent(UITooltip tooltip) |
| 151 | public void SetBlocked(bool blocked) |

## Documented by

| Wiki article |
| --- |
| [Forest crew and harvest controls](forest-panel-controls.md) |

## Sources

- `Assets.Behaviour.UI.Forest/ForestCrewTab.cs:1`
