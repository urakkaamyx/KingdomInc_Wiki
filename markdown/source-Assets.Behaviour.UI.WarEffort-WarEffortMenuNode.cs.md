# WarEffortMenuNode — source reference

Assets.Behaviour.UI.WarEffort/WarEffortMenuNode.cs · 52 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 10 | public class WarEffortMenuNode : MonoBehaviour, ITooltipTitleSource, ITooltipCustomSource |
| 18 | public WarStage Stage { get; private set; } |
| 20 | public float RightX => transform.localPosition.x + 39f |
| 22 | public float LeftX => transform.localPosition.x - 39f |
| 24 | public void SetWar(WarStage stage) |
| 31 | public void UpdateProgress() |
| 39 | public string GetTooltipTitle() |
| 44 | public void AddTooltipCustomContent(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [War selection and status panels](war-panel-controls.md) |

## Sources

- `Assets.Behaviour.UI.WarEffort/WarEffortMenuNode.cs:1`
