# Currencies and currency exchange

All nine currencies and exact exchange rates and taxes.

## Currency reference

| Currency | Reference value in raw Gold units | Unlock visibility | Tradeable |
| --- | --- | --- | --- |
| Gold | 1 | Always | Yes |
| Requisition | 1,000 | requisition_office | Yes |
| Medal | 600 | war_effort | Yes |
| Ring | 1,200 | quest_board | Yes |
| Mana | 11 | enchanter | No |
| Crown | 2,400 | restaurant | Yes |
| Ducat | 5,200 | dungeon | Yes |
| Ingenuity | 200 | inventor | No |
| Faith | 100 | shrine | No |

## Reference values

Values convert generated gold-equivalent costs into secondary currency amounts and provide exchange base rates. Balances and earned totals are separate. Spending a collection first checks affordability of every included currency.

## Exchange

currency_exchange follows Inventor; currency_exchange_tax follows it. Base tax is 1.0 (100%). Tax research halves it to 0.5. Prestige then multiplies tax by 1−CurrencyTaxReduce value.

Buying A units at reference value V costs truncate(A×V×(1+tax)) raw Gold units. Selling yields truncate(A×V/(1+tax)). At base tax, a Requisition costs 2,000 raw units (20 silver) and sells for 500 (5 silver); with only tax research it costs 1,500 (15 silver) and sells for 666 (6 silver, 66 copper).

## Income statistics

Exchange outputs use isIncome=false and do not count as earned Gold. Buy slider maximum uses affordable Gold; sell maximum uses currency balance.

## Sources

- `Assets.Source.Player/CurrencyExtensions.cs:7`
- `Assets.Source.Player/CurrencyExtensions.cs:23`
- `Assets.Source.Player/CurrencyExtensions.cs:71`
- `Assets.Source.Player/GamePlayer.cs:211`
- `Assets.Source.Player/GamePlayer.cs:654`
- `Assets.Behaviour.UI.CurrencyExchange/CurrencyExchangePopup.cs:63`
- `Assets.Behaviour.UI.CurrencyExchange/CurrencyExchangePopup.cs:85`
- `Assets.Source.Player.Tech/T10Inventor.cs:172`
