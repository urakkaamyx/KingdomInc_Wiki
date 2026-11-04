# TrackSwitch — source reference

Assets.Source.Flow.Elements/TrackSwitch.cs · 88 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class TrackSwitch : FlowElement |
| 9 | public bool SwitchPosition |
| 11 | public override string Label => "@track_switch" |
| 13 | public override ElementCategory Category => ElementCategory.Utility |
| 15 | public override string IconName => "Icons_73" |
| 17 | public override bool HasCraftButton => false |
| 19 | public TrackSwitch() |
| 38 | public void UpdateTrackSwitch() |
| 54 | public override void Update(float delta) |
| 74 | protected override void CopySettingsTo(FlowElement copy) |
| 79 | protected override void DataToJson(JsonObject data) |
| 84 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Switch](building-TrackSwitch.md) |
| [Track switches, timers, and release buttons](production-gates.md) |

## Sources

- `Assets.Source.Flow.Elements/TrackSwitch.cs:1`
