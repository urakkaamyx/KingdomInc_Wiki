# WorldFlowUpgrade — source reference

Assets.Behaviour.Flow/WorldFlowUpgrade.cs · 146 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 14 | public class WorldFlowUpgrade : MonoBehaviour, ITooltipTitleSource, ITooltipCustomSource |
| 31 | public WorldFlowElement Parent |
| 33 | public int Slot |
| 35 | public FlowUpgrade Upgrade |
| 46 | public void SetUpgrade(int slot, FlowUpgrade upgrade) |
| 60 | public void ToggleOptionSelect() |
| 65 | public void ToggleOptionSelect(bool allowEasyUpgrade) |
| 92 | public void SelectNewUpgrade(FlowUpgrade upgrade) |
| 115 | public string GetTooltipTitle() |
| 120 | public void AddTooltipCustomContent(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Machine stacks, mirrored ports, and upgrade slots](machine-stacks-upgrade-controls.md) |

## Sources

- `Assets.Behaviour.Flow/WorldFlowUpgrade.cs:1`
