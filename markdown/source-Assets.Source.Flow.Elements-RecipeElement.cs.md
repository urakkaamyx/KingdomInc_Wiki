# RecipeElement — source reference

Assets.Source.Flow.Elements/RecipeElement.cs · 462 lines · 8 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 14 | public abstract class RecipeElement : FlowElement |
| 16 | public RecipeTag CraftableTag |
| 18 | public CraftingRecipe Recipe |
| 20 | public CraftingInput Input |
| 22 | public bool IsEquipment |
| 28 | public bool ProductivityDisabled |
| 30 | public bool Crafting => Input != null |
| 32 | public override string Label => DefaultLabel |
| 34 | public override string IconName => Recipe?.IconName ?? DefaultIconName |
| 36 | public abstract string DefaultLabel { get; } |
| 38 | public abstract string DefaultIconName { get; } |
| 40 | public override bool HasCraftButton |
| 52 | public override ElementCategory Category => ElementCategory.Crafting |
| 54 | public virtual float ManualProgress => 1f / Recipe.CraftingTime / 2.5f * Speed |
| 56 | public override bool Stackable => true |
| 58 | public RecipeElement() |
| 62 | public virtual bool CanCraft(CraftingRecipe recipe) |
| 67 | public CurrencyCollection GetCraftingCost(CraftingRecipe recipe = null) |
| 96 | public void SetupRecipe(CraftingRecipe cr, bool isNew = true) |
| 159 | public override void UpdateUpgrades() |
| 185 | public override void Update(float delta) |
| 331 | public (float min, float max) GetQualityRange(bool useInput) |
| 364 | public float GetOutputQuality(float minQuality, float maxQuality) |
| 374 | public override float GetCraftEffectsVolume() |
| 383 | public override bool CanManualCraft() |
| 392 | public override void DoManualCraft() |
| 412 | public IEnumerable<CraftingRecipe> GetAvailableRecipes() |
| 423 | protected virtual bool IsCraftable(CraftingRecipe recipe) |
| 428 | protected override void CopySettingsTo(FlowElement copy) |
| 436 | public override bool HandleReopenBuyMenu() |
| 442 | protected override void DataToJson(JsonObject data) |
| 451 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Prestige perks and refunds](prestige-perks.md) |
| [Crafting, recipes, and automatic work](production-crafting.md) |
| [Enchanting, engraving, and blessings](production-enhancements.md) |
| [Inventors, experiments, and Ingenuity](production-inventor.md) |
| [Productivity and handcrafting](production-productivity.md) |
| [Item quality and critical crafting](production-quality.md) |
| [Production simulation and bottlenecks](production-simulation.md) |
| [Crafting workshops and their roles](production-workshops.md) |

## Sources

- `Assets.Source.Flow.Elements/RecipeElement.cs:1`
