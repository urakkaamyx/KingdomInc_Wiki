# Armory — source reference

Assets.Source.Flow.Elements/Armory.cs · 248 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 12 | public class Armory : FlowElement |
| 20 | public ItemType OutputType |
| 22 | public InventoryItem LastItem |
| 24 | public int Channel |
| 28 | public override string Label => "@armory" |
| 30 | public override ElementCategory Category => ElementCategory.Utility |
| 32 | public override Sprite Icon => ArmoryType?.GetIcon() ?? base.Icon |
| 34 | public override string IconName => "Icons_138" |
| 36 | public override bool HasCraftButton => false |
| 38 | public virtual int BaseInputCost => 100 |
| 40 | public int InputCost |
| 52 | public virtual int MaxItems => 10 |
| 54 | public ItemType ArmoryType |
| 72 | public List<Armory> ArmoryList => GamePlayer.Current.GetArmoryList(Channel, ArmoryType) |
| 74 | public Color ChannelColor => ArmoryContents.ChannelColor[Channel] |
| 76 | public virtual TechNode CostTech => _costTech |
| 78 | public virtual TechNode ChannelTech => _channelTech |
| 80 | public virtual string TooltipDescription => "@ArmoryTTDesc" |
| 82 | public Armory() |
| 90 | public override void OnCreateElement() |
| 98 | public override bool HandleReopenBuyMenu() |
| 104 | public InventoryItem PeekItem() |
| 109 | public virtual bool CanAcceptItem(ItemType i) |
| 122 | public override void Update(float delta) |
| 164 | protected override void CopySettingsTo(FlowElement copy) |
| 171 | public void SetOutputType(ItemType type) |
| 219 | protected override void DataToJson(JsonObject data) |
| 232 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Armory](building-Armory.md) |
| [Armories and shared item storage](production-global-storage.md) |

## Sources

- `Assets.Source.Flow.Elements/Armory.cs:1`
