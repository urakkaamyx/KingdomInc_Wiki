# Options, display, audio, language, and accessibility

Exposed settings and how they are stored.

## Available options

| Option | Implementation |
| --- | --- |
| Resolution | Deduplicated modes at least 1280×720; unmatched current mode shown as Custom |
| Window mode | Windowed or FullScreenWindow |
| Framerate | Saved target; default rounds display refresh-rate ratio |
| VSync | On without explicit target or when target is within 5 FPS of refresh, otherwise off |
| Music/sound | Separate controls with previews |
| Autosave | Whole minutes; default 5; zero disables timed autosaves |
| UI scale | Slider/4; default 1.0 |
| Bindings | Selected actions can be rebound/reset |
| Language | PlayerPrefs Locale; resource and language.ini handling |

## Scale limits

Maximum scale is 1.0 below 1080 pixels high, 1.25 below 1440, 1.75 below 2160, and 2.5 at 2160 or above. Scale changes refresh font filtering and main/game/prestige canvases. The slider can commit on mouse release, so Cancel does not necessarily undo an already applied live scale change.

## Language loading

Resources/Language TextAssets define locales. en-US is the fallback. A language.ini file in the process working directory overrides locale selection. Otherwise saved Locale is used; without one, the current culture is used only if exactly available, else en-US. Missing translations fall back to English, then show @key and log a warning.

Key=value text skips semicolon comments. A value beginning with @ aliases an already-read key. Applying locale changes current thread culture and UI culture.

## Accessibility evidence

OptionsUI provides scale, rebinding, resolution and independent volumes. It does not expose dedicated colorblind, screen-reader, subtitle, or reduced-motion switches. That describes this options class, not a platform-wide accessibility certification.

## Persistence

Unity PlayerPrefs store options separately from kingdom saves. Apply stores framerate/autosave settings and volume values, and updates global options. Different saves do not select separate options profiles.

## Sources

- `Assets.Behaviour.UI.MainMenu/OptionsUI.cs:104`
- `Assets.Behaviour.UI.MainMenu/OptionsUI.cs:181`
- `Assets.Behaviour.UI.MainMenu/OptionsUI.cs:219`
- `Assets.Behaviour.UI.MainMenu/OptionsUI.cs:286`
- `Assets.Behaviour.UI.MainMenu/OptionsUI.cs:305`
- `Assets.Source.Util/Translation.cs:84`
- `Assets.Source.Util/Translation.cs:133`
