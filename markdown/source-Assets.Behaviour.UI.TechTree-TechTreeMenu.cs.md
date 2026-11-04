# TechTreeMenu — source reference

Assets.Behaviour.UI.TechTree/TechTreeMenu.cs · 256 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public class TechTreeMenu : MonoBehaviour |
| 50 | public static TechTreeMenu Instance { get; private set; } |
| 52 | public static bool Visible |
| 64 | public TechNode RootNode { get; private set; } |
| 66 | public IEnumerable<UITechNode> Nodes => _nodes.Values |
| 88 | public void UpdateTechListButton(bool newUnlock = false) |
| 111 | public void ToggleListView() |
| 117 | public void ShowTechTree(TechNode root, bool force = false) |
| 157 | public void FocusNode(TechNode node) |
| 213 | public bool ProcessEscape() |
| 230 | public bool ProcessCancel() |
| 245 | public void UpdateTechTree() |

## Documented by

| Wiki article |
| --- |
| [Research tree and list interface](research-interface.md) |

## Sources

- `Assets.Behaviour.UI.TechTree/TechTreeMenu.cs:1`
