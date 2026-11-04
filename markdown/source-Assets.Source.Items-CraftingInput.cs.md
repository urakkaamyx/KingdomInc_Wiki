# CraftingInput — source reference

Assets.Source.Items/CraftingInput.cs · 75 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class CraftingInput |
| 9 | public readonly RecipeElement Parent |
| 13 | public IEnumerable<InventoryItem> AllItems |
| 27 | public CraftingInput(RecipeElement element, CraftingRecipe recipe) |
| 37 | public void AddItem(int slot, InventoryItem item) |
| 42 | public InventoryItem GetItem(int slot) |
| 51 | public IEnumerable<InventoryItem> GetItems(int slot) |
| 56 | public JsonValue ToJson() |
| 66 | public static CraftingInput FromJson(JsonArray json, RecipeElement parent, CraftingRecipe cr) |

## Documented by

| Wiki article |
| --- |
| [Data records, serialization, and implementation limits](implementation-data-and-serialization.md) |

## Sources

- `Assets.Source.Items/CraftingInput.cs:1`
