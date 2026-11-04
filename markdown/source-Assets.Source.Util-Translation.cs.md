# Translation — source reference

Assets.Source.Util/Translation.cs · 193 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 10 | public class Translation |
| 12 | public const string DefaultLanguage = "en-US" |
| 14 | public const bool TestMode = false |
| 28 | public static Color HighlightColor = new Color32(byte.MaxValue, 209, 0, byte.MaxValue) |
| 34 | public static Translation Current => _current |
| 36 | public static string CurrentLocale => _current.Locale |
| 38 | public static IEnumerable<Translation> All => _languages.Values |
| 40 | public string Locale { get; private set; } |
| 42 | public string DisplayName { get; private set; } |
| 44 | public Translation(TextReader reader) |
| 71 | public string Get(string key) |
| 77 | public void Apply() |
| 84 | public static void Init() |
| 121 | public static void Clear() |
| 127 | public static void UpdateLocale(Translation locale) |
| 133 | public static string TranslateOnly(string text, params object[] values) |
| 179 | public static string Translate(string text, params object[] values) |
| 184 | public static string Highlight(string text, Color c, params object[] values) |
| 189 | public static string Plural(string v, int count) |

## Documented by

| Wiki article |
| --- |
| [Options, display, audio, language, and accessibility](options-and-language.md) |

## Sources

- `Assets.Source.Util/Translation.cs:1`
