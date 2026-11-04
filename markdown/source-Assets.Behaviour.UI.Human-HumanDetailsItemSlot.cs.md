# HumanDetailsItemSlot — source reference

Assets.Behaviour.UI.Human/HumanDetailsItemSlot.cs · 62 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public class HumanDetailsItemSlot : MonoBehaviour, ITooltipTitleSource, ITooltipCustomSource |
| 25 | public EquipmentSlot Slot { get; private set; } |
| 27 | public void SetItem(InventoryItem item) |
| 53 | public string GetTooltipTitle() |
| 58 | public void AddTooltipCustomContent(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Character, training, recovery, and Arena displays](character-and-training-displays.md) |

## Sources

- `Assets.Behaviour.UI.Human/HumanDetailsItemSlot.cs:1`
