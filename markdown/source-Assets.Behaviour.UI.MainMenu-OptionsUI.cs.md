# OptionsUI — source reference

Assets.Behaviour.UI.MainMenu/OptionsUI.cs · 330 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 14 | public class OptionsUI : MonoBehaviour |
| 18 | public int Width |
| 20 | public int Height |
| 22 | public TMP_Dropdown.OptionData Option => new TMP_Dropdown.OptionData(Width + "x" + Height) |
| 24 | public OptionsResolution(Resolution res) |
| 30 | public OptionsResolution(int width, int height) |
| 36 | public override bool Equals(object obj) |
| 49 | public override int GetHashCode() |
| 54 | public bool IsCurrentResolution() |
| 104 | public static int DefaultFramerate => (int)Math.Round(Screen.currentResolution.refreshRateRatio.value) |
| 106 | public static int TargetFramerate => PlayerPrefs.GetInt("TargetFramerate", DefaultFramerate) |
| 108 | public static float UIScale |
| 120 | public static int AutosaveMinutes => PlayerPrefs.GetInt("AutosaveMinutes", 5) |
| 207 | public void ShowKeyBindings() |
| 219 | public void ApplyAndClose() |
| 248 | public void CancelOptions() |
| 260 | public void PreviewMusicVolume() |
| 265 | public void UpdateFpsDisplay() |
| 270 | public void UpdateAutosaveDisplay() |
| 280 | public void UpdateUIScaleDisplay() |
| 286 | public void UpdateUIScaleValue() |
| 305 | public static void UpdateGlobalOptions() |

## Documented by

| Wiki article |
| --- |
| [Options, display, audio, language, and accessibility](options-and-language.md) |

## Sources

- `Assets.Behaviour.UI.MainMenu/OptionsUI.cs:1`
