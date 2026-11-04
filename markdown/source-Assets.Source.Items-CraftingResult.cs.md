# CraftingResult — source reference

Assets.Source.Items/CraftingResult.cs · 103 lines · 4 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 9 | public class CraftingResult |
| 11 | public delegate InventoryItem CraftingResultCreator(CraftingInput input, float quality) |
| 13 | public ItemType Item |
| 15 | public ItemType TransformTo |
| 17 | public ItemEnhancement Enhancement |
| 19 | public int Count |
| 21 | public bool HasOutput = true |
| 23 | public int OutputIndex = -1 |
| 25 | public int BufferSize = 5 |
| 27 | public float Probability |
| 29 | public Sprite OverrideIcon |
| 31 | public Func<float, string> OverrideText |
| 33 | public readonly CraftingResultCreator Result |
| 35 | public CraftingResult(CraftingResultCreator creator, string icon, Func<float, string> text) |
| 43 | public CraftingResult(ItemEnhancement enhancement) |
| 67 | public CraftingResult(ItemType item, int count) |
| 84 | public CraftingResult(ItemType item, float frac) |
| 90 | public static CraftingResult TransformAdventurer(int slot, ItemType transformTo) |

## Documented by

| Wiki article |
| --- |
| [Prestige perks and refunds](prestige-perks.md) |
| [Enchanting, engraving, and blessings](production-enhancements.md) |
| [Item quality and critical crafting](production-quality.md) |
| [Summoning and necromancy](production-summoning-necromancy.md) |

## Sources

- `Assets.Source.Items/CraftingResult.cs:1`
