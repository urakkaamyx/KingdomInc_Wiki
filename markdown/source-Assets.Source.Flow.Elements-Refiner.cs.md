# Refiner — source reference

Assets.Source.Flow.Elements/Refiner.cs · 189 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public class Refiner : FlowElement |
| 17 | public const float CriticalCraftChance = 0.01f |
| 19 | public const float MinFailChance = 0.25f |
| 21 | public const float MaxFailChance = 0.95f |
| 25 | public InventoryItem LastItem |
| 27 | public float LastQuality |
| 29 | public float LastNewQuality |
| 31 | public int LastManaCost |
| 33 | public override string Label => "@refiner" |
| 35 | public override ElementCategory Category => ElementCategory.Utility |
| 37 | public override string IconName => "Icons_157" |
| 39 | public override bool HasCraftButton => false |
| 41 | public bool UseMana { get; private set; } |
| 43 | public Refiner() |
| 77 | public override void OnCreateElement() |
| 90 | public override void Update(float delta) |
| 145 | public float GetFailChance(InventoryItem item, bool? overrideMana = null) |
| 160 | public int GetManaCost(InventoryItem item) |
| 165 | public void ToggleUseMana(bool? toggleTo = null) |
| 171 | protected override void CopySettingsTo(FlowElement copy) |
| 176 | protected override void DataToJson(JsonObject data) |
| 184 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Refiner](building-Refiner.md) |
| [Refining and destruction risk](production-refining.md) |

## Sources

- `Assets.Source.Flow.Elements/Refiner.cs:1`
