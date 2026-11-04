# AdventurerAdvancement — source reference

Assets.Source.Adventure/AdventurerAdvancement.cs · 22 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 5 | public class AdventurerAdvancement |
| 7 | public delegate bool IsAvailableFor(HumanItemData item) |
| 9 | public delegate void ApplyAdvancement(HumanItemData item) |
| 11 | public string DisplayName |
| 13 | public string Description |
| 15 | public string IconName |
| 17 | public AdvancementSource Source |
| 19 | public IsAvailableFor Available = (HumanItemData hid) => false |
| 21 | public ApplyAdvancement Apply |

## Documented by

| Wiki article |
| --- |
| [Character, training, recovery, and Arena displays](character-and-training-displays.md) |

## Sources

- `Assets.Source.Adventure/AdventurerAdvancement.cs:1`
