# WarEffortSoldierSprite — source reference

Assets.Behaviour.UI.WarEffort/WarEffortSoldierSprite.cs · 214 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 14 | public class WarEffortSoldierSprite : MonoBehaviour, ITooltipTitleSource, ITooltipCustomSource, IPointerClickHandler, IEventSystemHandler |
| 16 | public static Color Healthy = new Color32(17, 186, 0, byte.MaxValue) |
| 18 | public static Color Unhealthy = new Color(1f, 0.65f, 0.65f) |
| 44 | public CombatantItemData Combatant { get; private set; } |
| 46 | public InventoryItem Item => Combatant.Item |
| 48 | public bool SlotAvailable => !_character.gameObject.activeSelf |
| 65 | public void SetCharacter(CombatantItemData item) |
| 152 | public string GetTooltipTitle() |
| 157 | public void AddTooltipCustomContent(UITooltip tooltip) |
| 179 | public void OnPointerClick(PointerEventData eventData) |
| 205 | public static Color GetHealthColor(float hp) |

## Documented by

| Wiki article |
| --- |
| [War selection and status panels](war-panel-controls.md) |

## Sources

- `Assets.Behaviour.UI.WarEffort/WarEffortSoldierSprite.cs:1`
