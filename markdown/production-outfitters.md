# Outfitters and equipment automation

Pair humans with compatible equipment and return the equipped character.

## Inputs and fitting

An Outfitter takes one HumanItemType and one EquipmentItemType. Its input filters check equipment compatibility against the other waiting input when present. Outfitter Skip Replace technology influences whether occupied slots may be replaced.

When both inputs are present, the node examines conflicting equipment. If any conflicting equipped item has the exact same item type as the incoming equipment, it forwards the human unchanged and keeps the incoming equipment available for another character.

Otherwise it consumes both into CurrentHuman and CurrentEquip and calls AddEquipment on the human. Completion returns that human after progress reaches 1 at Speed progress per second.

## Manual approval and automation

Without Outfitter Automation, an unqueued fitting stops at 80% progress until manually released by its interface. Automation allows it to continue past that point without the queued release.

This setting is a separate technology check, not the generic Worker-derived CanAutoCraft. Output space is required before any fitting work proceeds.

## Timeout

When a human is waiting without equipment and Timeout is greater than zero, the Outfitter accumulates a timeout and forwards the unchanged human after it is exceeded. The timeout resets when a fitting begins or neither relevant wait condition applies.

Timeout value is copied and saved. Routing humans with incompatible equipment can reject the pipe, so mixed equipment lines benefit from filtering by slot or character eligibility.

## Sources

- `Assets.Source.Flow.Elements/Outfitter.cs:35`
- `Assets.Source.Flow.Elements/Outfitter.cs:72`
- `Assets.Source.Flow.Elements/Outfitter.cs:81`
- `Assets.Source.Flow.Elements/Outfitter.cs:97`
- `Assets.Source.Flow.Elements/Outfitter.cs:156`
