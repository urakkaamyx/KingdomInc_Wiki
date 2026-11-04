# Arena audience income

How initial health, weapons, fighter types, and upgrades determine bout payment.

## Reward multiplier

At fight start, multiply both fighters’ current health fractions. Halve that result for each human without a main-hand weapon. This initial value is retained until resolution, so starting wounded reduces the entire bout’s reward.

At resolution, multiply by 1 + 0.1 × Arena Cashier upgrade count. Each Adventurer then contributes ×1.2; each other human contributes ×1.1; nonhumans add no type multiplier. With Blood Sport, a multiplier above 1 receives another ×1.25.

## Payment currency

Currency is selected with successive independent 25% checks, gated by strict reward thresholds. First try Ducats if the multiplier exceeds 1.5; if that fails or is unavailable, try Rings above 1.25, then Crowns above 1.09. Otherwise pay Gold.

Payment count is round(10,000 × final reward multiplier ÷ selected currency’s gold value). This changes the denomination, while the formula targets the same gold-equivalent amount. A resolved bout sets a four-second cooldown.

## Sources

- `Assets.Source.Flow.Elements/Arena.cs:135`
- `Assets.Source.Flow.Elements/Arena.cs:299`
- `Assets.Source.Flow.Elements/Arena.cs:321`
- `Assets.Source.Flow.Elements/Arena.cs:329`
