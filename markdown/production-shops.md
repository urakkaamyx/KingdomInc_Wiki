# Shops and gold collection

Shops sell suitable items immediately into a local till, then require collection.

## What Shops accept

A Shop accepts any sellable item with positive SellValue except CombatantItemType. Its one-item input is consumed whenever the till is below capacity; item sale itself has no per-item crafting timer.

Sale gold is rounded SellValue × (1 + 0.05 × Cashier count), then multiplied by 1 + Sell Value prestige when that bonus is positive. The last five sales are retained for its tooltip.

## Capacity and collection

Base gold capacity is 10,000, increased to 50,000 with Shop Expansion. Coffers multiply that base capacity by 1 + 2 × Coffers count. A sale can take the till above its cap because capacity is checked before the whole item value is added.

Manual collection transfers the smaller of stored gold and capacity. Overflow from a very valuable sale stays in the till for another collection. A Worker collects every 10 ÷ Speed seconds; extra workers and stacks improve that collection interval.

The first Shop is free. StackSize changes computed Speed, while capacity is based on GoldCap and Coffers count rather than stack size.

## Sources

- `Assets.Source.Flow.Elements/Shop.cs:38`
- `Assets.Source.Flow.Elements/Shop.cs:66`
- `Assets.Source.Flow.Elements/Shop.cs:99`
- `Assets.Source.Flow.Elements/Shop.cs:106`
- `Assets.Source.Flow.Elements/Shop.cs:135`
- `Assets.Source.Flow.Elements/Shop.cs:157`
