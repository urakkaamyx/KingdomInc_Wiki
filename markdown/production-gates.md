# Track switches, timers, and release buttons

Control when individual items enter a chain.

## Track Switch

With SwitchPosition true, Track Switch passes its waiting item to the first output when there is room. With the switch false, it stops the item unless Track Switch 2 has added a second output and that second output is connected and free.

A full selected route causes a stall; the node does not automatically use the other route. Switch position is copied and saved.

## Timer

Timer starts with a two-second interval and a two-second countdown. It counts down even when no item is present. Once the countdown has expired and its output is free, it forwards one waiting item and resets the countdown.

It therefore enforces spacing between successful releases rather than imposing a fresh delay starting at each arrival. An item arriving after a long idle can pass immediately. Timer processing does not use Speed or Worker.

The timer settings popup is gated by Outfitter Timeout technology. Its slider sets MaxTime and resets TimeLeft to the same value.

## Single Button

Single Button spends one queued click only when it successfully transfers an input item to its output. Clicking can queue up to ten releases through the interface. Unused clicks persist when no input is available or output is blocked.

## Sources

- `Assets.Source.Flow.Elements/TrackSwitch.cs:38`
- `Assets.Source.Flow.Elements/TrackSwitch.cs:54`
- `Assets.Source.Flow.Elements/Timer.cs:9`
- `Assets.Source.Flow.Elements/Timer.cs:39`
- `Assets.Behaviour.Flow.Elements/WorldFlowTimer.cs:63`
- `Assets.Source.Flow.Elements/SingleButton.cs:37`
- `Assets.Behaviour.Flow.Elements/WorldFlowSingleButton.cs:96`
