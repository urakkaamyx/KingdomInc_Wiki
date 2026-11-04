# CraftingReagent — source reference

Assets.Source.Items/CraftingReagent.cs · 40 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 5 | public class CraftingReagent |
| 7 | public readonly ItemType Item |
| 9 | public readonly bool ItemAffectsValue = true |
| 11 | public readonly string ReagentText |
| 13 | public readonly FlowIO.FlowFilter ItemFilter |
| 15 | public readonly int Count |
| 17 | public string IconName |
| 19 | public bool AffectsQuality = true |
| 21 | public bool PreviewFilter |
| 23 | public CraftingReagent(ItemType item, int count) |
| 30 | public CraftingReagent(FlowIO.FlowFilter filter, int count, ItemType preview = null, string previewText = null) |

## Documented by

| Wiki article |
| --- |
| [Crafting, recipes, and automatic work](production-crafting.md) |

## Sources

- `Assets.Source.Items/CraftingReagent.cs:1`
