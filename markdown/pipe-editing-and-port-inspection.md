# Pipes, waypoints, and port inspection

Connect, reroute, disconnect, and inspect the items inside production lines.

## Connections

Left click or drag a port to begin a connection; finish at a port of the opposite direction. Existing connections on either endpoint are disconnected before the new link is made. Starting from an already connected input reroutes from that pipe’s output. Starting from a connected output clears its waypoints first. Right click a connected port to disconnect it.

## Waypoints

While routing a pipe, Ctrl-click empty space to add a waypoint and continue drawing. Waypoints can be clicked/dragged, snapped to an offset grid, or positioned freely with Ctrl. Right click a waypoint removes it. Canceling a waypoint move restores its old coordinate. Pipe rendering and collider geometry follow all waypoints.

## Status colors

A transferred item briefly flashes the pipe white; rejected items set it dark red; timeout flashes dark orange. Port artwork also switches to an error sprite when its connected pipe rejected an item. These are feedback signals from the pipe model.

## Inspect buffers

Hover a port for its item icon preview and buffered count; when empty it can cycle among previewable accepted item types. Hold Shift while hovering for the full item tooltip. Shift-right-click a human item opens character details. Output ports normally buffer one item; FlowInput adds an item only when CanBuffer permits it.

## Sources

- `Assets.Behaviour.Flow/WorldFlowIO.cs:70`
- `Assets.Behaviour.Flow/WorldFlowPipe.cs:30`
- `Assets.Behaviour.Flow/WorldFlowPipeNode.cs:31`
- `Assets.Source.Flow/FlowInput.cs:7`
- `Assets.Source.Flow/FlowOutput.cs:19`
