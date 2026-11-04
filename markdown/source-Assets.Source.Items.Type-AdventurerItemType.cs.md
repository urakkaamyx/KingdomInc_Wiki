# AdventurerItemType — source reference

Assets.Source.Items.Type/AdventurerItemType.cs · 58 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public class AdventurerItemType : HumanItemType |
| 10 | public Func<GamePlayer, bool> AdvancementUnlocked |
| 12 | public override bool IsUnlocked |
| 40 | public AdventurerItemType(string id) |
| 45 | public override void AddToTooltip(InventoryItem item, UITooltip tooltip) |
| 51 | public void RequirementToTooltip(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Character, training, recovery, and Arena displays](character-and-training-displays.md) |

## Sources

- `Assets.Source.Items.Type/AdventurerItemType.cs:1`
