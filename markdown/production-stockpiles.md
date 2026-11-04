# Stockpiles and overflow

Local first-in, first-out storage smooths variable production.

## Storage and output

A Stockpile has a one-item input, one-item main output, and an internal FIFO list with default capacity 10. Each update it accepts one input item if the internal list has room, then moves the oldest stored item into the main output if that output has room.

The input and output buffers are outside the internal Contents count. Consequently a full ten-item internal list is not the entire number of items the node can hold. Mixed item types are allowed and retain insertion order.

## Overflow behavior

Stockpile Overflow adds a second output. When that output is connected and free, an input item is waiting, and the internal list is at least capacity, the node sends the oldest stored item to overflow first. It then admits the waiting input item.

Overflow therefore releases an older stored item, not the newest arriving item. A full stockpile with no incoming item does not automatically drain through overflow. Main output continues to use the oldest remaining item.

## Capacity controls

Stockpile Capacity technology enables the capacity slider. Adjusting it changes the internal Capacity integer; the value is copied and saved. Reducing the capacity does not immediately delete existing Contents.

## Sources

- `Assets.Source.Flow.Elements/Stockpile.cs:11`
- `Assets.Source.Flow.Elements/Stockpile.cs:59`
- `Assets.Source.Flow.Elements/Stockpile.cs:76`
- `Assets.Source.Flow.Elements/Stockpile.cs:94`
- `Assets.Behaviour.Flow.Elements/WorldFlowStockpile.cs:75`
