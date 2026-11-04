# TutorialUI — source reference

Assets.Behaviour.UI/TutorialUI.cs · 258 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 14 | public class TutorialUI : MonoBehaviour |
| 16 | public CanvasGroup NewGameContent |
| 18 | public GameObject BuildArrow |
| 20 | public GameObject TechArrow |
| 22 | public GameObject BlueprintGhost |
| 24 | public GameObject IOArrowPrefab |
| 47 | public static bool Active => Instance?.enabled ?? false |
| 49 | public static bool NewGameBlackout => Instance.NewGameContent.transform.parent.gameObject.activeSelf |
| 51 | public static TutorialUI Instance { get; private set; } |
| 78 | public void HideNewGameOverlay() |
| 86 | public void ShowBuildArrow() |
| 91 | public void ShowMineArrow() |
| 99 | public void ShowUpgradeArrow() |
| 121 | public void ShowOutputArrow(FlowElement element) |
| 139 | public void ShowInputArrow() |
| 164 | public void ShowTechArrow() |
| 169 | public void ShowShopArrow() |
| 196 | public void FinishTutorial() |
| 201 | public void ShowBlueprint(bool show) |
| 222 | public void ShowResourcesArrow(bool show) |
| 227 | public void ShowWarEffortArrow(bool show) |
| 232 | public void ShowForestArrow(bool show) |
| 237 | public void ShowFarmArrow(bool show) |
| 242 | public void ShowDecoArrow(bool show) |
| 247 | public void ShowNodeAdded(FlowElement nodeType) |

## Documented by

| Wiki article |
| --- |
| [Tooltips, warnings, notifications, and tutorial cues](tooltips-warnings-and-tutorial.md) |

## Sources

- `Assets.Behaviour.UI/TutorialUI.cs:1`
