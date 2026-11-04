# Building, copying, and area movement

Placement ghosts, costs, snapping, repeated builds, cloned networks, and moving groups.

## Placement

Click a purchase row for a blueprint or drag it for drag placement. Ghost footprints turn red on flow-collider overlap. Ctrl bypasses grid snapping. Placement checks affordability, spends cost, creates a copy, and positions it. Individual overlap shows NoSpace.

## Repeated builds and copied networks

Shift keeps the ghost active and updates cost for another placement. Otherwise blueprint mode ends and the buy menu may reopen. Cancel closes the ghost.

Copying a decorated container can include anchored machines/decorations. The game maps originals to copies, reconnects pipes whose two endpoints are copied, and offsets intermediate pipe nodes. That loop does not recreate connections to machines outside the selection.

## Area copy

clone_tool gates area copy. Overlapping colliders select machines first to establish a blueprint root, then decorations. A selection containing only decorations does not create an area-copy root in this implementation. The rectangle previews combined costs; very tiny selections are ignored.

## Area movement

unlock_area_move gates area movement. It creates an invisible temporary parent decoration and starts its drag mover to move existing parts instead of purchasing copies. Container movement uses anchored parts.

## Blueprint persistence

These classes implement in-memory placement/copy ghosts. No separate exported blueprint library or import/export format was found here. Normal player saves persist layouts and configuration.

## Additional workflows

add_diagrams research adds a workflow; element_stacking follows it. Extra workflows cost 100,000 raw-Gold-equivalent in Rings plus 100,000 in Gold while fewer than five workflows exist, otherwise Crowns replace Gold. The collection is multiplied by 1.3^(current workflow count).

## Sources

- `Assets.Behaviour.UI.BuyMenu/BuyMenuRow.cs:68`
- `Assets.Behaviour.Flow/WorldFlowGhost.cs:103`
- `Assets.Behaviour.Flow/WorldFlowGhost.cs:113`
- `Assets.Behaviour.Flow/WorldFlowGhost.cs:149`
- `Assets.Behaviour.Flow/WorldFlowGhost.cs:200`
- `Assets.Behaviour.UI.BuyMenu/AreaCopyGhost.cs:94`
- `Assets.Behaviour.UI.BuyMenu/AreaMoveGhost.cs:35`
- `Assets.Source.Player/GamePlayer.cs:639`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:67`
