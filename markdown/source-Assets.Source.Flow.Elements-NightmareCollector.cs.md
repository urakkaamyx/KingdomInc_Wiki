# NightmareCollector — source reference

Assets.Source.Flow.Elements/NightmareCollector.cs · 56 lines · 3 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class NightmareCollector : FlowElement |
| 9 | public override string Label => "@nightmare_distiller" |
| 11 | public override string IconName => "Icons3_92" |
| 13 | public override string MusicTrack => "Icicles LOOP BPM110" |
| 15 | public override ElementCategory Category => ElementCategory.Consumption |
| 17 | public override bool HasCraftButton => false |
| 19 | public float ProgressPerCollector => 1f / Mathf.Floor(Mathf.Sqrt(GamePlayer.Current.NightmareCount)) |
| 21 | public NightmareCollector() |
| 35 | public override void Update(float delta) |
| 49 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |
| 53 | protected override void DataToJson(JsonObject data) |

## Documented by

| Wiki article |
| --- |
| [Nightmare Distiller](building-NightmareCollector.md) |
| [Nightmares and the endgame loop](nightmare-loop.md) |
| [Incineration and nightmare distillation](production-disposal-nightmare.md) |

## Sources

- `Assets.Source.Flow.Elements/NightmareCollector.cs:1`
