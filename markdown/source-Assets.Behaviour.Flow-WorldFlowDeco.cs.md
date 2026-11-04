# WorldFlowDeco — source reference

Assets.Behaviour.Flow/WorldFlowDeco.cs · 347 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 14 | public class WorldFlowDeco : MonoBehaviour, IPointerEnterHandler, IEventSystemHandler, IPointerExitHandler, IPointerClickHandler |
| 39 | public FlowDeco Decoration |
| 44 | public WorldFlowDecoResizer PrimaryResizer { get; private set; } |
| 47 | public FlowCollider Collider { get; private set; } |
| 49 | public bool ToolsLocked { get; private set; } |
| 51 | public Color ToolColor |
| 63 | public Vector2Int Position => Decoration.Position |
| 65 | public Vector2Int Size => Decoration.Size |
| 67 | public bool OpenBuyAfterResize { get; set; } |
| 78 | public void SetDeco(FlowDeco deco) |
| 88 | public void UpdatePosition(Vector2Int pos) |
| 97 | public void UpdateSize(Vector2Int pos, Vector2Int size) |
| 113 | public void UpdateStyle() |
| 146 | public void UpdateLabel() |
| 155 | public void UpdateZoom(int zoom) |
| 174 | public void OnPointerEnter(PointerEventData eventData) |
| 183 | public void OnPointerExit(PointerEventData eventData) |
| 189 | public void OnPointerClick(PointerEventData eventData) |
| 197 | public void StartPicker() |
| 223 | public void SetToolOpacity(float alpha) |
| 251 | public void LockTools(Image locker) |
| 258 | public void UnlockTools() |
| 271 | public void DelayOpenBuyMenu() |
| 282 | public void OpenOptionsPopup() |
| 296 | public (List<WorldFlowElement> elements, List<WorldFlowDeco> decos, List<WorldFlowPipeNode> pipeNodes) GetAnchoredParts(bool includeContainers = false) |
| 332 | public static void UpdateZoomLevel(int zoom) |

## Documented by

| Wiki article |
| --- |
| [Container anchors, resizing, and group movement](container-moving-and-resizing.md) |

## Sources

- `Assets.Behaviour.Flow/WorldFlowDeco.cs:1`
