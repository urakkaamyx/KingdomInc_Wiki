# Requisition Offices and contracts

Convert selected equipment types into Requisition using base value.

## Contract deliveries

An office selects an index from the player's shared list of contracted item types and accepts exactly that type. It adds integer(BaseValue × (1 + 0.1 × Req Cashier count)) to StoredValue for each item consumed.

The code uses item.Type.BaseValue, so item quality and added enhancement sell value do not increase delivery credit. Every 1,000 StoredValue converts into one Requisition, with the remainder retained as progress.

## Capacity, workers, and passive generation

Stored Requisition capacity is 10 × (1 + 2 × Coffers count). Reaching capacity stops the update before passive progress and deliveries. A completion can go above capacity because generated Requisition is added as a batch.

Without a Worker, generated Requisition remains local until collected. With a Worker, new Requisition and any pending local collection are credited immediately. Installing an automatic worker also collects an existing local balance.

Each Req Passive upgrade adds 0.02 Requisition worth of stored value per one-second tick: 20 StoredValue per second at the normal 1,000 gold equivalent, or one Requisition every 50 seconds.

## Contract generation and reroll cost

The first generated contract is randomly iron sword or iron dagger. The second is simple robe, rough vest, or softwood bow. Later candidates come from available recipe results that are EquipmentItemType; already contracted types are removed while more than one candidate remains.

Fallbacks for missing random candidates are mushroom stew for contract 3, wild staff for 4, arcanium sword for 5, and iron sword afterwards. Reroll cost spends all current Requisition if below five; otherwise it is max(5, current Requisition integer-divided by 100).

## Sources

- `Assets.Source.Flow.Elements/RequisitionOffice.cs:75`
- `Assets.Source.Flow.Elements/RequisitionOffice.cs:88`
- `Assets.Source.Flow.Elements/RequisitionOffice.cs:101`
- `Assets.Source.Flow.Elements/RequisitionOffice.cs:196`
- `Assets.Source.Flow.Elements/RequisitionOffice.cs:219`
- `Assets.Source.Flow.Elements/RequisitionOffice.cs:251`
