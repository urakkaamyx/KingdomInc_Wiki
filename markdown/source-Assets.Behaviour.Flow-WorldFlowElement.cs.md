# WorldFlowElement — source reference

Assets.Behaviour.Flow/WorldFlowElement.cs · 475 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 19 | public class WorldFlowElement : MonoBehaviour, IPointerClickHandler, IEventSystemHandler, IPointerEnterHandler, IPointerExitHandler |
| 73 | public Action OnUpdateIcon |
| 79 | public Sprite BackgroundSprite => _background.sprite |
| 82 | public FlowCollider Collider { get; private set; } |
| 84 | public FlowElement Element { get; private set; } |
| 86 | public Vector2Int Position => Element.Position |
| 88 | public Vector2 Size |
| 97 | public Vector2 FloatingIconPos |
| 114 | public Vector2 Center => new Vector2((float)Position.x + Size.x / 2f, (float)Position.y - Size.y / 2f) |
| 144 | public void SetStackSize(int stackSize) |
| 181 | public void SetElement(FlowElement element) |
| 188 | public void UpdateVisuals() |
| 204 | public void UpdateIcon(Sprite icon = null) |
| 213 | public void UpdateLabel(string label = null) |
| 228 | public void UpdateUpgradeSlots() |
| 250 | public void UpdateIO() |
| 268 | public void ShowCraftButton(bool show) |
| 342 | public bool UpdatePosition(Vector2Int pos) |
| 360 | public void ClickCraft() |
| 365 | public void OnPointerClick(PointerEventData eventData) |
| 402 | public void AttemptStackElement() |
| 429 | public void StartPicker() |
| 444 | public void ShowIncome(Currency c, long amt, bool force = false) |
| 452 | public void ShowMessage(string msg, Color c) |
| 460 | public void OnPointerExit(PointerEventData eventData) |
| 466 | public void OnPointerEnter(PointerEventData eventData) |

## Documented by

| Wiki article |
| --- |
| [Machine stacks, mirrored ports, and upgrade slots](machine-stacks-upgrade-controls.md) |

## Sources

- `Assets.Behaviour.Flow/WorldFlowElement.cs:1`
