# Luxury Shops and crown chances

Quality goods can produce enhanced gold income and occasional Crowns.

## Eligible items

Luxury Shop is intrinsically automatic. It accepts positive-value, sellable noncombatants only when item Quality is strictly greater than 1. It consumes one buffered item each update and credits proceeds directly.

Gold before rounding equals item SellValue × item Quality. If Quality − 1 is strictly above 0.2, multiply that by 1.2. Sell Value prestige then multiplies it by 1 + its bonus.

## Crown roll

Food never generates Crowns here. For other eligible goods, Quality − 1 must be strictly greater than 0.1 before any Crown roll occurs. The chance is clamp(Quality − 1, 0, 0.5). On success, Crown quantity is the integer part of the pre-rounded gold value divided by 2,400.

A successful roll can still award zero Crowns if the sale value is below one Crown's gold equivalent. The Crown check does not reduce the gold payout. Quality 1.10 or 1.20 sits on a strict threshold rather than automatically receiving the higher-tier effect.

## Sources

- `Assets.Source.Flow.Elements/LuxuryShop.cs:23`
- `Assets.Source.Flow.Elements/LuxuryShop.cs:25`
- `Assets.Source.Flow.Elements/LuxuryShop.cs:38`
- `Assets.Source.Player/CurrencyExtensions.cs:7`
