# Kitchen — source reference

Assets.Source.Flow.Elements/Kitchen.cs · 36 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 6 | public class Kitchen : RecipeElement |
| 8 | public override string DefaultLabel => "@kitchen" |
| 10 | public override string DefaultIconName => "Icons_184" |
| 12 | public override string MusicTrack => "Kingdom Wonder LOOP BPM70" |
| 14 | public Kitchen() |
| 22 | public override void UpdateUpgrades() |
| 28 | protected override bool IsCraftable(CraftingRecipe recipe) |

## Documented by

| Wiki article |
| --- |
| [Kitchen](building-Kitchen.md) |
| [Crafting workshops and their roles](production-workshops.md) |

## Sources

- `Assets.Source.Flow.Elements/Kitchen.cs:1`
