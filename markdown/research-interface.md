# Research tree and list interface

Navigate branches, locate technologies, and distinguish visible clues from purchasable nodes.

## Tree navigation

Opening research shows the global tree; selecting an owned root opens its child branch. Clicking the same root again returns global. The War branch also displays War-type nodes and the Dungeon branch Dungeon-type nodes. Hidden technologies are filtered out. Camera position and zoom are saved on the player.

## Availability cues

Available nodes show price, glow and purchase behavior. Locked nodes use unknown/gray states; a node’s identity may appear when an adjacent prerequisite is available or purchased. Custom unmet requirements are appended in red. Owned roots show counts of currently available children and a new-tech indicator based on the last seen count.

## Research list

global_tech_upgrade exposes the list button. The list groups available roots, available children, locked nodes, and purchased nodes. Left click buys an available row after affordability check; right click an unlocked row focuses that node in its branch. The inspected implementation appends purchased nodes through two loops, so duplicate purchased rows can appear.

## Exit behavior and dormant code

Escape closes list first, then a branch, then research. Cancel can return from a branch if the pointer was not dragged far; right-clicking a list row is reserved for locate. UIElementTechNode contains child-purchase helper code, but _childPurchaseActive always returns false in this inspected build, so that shortcut is dormant.

## Sources

- `Assets.Behaviour.UI.TechTree/TechTreeListItem.cs:43`
- `Assets.Behaviour.UI.TechTree/TechTreeListView.cs:29`
- `Assets.Behaviour.UI.TechTree/TechTreeMenu.cs:68`
- `Assets.Behaviour.UI.TechTree/UIElementTechNode.cs:61`
- `Materials.cs:27`
