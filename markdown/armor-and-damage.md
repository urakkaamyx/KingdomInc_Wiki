# Armor and damage reduction

The exact armor curve, unarmored penalty, and damage-processing order.

## Armor curve

For Armor A ≤ 200, ordinary incoming damage is multiplied by 0.5^(A/200). Above 200, first replace A with 200 + (A − 200)^0.8, then apply that exponential. This gives diminishing returns beyond 200.

Exactly zero Armor adds an extra ×2 penalty. Armor-ignoring attacks skip both the curve and zero-armor penalty. Active damage-taken traits apply afterward; the result is rounded and subtracted from health. An incoming value of exactly zero returns immediately.

| Armor | Incoming ordinary damage before traits |
| --- | --- |
| 0 | 200% |
| 100 | about 70.71% |
| 200 | 50% |
| 400 | about 39.32% |
| 800 | about 28.04% |

## Roles and category

Tank multiplies damage taken by 0.75. Guardian with a Shield divides it by 1 + 0.1 × trait quality. These apply after armor and also protect against armor-ignoring attacks.

Armor category is distinct from the numerical Armor stat. Light, Medium, and Heavy tags affect advancement and certain traits. The numerical stat controls the damage curve.

## Sources

- `Assets.Source.Items.Data/CombatantItemData.cs:149`
- `Assets.Source.Items.Data/CombatantItemData.cs:396`
- `Assets.Source.Adventure/AdventurerTrait.cs:94`
- `Assets.Source.Adventure/AdventurerTrait.cs:130`
