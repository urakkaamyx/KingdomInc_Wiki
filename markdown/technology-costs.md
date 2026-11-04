# Technology cost formula

Deterministic prices, type multipliers, currency conversion, rounding, and prestige.

## Raw price

At technology cost tier t, P = 400 × typeMultiplier × CostMultiplier × 2^(t−1) × R. R is a deterministic pseudorandom float in [0.92,1.10), seeded from the identifier. Prices do not reroll whenever a menu opens. A zero multiplier creates a free empty collection. Gold numbers in this formula are stored smallest-coin units: 100 units = 1 silver and 10,000 = 1 displayed gold coin.

## Type multipliers

| Type | Multiplier |
| --- | --- |
| FlowElement | 4.5 |
| Utility | 6 |
| UpgradeSlot | 4 |
| UpgradeType | 3 |
| Recipe | 1 |
| Resource | 2 |
| Quest | 2 |
| Dungeon | 5 |
| War | 5 |
| Other, including Decoration | 1 |

## Each currency is a separate charge

Gold = RoundGold(truncate(P × GoldMultiplier × (1 if tier≤1 else 2))). Each non-gold charge is ceil(P/referenceGoldValue); Faith and Ingenuity are then halved with integer division. Gold plus Ducats means both charges, not a split total.

Normal RoundGold leaves values below 10,000 unchanged, rounds 10,000–999,999 to hundreds, and rounds 1,000,000 or more to ten-thousands. The helper supports another maxCount mode for other callers.

## Default currencies

| Tier | Currency collection |
| --- | --- |
| 1 | Gold |
| 2 | Gold + Requisition |
| 3–4 | Gold + Medal |
| 5–7 | Gold + Ring |
| 8–15 | Gold + Ducat |
| 16 and above | Gold |

## Prestige and caching

TechCostReduce multiplies the generated collection by 1−perkValue and rounds each result with Math.Round. TechNode caches costs; GameManager resets every cached cost at scene start. Explicit currency/multiplier overrides take priority. Non-technology buildings share CreateCost but use a different tier-scaling branch.

## Sources

- `Assets.Source.Player/TechNode.cs:244`
- `Assets.Source.Player/TechNode.cs:263`
- `Assets.Source.Player/CurrencyCollection.cs:169`
- `Assets.Source.Player/CurrencyCollection.cs:98`
- `Assets.Source.Player/CurrencyCollection.cs:221`
- `Assets.Source.Util/GameMath.cs:88`
- `Assets.Behaviour/GameManager.cs:24`
