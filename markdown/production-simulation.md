# Production simulation and bottlenecks

How diagrams, pipes, queues, and blocked outputs determine actual throughput.

## Simulation order

The production manager advances the player with Unity's frame delta. Every saved flow diagram is updated, so changing the displayed diagram does not suspend the others. Within each diagram, all buildings update in list order and then all pipes update in list order.

This is a frame-driven simulation, not a universal once-per-second production tick. Buildings implement their own timers. A nominal items-per-second rate can be limited by frame updates because many building Update methods finish at most one operation per call.

## Pipes and buffers

Pipes repeatedly transfer the first available output item while the receiving input accepts its type and has buffer space. There is no pipe travel-time or pipe-length penalty in the transfer method. Items remain individual inventory objects with their quality, equipment, and character data.

An input's acceptance filter and its capacity are separate checks. An unacceptable first item marks the pipe as rejected and blocks the queue behind it. A full but otherwise compatible destination simply stalls transfer. Most utility inputs and outputs hold one item; resource outputs normally hold five; recipe inputs hold exactly that reagent's required count.

## Diagnosing a stopped chain

Check the destination's item filter, its input capacity, all output capacities of a multi-output recipe, the building's currency cost, automatic worker, and any shared resource quota or war gate. A craft can wait with its ingredients already consumed until every required output has room.

Recipe completion checks whether each output has at least one free place, then adds the entire result batch. A large batch may therefore exceed its nominal buffer size. These are queue limits, not an item stack system.

## Sources

- `Assets.Behaviour.Flow/WorldFlowManager.cs:129`
- `Assets.Source.Player/GamePlayer.cs:141`
- `Assets.Source.Flow/FlowDiagram.cs:29`
- `Assets.Source.Flow/FlowPipe.cs:21`
- `Assets.Source.Flow/FlowIO.cs:32`
- `Assets.Source.Flow.Elements/RecipeElement.cs:202`
