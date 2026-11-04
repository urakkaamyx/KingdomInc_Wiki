# Portal — source reference

Assets.Source.Flow.Elements/Portal.cs · 232 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public class Portal : FlowElement |
| 19 | public int Channel |
| 21 | public int ChannelIndex |
| 23 | public bool IsOutput |
| 27 | public override string Label => "@portal" |
| 29 | public override ElementCategory Category => ElementCategory.Utility |
| 31 | public override string IconName => "Icons_183" |
| 33 | public override bool HasCraftButton => false |
| 35 | public override Sprite Icon => LastItem?.Icon ?? base.Icon |
| 37 | public virtual int InputCost |
| 53 | public List<Portal> PortalList => GamePlayer.Current.GetPortalList(Channel, ChannelIndex) |
| 55 | public Color ChannelColor => ArmoryContents.ChannelColor[Channel] |
| 57 | public InventoryItem LastItem { get; private set; } |
| 59 | public Portal() |
| 80 | public override void Update(float delta) |
| 133 | protected override void CopySettingsTo(FlowElement copy) |
| 141 | public override bool HandleReopenBuyMenu() |
| 147 | public void SetOutput(bool output) |
| 198 | public void ClearOutput() |
| 211 | protected override void DataToJson(JsonObject data) |
| 222 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Portal](building-Portal.md) |
| [Portals and shared channels](production-portals.md) |

## Sources

- `Assets.Source.Flow.Elements/Portal.cs:1`
