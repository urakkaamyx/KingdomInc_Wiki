# UIAlertWindow — source reference

Assets.Behaviour.UI/UIAlertWindow.cs · 115 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public class UIAlertWindow : MonoBehaviour |
| 26 | public static bool Active |
| 38 | public static void Init(UIAlertWindow instance) |
| 43 | public static void Show(string title, string message, Action onClose = null) |
| 51 | public static void Query(string title, string message, Action onYes = null, Action onNo = null) |
| 66 | public static void Show(string title, string message, string[] buttons, Action<string> onClick) |
| 74 | public static void Hide() |
| 83 | public void ShowAlert(string title, string message, string[] buttons, Action<string> onClick) |

## Documented by

| Wiki article |
| --- |
| [Tooltips, warnings, notifications, and tutorial cues](tooltips-warnings-and-tutorial.md) |

## Sources

- `Assets.Behaviour.UI/UIAlertWindow.cs:1`
