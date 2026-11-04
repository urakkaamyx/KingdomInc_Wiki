# Deconstruction and refunds

Remove machines, decoration groups, pipes, and waypoints.

## Pointer target determines the action

In deconstruct mode, releasing the left button removes the target. A connected port takes precedence over its machine and disconnects its pipe. A pipe waypoint removes only that waypoint. A machine removes that machine; a decoration removes the decoration. The displayed refund refreshes roughly every 0.1 seconds.

## Shift removes anchored contents

Holding Shift while deconstructing a parent decoration also removes its anchored machines and decorations. The decoration refund path adds machine refunds when anchored contents are included. Without Shift the contents remain. Decorations refund half their own purchase cost. Refunds are not income for earned-Gold statistics.

## Preview before dropping

The overlay shows the available refund collection. It does not refund a whole machine merely for disconnecting a port. Moving groups and individual machine drags have separate collision/cancel behavior; they are not purchases unless a copy blueprint is used.

## Sources

- `Assets.Behaviour.UI.HUD/DeconstructOverlay.cs:26`
- `Assets.Source.Flow/FlowDeco.cs:52`
- `Assets.Behaviour.Flow/WorldFlowPipeNode.cs:31`
