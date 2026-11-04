# UITechNode — source reference

Assets.Behaviour.UI.TechTree/UITechNode.cs · 198 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 13 | public class UITechNode : MonoBehaviour, IPointerEnterHandler, IEventSystemHandler, IPointerExitHandler, IPointerClickHandler, ITooltipTitleSource, ITooltipCustomSource |
| 16 | protected Image _background |
| 19 | protected Image _icon |
| 22 | protected Image _highlight |
| 25 | protected Image _glow |
| 28 | protected Image _purchased |
| 31 | protected Sprite _lockedIcon |
| 39 | public TechNode Tech { get; private set; } |
| 41 | public TechTreeMenu Parent { get; private set; } |
| 48 | protected virtual void Start() |
| 54 | public virtual void UpdateNodeStatus() |
| 72 | public virtual void SetTech(TechNode node) |
| 78 | protected virtual void Update() |
| 91 | public virtual void OnPointerEnter(PointerEventData eventData) |
| 99 | public virtual void OnPointerExit(PointerEventData eventData) |
| 104 | public virtual void OnPointerClick(PointerEventData eventData) |
| 125 | public virtual string GetTooltipTitle() |
| 130 | public virtual void AddTooltipCustomContent(UITooltip tooltip) |
| 135 | public static void AddToTooltip(UITooltip tooltip, TechNode tech) |
| 189 | protected static string _getRequirementDescription(TechNode req, TechNode self) |

## Documented by

| Wiki article |
| --- |
| [Technology requirements and unlocking](technology-rules.md) |

## Sources

- `Assets.Behaviour.UI.TechTree/UITechNode.cs:1`
