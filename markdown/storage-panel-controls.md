# Armory and Portal configuration

Input/output modes, eight colors, numbered subchannels, and shared inventories.

## Armory

The popup has eight color channels. Channel selectors are hidden unless the machine’s ChannelTech is owned. Choose the Input row to store items, or an available compatible item type to output it. Available output types are sorted by item ordinal; rows show stored count and peek-item tooltips.

## Safe mode switching behavior

Switching from output to input clears outputs; switching from input to output clears inputs. Changing an output type returns the currently connected pipe’s input/output buffers to the Armory channel and clears those buffers before reconfiguring the output. Changing channels refreshes colors and item choices.

## Portal

The Portal popup always builds eight color choices and eight numbered index choices. Numbered indices are shown after portal_unlock_channels; the labels are 1–8 while storage uses indices 0–7. Choose Input or Output to set its direction. Changing an output Portal’s color or index first clears its output. Index contents refresh about every 0.2 seconds.

## Find linked stores

World Armory and Portal adapters show channel colors and live item/count information. Their cycle action finds the next related machine and calls ShowElement, allowing navigation to another linked storage endpoint. Empty stores have no fabricated item tooltip.

## Sources

- `Assets.Behaviour.UI.ItemStore/ArmoryChannelSelect.cs:18`
- `Assets.Behaviour.UI.ItemStore/ArmoryItemRow.cs:32`
- `Assets.Behaviour.UI.ItemStore/ArmoryPopup.cs:52`
- `Assets.Behaviour.UI.ItemStore/PortalIndexSelect.cs:29`
- `Assets.Behaviour.UI.ItemStore/PortalPopup.cs:43`
- `Assets.Behaviour.Flow.Elements/WorldFlowArmory.cs:29`
- `Assets.Behaviour.Flow.Elements/WorldFlowPortal.cs:46`
