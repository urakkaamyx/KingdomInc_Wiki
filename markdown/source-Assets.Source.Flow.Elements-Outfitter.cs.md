# Outfitter — source reference

Assets.Source.Flow.Elements/Outfitter.cs · 186 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public class Outfitter : FlowElement |
| 15 | public bool Queued |
| 17 | public float Timeout |
| 21 | public InventoryItem CurrentHuman |
| 23 | public InventoryItem CurrentEquip |
| 25 | public override string Label => "@outfitter" |
| 27 | public override ElementCategory Category => ElementCategory.Utility |
| 29 | public override string IconName => "Icons_62" |
| 31 | public override bool HasCraftButton => false |
| 33 | public bool Automated { get; private set; } |
| 35 | public Outfitter() |
| 64 | public override void Start() |
| 72 | public void CheckAutomated() |
| 97 | public override void Update(float delta) |
| 156 | protected override void CopySettingsTo(FlowElement copy) |
| 161 | protected override void DataToJson(JsonObject data) |
| 174 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Outfitter](building-Outfitter.md) |
| [Outfitters and equipment automation](production-outfitters.md) |

## Sources

- `Assets.Source.Flow.Elements/Outfitter.cs:1`
