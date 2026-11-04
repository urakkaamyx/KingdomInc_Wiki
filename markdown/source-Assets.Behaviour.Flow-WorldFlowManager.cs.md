# WorldFlowManager — source reference

Assets.Behaviour.Flow/WorldFlowManager.cs · 607 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 17 | public class WorldFlowManager : MonoBehaviour |
| 19 | public const int GridSize = 64 |
| 90 | public static WorldFlowManager Instance { get; private set; } |
| 92 | public static bool Visible |
| 104 | public IEnumerable<WorldFlowElement> Elements => _elements |
| 106 | public bool BlueprintActive => _currentGhost |
| 108 | public WorldFlowGhost BlueprintPrefab => _ghostPrefab |
| 110 | public FlowDiagram CurrentFlow => GamePlayer.Current.ActiveFlow |
| 157 | public void SetupFlow(int idx) |
| 177 | public void SwapFlowIndex(int swap1, int swap2) |
| 187 | public void ShowFlow(int idx) |
| 233 | public void CycleFlow(int cycle) |
| 284 | public WorldFlowDeco ShowDeco(FlowDeco deco) |
| 329 | public void CreateNewPipe(FlowPipe pipe) |
| 335 | public void CreateNewElement(FlowElement el) |
| 349 | public WorldFlowDeco CreateNewDeco(FlowDeco deco) |
| 355 | public void DisconnectPipe(FlowPipe pipe, FlowDiagram inFlow = null) |
| 364 | public void RemoveElement(FlowElement element) |
| 376 | public void RemoveDecoration(WorldFlowDeco deco) |
| 382 | public void MoveToFlow(WorldFlowDeco deco, int moveFrom, int moveTo, bool temporary = false) |
| 401 | public void MoveToFlow(WorldFlowElement element, int moveFrom, int moveTo) |
| 408 | public void MoveToFlow(WorldFlowPipe pipe, int moveFrom, int moveTo) |
| 419 | public void MoveToFlow(WorldFlowPipeNode pipe, int moveFrom, int moveTo) |
| 424 | public WorldFlowPipe CreateGhostPipe(WorldFlowIO start, List<Vector2Int> nodes) |
| 444 | public void ClearPipeGhost() |
| 453 | public WorldFlowPipeNode CreatePipeNode(WorldFlowPipe pipe, int idx, Vector2Int pos) |
| 461 | public WorldFlowGhost ShowPurchaseBlueprint(FlowElement element, bool hold) |
| 476 | public WorldFlowGhost CreatePurchaseBlueprint(FlowElement element, bool preview) |
| 487 | public WorldFlowGhost ShowDecoBlueprint(FlowDeco deco, bool isClone, bool hold) |
| 499 | public void UpdateCostDisplay(CurrencyCollection cost) |
| 510 | public void StopBlueprintMode() |
| 523 | public void ShowIncome(Vector2 worldPos, Currency c, long amt) |
| 537 | public TMP_Text ShowFloatingIconText(Vector2 worldPos, Sprite icon, string text) |
| 554 | public static Vector2Int ClampToGrid(Vector2Int pos, int addedYOffset = 0) |
| 559 | public void ToggleFlow(bool toggleTo) |
| 564 | public void UpdateFlowElements<T>() where T : FlowElement |
| 579 | public void UpdateFlowElements(string nodeType) |
| 594 | public void ShowElement(FlowElement element) |

## Documented by

| Wiki article |
| --- |
| [Production simulation and bottlenecks](production-simulation.md) |
| [Saves, autosaves, pause, and offline behavior](saves-time-and-offline.md) |

## Sources

- `Assets.Behaviour.Flow/WorldFlowManager.cs:1`
