# Currencies and the exchange

Gold equivalents, eligible currencies, taxes, and rounding.

## Gold equivalents

Currencies have fixed gold equivalents used for conversion and prices: Gold 1, Requisition 1,000, Medal 600, Ring 1,200, Mana 11, Crown 2,400, Ducat 5,200, Ingenuity 200, and Faith 100.

Mana, Ingenuity, and Faith are explicitly nontradeable. The currency interface exposes exchange on tradeable non-Gold currencies after Currency Exchange technology is owned.

## Tax formula

Base exchange tax is 1, meaning 100%. Currency Exchange Tax technology halves it to 0.5. Currency Tax Reduction prestige further multiplies tax by 1 minus its current bonus.

Buying N units costs trunc(N × gold equivalent × (1 + tax)) Gold. Selling N units receives trunc(N × gold equivalent ÷ (1 + tax)) Gold. The buy and sell formulas use opposite sides of the same multiplier, so a round trip loses value.

## Example and accounting

At the base 100% tax, one Requisition costs 2,000 Gold to buy and sells for 500 Gold. At 50% tax it costs 1,500 and sells for 666 after truncation.

Exchange credits use isIncome = false, unlike normal production rewards. The purchase slider's maximum is floor(available Gold ÷ taxed unit price). Currency unlocks come from their associated production or progression technology.

## Sources

- `Assets.Source.Player/CurrencyExtensions.cs:7`
- `Assets.Source.Player/CurrencyExtensions.cs:23`
- `Assets.Source.Player/CurrencyExtensions.cs:71`
- `Assets.Source.Player/GamePlayer.cs:654`
- `Assets.Behaviour.UI.CurrencyExchange/CurrencyExchangePopup.cs:63`
- `Assets.Behaviour.UI.CurrencyExchange/CurrencyExchangePopup.cs:85`
- `Assets.Behaviour.UI.Shared/CurrencyCell.cs:66`
