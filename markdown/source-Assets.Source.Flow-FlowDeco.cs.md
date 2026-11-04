# FlowDeco — source reference

Assets.Source.Flow/FlowDeco.cs · 175 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 10 | public class FlowDeco : IJsonSource |
| 12 | public Vector2Int Position |
| 14 | public Vector2Int Size |
| 16 | public int StyleIndex |
| 18 | public DecoSticker Sticker |
| 20 | public string Label |
| 22 | public bool Locked |
| 24 | public bool IsParent |
| 26 | public WorldFlowDeco World |
| 28 | public bool IsContainer |
| 40 | public bool IsNewContainer |
| 52 | public CurrencyCollection GetCopyCost(bool withAnchored) |
| 71 | public FlowDeco CreateCopy() |
| 83 | public CurrencyCollection GetRefund(bool withAnchored) |
| 93 | public CurrencyCollection GetRefund(IEnumerable<WorldFlowElement> anchored) |
| 117 | public virtual JsonValue ToJson() |
| 143 | public static FlowDeco FromJson(JsonValue json, FlowDiagram returned) |
| 161 | public static CurrencyCollection GetContainerCost() |
| 166 | public static CurrencyCollection GetLabelCost() |
| 171 | public static CurrencyCollection GetStickerCost() |

## Documented by

| Wiki article |
| --- |
| [Deconstruction and refunds](deconstruction-and-refunds.md) |
| [Decorations, labels, colors, and stickers](decoration-labels-stickers.md) |

## Sources

- `Assets.Source.Flow/FlowDeco.cs:1`
