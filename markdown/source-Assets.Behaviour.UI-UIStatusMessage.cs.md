# UIStatusMessage — source reference

Assets.Behaviour.UI/UIStatusMessage.cs · 154 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 10 | public class UIStatusMessage : MonoBehaviour, IPointerClickHandler, IEventSystemHandler |
| 16 | public CanvasGroup Transparency |
| 18 | public Image StatusIcon |
| 20 | public TMP_Text StatusText |
| 22 | public Action OnClick |
| 64 | public IEnumerator FadeIn() |
| 81 | public IEnumerator FadeOut() |
| 94 | public void OnPointerClick(PointerEventData eventData) |
| 100 | public void CloseMessage() |
| 105 | public void SetPersistent(bool persistent) |
| 110 | public static UIStatusMessage Show(string text, string iconName, bool persistent, Action onClick = null) |
| 115 | public static UIStatusMessage Show(string text, Sprite icon, bool persistent, Action onClick = null) |
| 148 | public static void InitParent(RectTransform container, UIStatusMessage prefab) |

## Documented by

| Wiki article |
| --- |
| [Tooltips, warnings, notifications, and tutorial cues](tooltips-warnings-and-tutorial.md) |

## Sources

- `Assets.Behaviour.UI/UIStatusMessage.cs:1`
