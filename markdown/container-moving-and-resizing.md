# Container anchors, resizing, and group movement

How decorated areas collect machines, labels, and pipe waypoints.

## Anchored parts

An IsParent decoration gathers overlapping machines, decorations, and pipe waypoints. It recursively follows parent decorations, deduplicates machines/decorations, and normally excludes other containers unless requested. Turning Anchor off makes the decoration move alone. Labels can be parents too.

## Move and resize

Use the move handle to pick up a parent and its anchored parts. Ctrl bypasses the layout grid. On drop, any overlapping anchored machine causes the complete group to revert. Cancel also reverts unless the group has crossed to another workflow. Resize from a corner; minimum width and height are 64. Cancel restores old position and size.

## Move between workflows

A group transfer retains pipes with both endpoints in the moved machine set and transfers their waypoints; crossing-boundary connections are disconnected. Decorations and anchored pipe nodes move with it. The temporary parent used by area-move is destroyed afterward.

## Lock and clone

Lock hides normal move/edit/resize controls and exposes an unlock control. At far zoom levels the edit button is hidden and move handles scale up. Middle click copies an affordable decorated group after container_clone. Clicking a parent label can locate the overlapping container for that clone action.

## Sources

- `Assets.Behaviour.Flow/WorldFlowDeco.cs:69`
- `Assets.Behaviour.Flow/WorldFlowDecoEdit.cs:18`
- `Assets.Behaviour.Flow/WorldFlowDecoMover.cs:39`
- `Assets.Behaviour.Flow/WorldFlowDecoResizer.cs:30`
