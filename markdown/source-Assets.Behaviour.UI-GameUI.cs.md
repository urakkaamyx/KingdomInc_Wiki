# GameUI — source reference

Assets.Behaviour.UI/GameUI.cs · 1,025 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 40 | public class GameUI : MonoBehaviour |
| 152 | public static GameUI Instance { get; private set; } |
| 154 | public static bool MenuVisible => Instance._ingameMenuContent.gameObject.activeSelf |
| 157 | public SelectResourcePopup ResourcePopup { get; private set; } |
| 160 | public SelectRecipePopup RecipePopup { get; private set; } |
| 163 | public DecoOptionsPopup DecoPopup { get; private set; } |
| 166 | public StickerOptionsPopup StickerPopup { get; private set; } |
| 169 | public FlowOptionsPopup FlowPopup { get; private set; } |
| 172 | public SelectReqContractPopup RequisitionPopup { get; private set; } |
| 175 | public SelectWarEffortPopup WarEffortPopup { get; private set; } |
| 178 | public SelectForestResourcePopup ForestResourcePopup { get; private set; } |
| 181 | public HumanDetailsPopup CharacterPopup { get; private set; } |
| 184 | public QuestBoardPopup QuestPopup { get; private set; } |
| 187 | public ArmoryPopup ArmoryPopup { get; private set; } |
| 190 | public PortalPopup PortalPopup { get; private set; } |
| 193 | public ItemFilterPopup FilterPopup { get; private set; } |
| 196 | public ItemAppraiserPopup AppraiserPopup { get; private set; } |
| 199 | public AccountantPopup AccountantPopup { get; private set; } |
| 202 | public SelectDungeonPopup DungeonPopup { get; private set; } |
| 205 | public CurrencyExchangePopup CurrencyExchangePopup { get; private set; } |
| 208 | public VictoryPopup VictoryPopup { get; private set; } |
| 211 | public GameObject PipeNodeHint { get; private set; } |
| 214 | public GameObject PlacementHint { get; private set; } |
| 217 | public GameObject DeconstructHint { get; private set; } |
| 293 | public void UpdateMouseHover() |
| 316 | public void UpdateUIScale() |
| 329 | public void ToggleBuyMenu() |
| 334 | public void ToggleBuyMenu(bool toggleTo) |
| 344 | public void ToggleItemMenu() |
| 349 | public void ToggleItemMenu(bool toggleTo) |
| 362 | public void ToggleDeconstructMode() |
| 367 | public void ToggleDeconstructMode(bool toggleTo) |
| 416 | public void ToggleTechMenu() |
| 429 | public void ToggleTechMenu(bool toggleTo) |
| 440 | public void ToggleDecoMenu() |
| 445 | public void ToggleDecoMenu(bool toggleTo) |
| 458 | public void ToggleMap() |
| 481 | public void ToggleResourceMenu() |
| 486 | public void ToggleResourceMenu(bool toggleTo) |
| 499 | public void ToggleWarEffortMenu() |
| 504 | public void ToggleWarEffortMenu(WarType war) |
| 510 | public void ToggleWarEffortMenu(bool toggleTo) |
| 523 | public void ToggleForestCrewMenu() |
| 528 | public void ToggleForestCrewMenu(bool toggleTo) |
| 541 | public void ToggleFarmMenu() |
| 546 | public void ToggleFarmMenu(bool toggleTo) |
| 559 | public void ToggleDungeonMenu(DungeonType dungeon) |
| 565 | public void ToggleDungeonMenu(DungeonProgress progress) |
| 571 | public void ToggleDungeonMenu() |
| 576 | public void ToggleDungeonMenu(bool toggleTo) |
| 589 | public void ToggleCloneMode() |
| 594 | public void ToggleCloneMode(bool toggleTo) |
| 609 | public void ToggleCloneBorder(bool toggleTo) |
| 614 | public void ToggleAreaMove() |
| 619 | public void ToggleAreaMove(bool toggleTo) |
| 634 | public void ToggleMoveBorder(bool toggleTo) |
| 639 | public void ShowCharacterDetails(HumanItemData item, Action onClose = null) |
| 645 | public void CloseAllExcept(GameUIType? type) |
| 714 | public bool IsActive(GameUIType type) |
| 736 | public void TogglePopupMenu(UIPopupMenu popup) |
| 741 | public void TogglePopupMenu(UIPopupMenu popup, bool toggleTo, bool playSound = true) |
| 773 | public void KeyboardPicker() |
| 797 | public void InsufficientFundsWarning() |
| 802 | public TMP_Text ShowWarning(Vector2 position, string text) |
| 825 | public void ProcessCancel() |
| 840 | public void ProcessEscape() |
| 896 | public void ToggleUI(bool? toggleTo = null) |
| 905 | public void UpdateBuildBarButtons() |
| 925 | public void UpdateResourcesButton() |
| 944 | public void UpdateWarEffortButton() |
| 949 | public void UpdateForestCrewButton() |
| 954 | public void UpdateFarmButton() |
| 959 | public void UpdateDungeonButton() |
| 964 | public void UpdateFlowMenu(bool isNew = false) |
| 978 | public void ToggleSearch() |
| 1006 | public void DoHotkey(int key) |
| 1016 | public void FillMenu(RectTransform parent, int curr, int max, float height) |

## Documented by

| Wiki article |
| --- |
| [Controls and rebinding](controls.md) |
| [Saves, autosaves, pause, and offline behavior](saves-time-and-offline.md) |

## Sources

- `Assets.Behaviour.UI/GameUI.cs:1`
