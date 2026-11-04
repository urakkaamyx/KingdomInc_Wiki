# InputActions — source reference

Assets.Behaviour.Input/InputActions.cs · 659 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 10 | public class InputActions : IInputActionCollection2, IInputActionCollection, IEnumerable<InputAction>, IEnumerable, IDisposable |
| 12 | public struct PlayerActions(InputActions wrapper) |
| 16 | public bool enabled => Get().enabled |
| 18 | public InputActionMap Get() |
| 23 | public void Enable() |
| 28 | public void Disable() |
| 33 | public static implicit operator InputActionMap(PlayerActions set) |
| 38 | public void AddCallbacks(IPlayerActions instance) |
| 50 | public void RemoveCallbacks(IPlayerActions instance) |
| 58 | public void SetCallbacks(IPlayerActions instance) |
| 69 | public struct UIActions(InputActions wrapper) |
| 73 | public InputAction Interact => m_Wrapper.m_UI_Interact |
| 75 | public InputAction Cancel => m_Wrapper.m_UI_Cancel |
| 77 | public InputAction TraverseMap => m_Wrapper.m_UI_TraverseMap |
| 79 | public InputAction TraverseHold => m_Wrapper.m_UI_TraverseHold |
| 81 | public InputAction Zoom => m_Wrapper.m_UI_Zoom |
| 83 | public InputAction TogglePurchaseMenu => m_Wrapper.m_UI_TogglePurchaseMenu |
| 85 | public InputAction ToggleItemMenu => m_Wrapper.m_UI_ToggleItemMenu |
| 87 | public InputAction ToggleDeconstruct => m_Wrapper.m_UI_ToggleDeconstruct |
| 89 | public InputAction ToggleTech => m_Wrapper.m_UI_ToggleTech |
| 91 | public InputAction ToggleDeco => m_Wrapper.m_UI_ToggleDeco |
| 93 | public InputAction ToggleMap => m_Wrapper.m_UI_ToggleMap |
| 95 | public InputAction ToggleResources => m_Wrapper.m_UI_ToggleResources |
| 97 | public InputAction Escape => m_Wrapper.m_UI_Escape |
| 99 | public InputAction Picker => m_Wrapper.m_UI_Picker |
| 101 | public InputAction Clone => m_Wrapper.m_UI_Clone |
| 103 | public InputAction ToggleUI => m_Wrapper.m_UI_ToggleUI |
| 105 | public InputAction AreaMove => m_Wrapper.m_UI_AreaMove |
| 107 | public InputAction ToggleSearch => m_Wrapper.m_UI_ToggleSearch |
| 109 | public InputAction Hotkey1 => m_Wrapper.m_UI_Hotkey1 |
| 111 | public InputAction Hotkey2 => m_Wrapper.m_UI_Hotkey2 |
| 113 | public InputAction Hotkey3 => m_Wrapper.m_UI_Hotkey3 |
| 115 | public InputAction Hotkey4 => m_Wrapper.m_UI_Hotkey4 |
| 117 | public InputAction Hotkey5 => m_Wrapper.m_UI_Hotkey5 |
| 119 | public InputAction Hotkey6 => m_Wrapper.m_UI_Hotkey6 |
| 121 | public InputAction Hotkey7 => m_Wrapper.m_UI_Hotkey7 |
| 123 | public InputAction Hotkey8 => m_Wrapper.m_UI_Hotkey8 |
| 125 | public InputAction Hotkey9 => m_Wrapper.m_UI_Hotkey9 |
| 127 | public InputAction Hotkey0 => m_Wrapper.m_UI_Hotkey0 |
| 129 | public bool enabled => Get().enabled |
| 131 | public InputActionMap Get() |
| 136 | public void Enable() |
| 141 | public void Disable() |
| 146 | public static implicit operator InputActionMap(UIActions set) |
| 151 | public void AddCallbacks(IUIActions instance) |
| 331 | public void RemoveCallbacks(IUIActions instance) |
| 339 | public void SetCallbacks(IUIActions instance) |
| 350 | public interface IPlayerActions |
| 354 | public interface IUIActions |
| 487 | public InputActionAsset asset { get; } |
| 489 | public InputBinding? bindingMask |
| 501 | public ReadOnlyArray<InputDevice>? devices |
| 513 | public ReadOnlyArray<InputControlScheme> controlSchemes => asset.controlSchemes |
| 515 | public IEnumerable<InputBinding> bindings => asset.bindings |
| 517 | public PlayerActions Player => new PlayerActions(this) |
| 519 | public UIActions UI => new UIActions(this) |
| 521 | public InputControlScheme KeyboardMouseScheme |
| 533 | public InputControlScheme GamepadScheme |
| 545 | public InputControlScheme TouchScheme |
| 557 | public InputControlScheme JoystickScheme |
| 569 | public InputControlScheme XRScheme |
| 581 | public InputActions() |
| 620 | public void Dispose() |
| 625 | public bool Contains(InputAction action) |
| 630 | public IEnumerator<InputAction> GetEnumerator() |
| 640 | public void Enable() |
| 645 | public void Disable() |
| 650 | public InputAction FindAction(string actionNameOrId, bool throwIfNotFound = false) |
| 655 | public int FindBinding(InputBinding bindingMask, out InputAction action) |

## Documented by

| Wiki article |
| --- |
| [Controls and rebinding](controls.md) |

## Sources

- `Assets.Behaviour.Input/InputActions.cs:1`
