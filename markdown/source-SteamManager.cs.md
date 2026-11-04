# SteamManager — source reference

SteamManager.cs · 123 lines · infrastructure

## Audit classification

Bundled infrastructure / metadata. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public class SteamManager : MonoBehaviour |
| 10 | protected static bool s_EverInitialized |
| 12 | protected static SteamManager s_instance |
| 14 | protected bool m_bInitialized |
| 16 | protected SteamAPIWarningMessageHook_t m_SteamAPIWarningMessageHook |
| 18 | protected static SteamManager Instance |
| 30 | public static bool Initialized => Instance.m_bInitialized |
| 33 | protected static void SteamAPIDebugTextHook(int nSeverity, StringBuilder pchDebugText) |
| 45 | protected virtual void Awake() |
| 91 | protected virtual void OnEnable() |
| 104 | protected virtual void OnDestroy() |
| 116 | protected virtual void Update() |

## Documented by

| Wiki article |
| --- |
| [Achievements, Steam statistics, and integration](achievements-and-steam.md) |

## Sources

- `SteamManager.cs:1`
