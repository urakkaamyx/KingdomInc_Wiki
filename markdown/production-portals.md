# Portals and shared channels

Move arbitrary items between diagrams using Mana-funded storage lanes.

## Channel storage

Portals use a shared inventory indexed by eight channels and eight channel indices, giving 64 separate lanes. Each lane holds up to 20 items in FIFO order and can contain mixed item types.

A Portal is either an input terminal or an output terminal. Input accepts any item if its one-item buffer is free, then pays Mana to store it in the selected lane. Output requests and forwards the oldest item in that lane.

## Fees and overflow

The base input fee is 12 Mana per item, reduced to 6 by Portal Cost Reduce and to 3 by Portal Cost Reduce 2. The fee is charged once on entry; the output has no additional fee.

Portal Overflow gives an input a passthrough output. It forwards the waiting item only when the selected lane is full and the overflow output is connected and free. Running out of Mana does not by itself qualify for overflow.

## Waiting outputs and settings

Empty output terminals join a waiting queue. A newly stored item can be handed directly to the first queued output rather than remaining in the lane's list. Empty polling uses a 0.2-second timeout.

The terminal pauses while its settings popup is active. Changing between input and output clears the previous IO layout. Channel, channel index, direction, and last displayed item are saved.

## Sources

- `Assets.Source.Flow.Elements/Portal.cs:37`
- `Assets.Source.Flow.Elements/Portal.cs:80`
- `Assets.Source.Flow.Elements/Portal.cs:147`
- `Assets.Source.Items/PortalContents.cs:10`
- `Assets.Source.Items/PortalContents.cs:39`
- `Assets.Source.Items/PortalContents.cs:65`
