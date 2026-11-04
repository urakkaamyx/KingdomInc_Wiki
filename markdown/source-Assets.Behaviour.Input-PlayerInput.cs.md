# PlayerInput — source reference

Assets.Behaviour.Input/PlayerInput.cs · 314 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 13 | public class PlayerInput : MonoBehaviour |
| 21 | public static PlayerInput Instance { get; private set; } |
| 23 | public static InputActionAsset Asset => _inputInstance.asset |
| 25 | public static IReadOnlyList<InputAction> RebindableKeys { get; private set; } |
| 27 | public static bool Enabled { get; private set; } |
| 29 | public static bool Delayed => Instance._inputDelay > 0 |
| 31 | public static Vector2Int MouseUI |
| 40 | public static Vector2Int MouseWorld => new Vector2Int(Mathf.RoundToInt(MouseWorld3.x), Mathf.RoundToInt(MouseWorld3.y)) |
| 42 | public static Vector3 MouseWorld3 { get; private set; } |
| 44 | public static Vector2 MouseWorld3Live => Camera.main.ScreenToWorldPoint(new Vector3(MouseUI.x, MouseUI.y)) |
| 46 | public static bool InteractPressed => Mouse.current.leftButton.wasPressedThisFrame |
| 48 | public static bool InteractReleased => Mouse.current.leftButton.wasReleasedThisFrame |
| 50 | public static bool CancelPressed => _inputInstance.UI.Cancel.WasPressedThisFrame() |
| 52 | public static string SearchKey => _inputInstance.UI.ToggleSearch.GetBindingDisplayString() |
| 54 | public static InputActions Controls => _inputInstance |
| 56 | public float TraverseDistance { get; private set; } |
| 239 | public void UpdateMouseWorld() |
| 266 | public void StopTraverse() |
| 291 | public static void Enable() |
| 300 | public static void Disable() |
| 309 | public static void Delay() |

## Documented by

| Wiki article |
| --- |
| [Controls and rebinding](controls.md) |

## Sources

- `Assets.Behaviour.Input/PlayerInput.cs:1`
