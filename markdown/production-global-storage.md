# Armories and shared item storage

Storage terminals share inventories by item type and channel across diagrams.

## Input and output terminals

An Armory terminal configured without OutputType accepts compatible incoming items into the player's shared ArmoryContents. A terminal configured with an OutputType requests that item type from shared storage and buffers it for its pipe.

Stored inventory is indexed by channel and exact ItemType, with eight channels. Capacity checks apply to a particular item type in a channel rather than to a building's total inventory. Multiple terminals on that channel access the same pool across diagrams.

## Costs and dispatch

Armory-family input costs are paid when items enter storage. Ordinary base input cost is 100 Gold, reduced to half by Armory Storage Cost technology. Guildhouse uses a base of 200 Gold; Hoard uses zero.

Stored items are retrieved in FIFO order. Empty output terminals join a waiting queue; an incoming item can be delivered directly into the earliest queued output. Empty requesters briefly wait 0.2 seconds before polling again.

With Armory Overflow technology, an input terminal can pass its waiting item to a connected overflow output when that item's shared capacity is full. Insufficient input fee alone does not trigger overflow because the overflow condition specifically tests storage capacity.

## Storage families

Armory accepts weapons, headgear, and chest armor, with capacity 10 per type and channel. Pantry accepts Food and Potions and keeps capacity 10. Library accepts Scrolls with capacity 5. Treasury accepts Rings, Amulets, and Trinkets with capacity 5.

Guildhouse accepts Adventurers, or all HumanItemType after Guildhouse Conscripts, with capacity 5. Hoard accepts dungeon-sourced items and noncombatant quest-sourced items with capacity 80, has no input fee, and has no channel-unlock technology requirement.

## Editing terminals

Opening the relevant storage popup pauses that specific terminal's processing. When an output terminal changes selected item type, any mismatched item already in its output is returned to shared storage.

## Sources

- `Assets.Source.Flow.Elements/Armory.cs:38`
- `Assets.Source.Flow.Elements/Armory.cs:109`
- `Assets.Source.Flow.Elements/Armory.cs:122`
- `Assets.Source.Flow.Elements/Armory.cs:171`
- `Assets.Source.Items/ArmoryContents.cs:10`
- `Assets.Source.Items/ArmoryContents.cs:54`
- `Assets.Source.Items/ArmoryContents.cs:87`
- `Assets.Source.Flow.Elements/Pantry.cs:23`
- `Assets.Source.Flow.Elements/Library.cs:15`
- `Assets.Source.Flow.Elements/Treasury.cs:15`
- `Assets.Source.Flow.Elements/Guildhouse.cs:15`
- `Assets.Source.Flow.Elements/Hoard.cs:13`
