# WorldFlowStockpile — source reference

Assets.Behaviour.Flow.Elements/WorldFlowStockpile.cs · 110 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 15 | public class WorldFlowStockpile : MonoBehaviour, ITooltipTitleSource, ITooltipCustomSource |
| 70 | public string GetTooltipTitle() |
| 75 | public void ToggleCapacitySlider() |
| 87 | public void UpdateSlider() |
| 95 | public void SliderReleased() |
| 101 | public void AddTooltipCustomContent(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Stockpiles and overflow](production-stockpiles.md) |

## Sources

- `Assets.Behaviour.Flow.Elements/WorldFlowStockpile.cs:1`
