# Machine stacks, mirrored ports, and upgrade slots

Additional mouse gestures and how upgrade replacement charges and refunds work.

## Stack and mirror

After element_stacking, Ctrl-left-click a stackable machine to add one copy, up to stack size 5. The game charges GetSingleCopyCost, updates upgrade effects and label, and shows the stack as layered backgrounds. It does not stack while deconstructing or when the pointer is on a Button or port. Alt-left-click flips Mirrored and rebuilds port positions and pipe lines.

## Picker

Middle click after unlock_picker opens a configured purchase copy if affordable. Pointer travel exceeding 50 world units suppresses accidental clicks after panning.

## Upgrade slots

Click a slot to see Remove plus available researched upgrades. Hover an option to see its effect at the relevant nth duplicate, its purchase cost, and any old-upgrade refund. Selecting a different type charges the new price and refunds the old upgrade; selecting Remove only refunds. Selecting the same upgrade type opens/closes the chooser without buying a second copy.

With easy_node_upgrade, Ctrl-clicking a slot asks the machine for its automatic recommended upgrade and attempts to buy that. Progress bars show current crafting and productivity; the full-output warning appears after completed progress remains blocked for more than 0.1 seconds.

## Sources

- `Assets.Behaviour.Flow/WorldFlowElement.cs:116`
- `Assets.Behaviour.Flow/WorldFlowUpgrade.cs:37`
- `Assets.Behaviour.Flow/WorldFlowUpgradeOption.cs:20`
- `Assets.Behaviour.Flow/CraftButtonWarning.cs:16`
