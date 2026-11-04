# WorldFlowCamera — source reference

Assets.Behaviour.Flow/WorldFlowCamera.cs · 169 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 10 | public class WorldFlowCamera : MonoBehaviour |
| 38 | public static WorldFlowCamera Instance { get; private set; } |
| 40 | public int MaxZoom |
| 52 | public int ZoomLevel { get; private set; } |
| 54 | public float ZoomScale => GetZoomScale(ZoomLevel) |
| 56 | public float TextScale => ZoomScale / 2f |
| 86 | public void ChangeZoomLevel(int diff) |
| 102 | public void SetZoomLevel(int lv) |
| 126 | public static float GetZoomScale(int lv) |
| 139 | public void Move(float dX, float dY) |
| 144 | public void RecalculateBounds() |

## Documented by

| Wiki article |
| --- |
| [Map navigation and dragging](map-navigation-and-dragging.md) |

## Sources

- `Assets.Behaviour.Flow/WorldFlowCamera.cs:1`
