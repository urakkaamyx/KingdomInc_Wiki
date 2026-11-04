# Restaurants, food, and Crowns

Meals generate Gold and probabilistic Crown income.

## Food sales

A Restaurant accepts sellable, positive-value equipment in the Food slot. A sale starts with V = SellValue × (1 + 0.05 × Cashier count). If the food has any enhancement, V is multiplied by 1.2.

Crown score is V ÷ 2,400 × (1 + 0.1 × Restaurant Crowns count). Halve that score when the food's default recipe is missing or is not tagged Kitchen; this includes Campfire foods even when made inside a Kitchen.

## How Crown score resolves

While the remaining score is positive, the game tests a random chance equal to that score, awarding one Crown and subtracting one on success. Scores of at least 1 therefore guarantee their whole-number portion and roll the fractional remainder.

If item Quality is strictly greater than 1.2, the gold value receives a Big Tippers multiplier of 1 + min(0.5, 0.5 × Big Tippers count × (Quality − 0.8)). This bonus is applied after the Crown score is calculated.

If at least one Crown was won, gold value is halved. The final gold amount is rounded and both rewards are stored locally. Restaurant does not read Sell Value prestige in its sale code.

## Collection

A Worker collects both currencies every 10 ÷ Speed seconds. Manual collection also takes both balances, though the manual-availability check requires stored Gold greater than zero. There is no local storage cap in Restaurant's code.

## Sources

- `Assets.Source.Flow.Elements/Restaurant.cs:38`
- `Assets.Source.Flow.Elements/Restaurant.cs:51`
- `Assets.Source.Flow.Elements/Restaurant.cs:102`
- `Assets.Source.Flow.Elements/Restaurant.cs:110`
- `Assets.Source.Flow.Elements/Restaurant.cs:134`
- `Assets.Source.Flow.Elements/Restaurant.cs:158`
