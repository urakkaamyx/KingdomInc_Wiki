# Currency HUD and coin denominations

Interpret raw Gold units, copper/silver/gold icons, affordability, and exchange clicks.

## One stored Gold unit is the smallest coin unit

Currency.Gold is stored as an integer, but the UI splits it into denominations: copper=amount%100, silver=(amount/100)%100, gold=amount/10000. Thus 100 raw Gold units display as 1 silver and 10,000 as 1 gold. Source-derived numeric costs in raw collections must be converted before labeling them displayed gold coins.

## Compact HUD

The currency pane refreshes about every 0.2 seconds. With fewer than four currency kinds it forces copper visible; below six it retains silver. More populated HUDs can hide small denominations to fit. Hovering while a tooltip is active postpones rebuilding the currency rows. Values in tooltips also use coin denominations and can omit copper when gold is present.

## Cost and value displays

CurrencyDisplay can mark insufficient balances with a configured color and show No Cost for an empty collection. CurrencyDisplayLite presents machine income with a specialist currency beside coins. TooltipCost rebuilds its layout; TooltipValue presents a compact multi-currency value line.

## Exchange gesture

After currency_exchange, left click a tradeable non-Gold currency cell to buy, right click to sell. Mana, Ingenuity and Faith display an exchange-disabled message. Hover shows the currency description. This shortcut applies to currency cells carrying their tooltip/component, not arbitrary artwork shaped like coins.

## Sources

- `Assets.Behaviour.UI.HUD/CurrencyPane.cs:18`
- `Assets.Behaviour.UI.Shared/CurrencyCell.cs:26`
- `Assets.Behaviour.UI.Shared/CurrencyDisplay.cs:43`
- `Assets.Behaviour.UI.Shared/CurrencyDisplayLite.cs:38`
- `Assets.Behaviour.UI.Tooltip/UITooltipCost.cs:19`
- `Assets.Behaviour.UI.Tooltip/UITooltipValue.cs:32`
