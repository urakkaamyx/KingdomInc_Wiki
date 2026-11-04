# MusicManager — source reference

Assets.Behaviour.Util/MusicManager.cs · 184 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class MusicManager : MonoBehaviour |
| 30 | public static bool IsPlaying => _instance._source.isPlaying |
| 32 | public static float Volume |
| 105 | public void PlayTrack(string trackName, float fadeTime, float quietTime) |
| 110 | public void PlayTrack(AudioClip track, float fadeTime, float quietTime) |
| 134 | public static void Play(string trackName, float fadeTime = -1f) |
| 142 | public static void Queue(string musicTrack, int prio) |
| 173 | public static void PreviewVolume(float vol) |

## Documented by

| Wiki article |
| --- |
| [Menus, save selection, music, and visual feedback](menus-saves-music-and-animation.md) |

## Sources

- `Assets.Behaviour.Util/MusicManager.cs:1`
