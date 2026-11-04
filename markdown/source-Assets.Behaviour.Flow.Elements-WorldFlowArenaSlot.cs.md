# WorldFlowArenaSlot — source reference

Assets.Behaviour.Flow.Elements/WorldFlowArenaSlot.cs · 64 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public class WorldFlowArenaSlot : WorldFlowCombatant, ITooltipTitleSource, ITooltipCustomSource, IPointerClickHandler, IEventSystemHandler |
| 25 | public override void SetCombatant(CombatantItemData c) |
| 34 | public void SetBlocked() |
| 42 | public string GetTooltipTitle() |
| 47 | public void AddTooltipCustomContent(UITooltip tooltip) |
| 57 | public void OnPointerClick(PointerEventData eventData) |

## Documented by

| Wiki article |
| --- |
| [Character, training, recovery, and Arena displays](character-and-training-displays.md) |

## Sources

- `Assets.Behaviour.Flow.Elements/WorldFlowArenaSlot.cs:1`
