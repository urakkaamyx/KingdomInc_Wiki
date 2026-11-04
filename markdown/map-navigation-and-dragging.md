# Map navigation and dragging

Camera scales, click-to-move, drag-to-move, snapping, and cancellation.

## Camera

WASD moves the world or technology camera. Movement speed scales with 5−zoomLevel. Zoom levels 0–4 use scales 0.25, 0.5, 1, 2, and 4; maximum level is 3 on screens no taller than 1400 unless UI scale exceeds 1, otherwise 4. Zoom adjusts around the mouse. Bounds surround placed machines with about 1000 world units of margin; technology bounds surround visible tech nodes.

## Click or drag

DragDropManager supports holding the left mouse button and releasing to drop, or clicking once to pick up and again to drop. New drags are blocked during deconstruction and the initial tutorial blackout. Text fields delay normal player shortcuts while focused.

## Move a machine

Click or drag its title label. Ctrl bypasses grid snapping. Dropping onto another machine restores its prior position. Cancel restores its old position unless it has already been transferred to another workflow. Moving a single machine to another workflow disconnects all of its pipes.

FlowCollider separates dragged machines into another layer; collision tests reject machine overlaps, while decorations are allowed behind machines. Prefab lookup uses the machine ElementType to select its UI, decorative background, and category title border.

## Sources

- `Assets.Behaviour.Flow/WorldFlowCamera.cs:58`
- `Assets.Behaviour.Flow/WorldFlowLabel.cs:18`
- `Assets.Behaviour.Flow/FlowCollider.cs:19`
- `Assets.Behaviour.Flow/FlowColliderManager.cs:12`
- `Assets.Behaviour.Flow/FlowPrefabManager.cs:20`
- `Assets.Behaviour.Flow/FlowPrefabSet.cs:21`
- `Assets.Behaviour.UI/DragDropManager.cs:30`
- `Assets.Behaviour.UI/IDragDropTarget.cs:5`
- `Assets.Behaviour.UI/ActiveTextField.cs:11`
