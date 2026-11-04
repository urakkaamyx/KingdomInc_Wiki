# UITooltip — source reference

Behaviour.UI/UITooltip.cs · 302 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 17 | public class UITooltip : MonoBehaviour |
| 19 | public static bool TooltipEnabled = true |
| 21 | public static Color SeparatorColor = new Color(0.415f, 0.415f, 0.415f) |
| 53 | public static bool Active |
| 65 | public static RectTransform tooltipParent { get; private set; } |
| 67 | public TooltipSource Source { get; protected set; } |
| 69 | public RectTransform Content => _contentParent |
| 71 | public virtual UITooltip Prefab => UITooltipParent.TooltipPrefab |
| 73 | public virtual float SizeX => ((RectTransform)transform).sizeDelta.x |
| 75 | public virtual float SizeY => ((RectTransform)transform).sizeDelta.y |
| 82 | public static void SetupTooltipContext(RectTransform parent) |
| 87 | public UITooltipText AddTextLine(string text, int size = 12, float margin = 8f) |
| 95 | public (UITooltipText label, UITooltipText level) AddHeader(string name, int level, int maxLevel = 0, int size = 12, float margin = 8f) |
| 117 | public UITooltipLine AddSeparator(Color c, float thickness, float spacingTop, float spacingBottom) |
| 129 | public UITooltipLine AddSeparator() |
| 134 | public UITooltipSpacer AddMinHeightSpacer(float minHeight) |
| 142 | public (UITooltipText Label, UITooltipCost Cost) AddCostLine(CurrencyCollection cost, string label = "@CostLabel", bool sep = true) |
| 162 | public UITooltipValue AddValueLine(CurrencyCollection value, string label = "@SellValue") |
| 170 | public void AddItemLine(InventoryItem item, int count, string nameOverride = null) |
| 177 | public void AddIconLine(Sprite icon, string text, Color c) |
| 184 | public void AddProgressBarLine(string label, Func<Color> barColor, Func<float> progressSource, Func<string> textSource) |
| 193 | public void AddContent(UITooltipContent content) |
| 198 | public virtual void SetContent(TooltipSource tt) |
| 230 | public virtual void RefreshContent() |
| 237 | protected virtual void Update() |
| 259 | public static void Show(TooltipSource tt, UITooltip prefab) |
| 275 | public static void Refresh() |
| 287 | public static void Refresh(TooltipSource tt) |
| 295 | public static void Hide(TooltipSource tt) |

## Documented by

| Wiki article |
| --- |
| [Tooltips, warnings, notifications, and tutorial cues](tooltips-warnings-and-tutorial.md) |

## Sources

- `Behaviour.UI/UITooltip.cs:1`
