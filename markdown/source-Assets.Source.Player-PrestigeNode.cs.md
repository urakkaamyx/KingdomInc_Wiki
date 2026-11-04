# PrestigeNode — source reference

Assets.Source.Player/PrestigeNode.cs · 132 lines · 10 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public class PrestigeNode |
| 14 | public static PrestigeNode TechCostReduce = new PrestigeNode("tech_cost_reduce") |
| 21 | public static PrestigeNode ResourceCostReduce = new PrestigeNode("resource_cost_reduce") |
| 28 | public static PrestigeNode CurrencyTaxReduce = new PrestigeNode("currency_tax_reduce") |
| 35 | public static PrestigeNode EquipmentQuality = new PrestigeNode("equipment_quality") |
| 42 | public static PrestigeNode HumanQuality = new PrestigeNode("human_quality") |
| 49 | public static PrestigeNode HandcraftingProductivity = new PrestigeNode("handcrafting_productivity") |
| 56 | public static PrestigeNode DarkEssenceQuality = new PrestigeNode("dark_essence_quality") |
| 63 | public static PrestigeNode HumanHealth = new PrestigeNode("human_health") |
| 70 | public static PrestigeNode SellValue = new PrestigeNode("sell_value") |
| 77 | public readonly string Identifier |
| 79 | public readonly int Index |
| 81 | public Func<int, int> GetCost |
| 83 | public string DisplayName |
| 85 | public string IconName |
| 87 | public Vector2Int Position |
| 89 | public Func<int, string> CreateDescription |
| 91 | public static int Count => _orderedNodes.Count |
| 93 | public static IEnumerable<PrestigeNode> All => _orderedNodes |
| 95 | public Func<int, float> CalcValue { private get; set; } |
| 97 | public int CurrentPoints => GamePlayer.Current.GetPrestigePoints(this) |
| 99 | public float CurrentValue => GetValue(CurrentPoints) |
| 101 | public int NextPointCost => GetCost(CurrentPoints) |
| 103 | public PrestigeNode(string identifier) |
| 114 | public float GetValue(int points) |
| 123 | public static PrestigeNode Get(string id) |
| 128 | public static PrestigeNode Get(int idx) |

## Documented by

| Wiki article |
| --- |
| [Prestige perks and refunds](prestige-perks.md) |
| [Offshore Tax Account](prestige-CurrencyTaxReduce.md) |
| [Darkest Essence](prestige-DarkEssenceQuality.md) |
| [Mark of Quality](prestige-EquipmentQuality.md) |
| [I'll Do It Myself](prestige-HandcraftingProductivity.md) |
| [Heroes of Yensburg](prestige-HumanHealth.md) |
| [Mark of Experience](prestige-HumanQuality.md) |
| [Resource Hoarder](prestige-ResourceCostReduce.md) |
| [Otherworldly Negotiations](prestige-SellValue.md) |
| [Techno-wizard](prestige-TechCostReduce.md) |

## Sources

- `Assets.Source.Player/PrestigeNode.cs:1`
