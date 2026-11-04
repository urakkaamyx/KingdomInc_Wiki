# UISounds — source reference

Assets.Behaviour.UI/UISounds.cs · 166 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 6 | public class UISounds : MonoBehaviour |
| 10 | public float Timeout |
| 13 | public const float DefaultVolume = 0.5f |
| 45 | public static UISounds Instance { get; private set; } |
| 47 | public static float Volume |
| 78 | public void PlaySound(AudioClip clip) |
| 83 | public void PlaySound(AudioClip clip, float volume, float pitchShift = 1.02f) |
| 124 | public static void CraftStep() |
| 129 | public static void CraftFinished(float volume = 1f) |
| 134 | public static void WindowOpen() |
| 139 | public static void WindowClose() |
| 144 | public static void Button() |
| 149 | public static void TurnPage(float volume = 1f) |
| 154 | public static void Coins(float volume = 1f) |
| 159 | public static void PreviewVolume(float vol) |

## Documented by

| Wiki article |
| --- |
| [Menus, save selection, music, and visual feedback](menus-saves-music-and-animation.md) |

## Sources

- `Assets.Behaviour.UI/UISounds.cs:1`
