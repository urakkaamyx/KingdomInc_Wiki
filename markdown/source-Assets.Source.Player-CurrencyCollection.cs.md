# CurrencyCollection — source reference

Assets.Source.Player/CurrencyCollection.cs · 230 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public class CurrencyCollection |
| 10 | public static IReadOnlyList<Currency> Gold |
| 12 | public static IReadOnlyList<Currency> GoldRequisition |
| 14 | public static IReadOnlyList<Currency> GoldMedal |
| 16 | public static IReadOnlyList<Currency> GoldRing |
| 18 | public static IReadOnlyList<Currency> GoldMana |
| 20 | public static IReadOnlyList<Currency> GoldCrown |
| 22 | public static IReadOnlyList<Currency> GoldDucat |
| 24 | public static IReadOnlyList<Currency> GoldFaith |
| 26 | public static IReadOnlyList<Currency> GoldIngenuity |
| 28 | public static IReadOnlyList<Currency> Requisition |
| 34 | public static int NumCurrencies { get; private set; } |
| 36 | public int CurrencyCount |
| 52 | public bool IsEmpty => CurrencyCount == 0 |
| 106 | public CurrencyCollection() |
| 111 | public CurrencyCollection(long[] amt) |
| 117 | public CurrencyCollection(Currency c, long amt) |
| 123 | public CurrencyCollection(CurrencyCollection clone) |
| 129 | public CurrencyCollection Add(Currency c, long amt) |
| 135 | public CurrencyCollection AddGoldEquivalent(Currency c, long amt) |
| 140 | public CurrencyCollection Add(CurrencyCollection other) |
| 152 | public IEnumerable<(Currency c, long amt)> GetCurrency() |
| 163 | public static IEnumerable<Currency> GetDefaultCostCurrency(int tier) |
| 169 | public static CurrencyCollection CreateCost(string id, double baseCost, double baseMultiplier, double goldMultiplier, int costTier, IEnumerable<Currency> setCurrency, bool isTech) |
| 221 | public static CurrencyCollection operator *(CurrencyCollection c1, double mult) |

## Documented by

| Wiki article |
| --- |
| [Technology cost formula](technology-costs.md) |

## Sources

- `Assets.Source.Player/CurrencyCollection.cs:1`
