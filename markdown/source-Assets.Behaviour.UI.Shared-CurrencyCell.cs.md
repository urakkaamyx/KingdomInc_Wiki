# CurrencyCell — source reference

Assets.Behaviour.UI.Shared/CurrencyCell.cs · 81 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 13 | public class CurrencyCell : MonoBehaviour, ITooltipTitleSource, ITooltipCustomSource, IPointerClickHandler, IEventSystemHandler |
| 26 | public void SetCurrency(Currency curr, long amt, Color c) |
| 32 | public void SetCurrency(Sprite icon, long amt, Color c) |
| 41 | public string GetTooltipTitle() |
| 46 | public void AddTooltipCustomContent(UITooltip tooltip) |
| 64 | public void OnPointerClick(PointerEventData eventData) |

## Documented by

| Wiki article |
| --- |
| [Currency HUD and coin denominations](currency-hud-and-denominations.md) |
| [Currencies and the exchange](production-currency-exchange.md) |

## Sources

- `Assets.Behaviour.UI.Shared/CurrencyCell.cs:1`
