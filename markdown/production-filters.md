# Filters, Appraisers, Inspectors, and Accountants

Sort by type, statistics, or the kingdom's current currency balance.

## Filter

Filter has one generic input and two outputs. An exact match to the chosen ItemType goes to output zero; everything else goes to output one. Only the matching route's capacity is checked, so a blocked selected branch stalls that item instead of falling back.

With no chosen type, ordinary input items all go to the nonmatching output. Setting the filter also gives the first output that item's preview type.

## Appraiser

Appraiser evaluates one selected AppraiserStat and a threshold with Equal, Not Equal, Less Than, Less Than or Equal, Greater Than, or Greater Than or Equal. Passing items go to the first output; failures to the second.

With no selected stat every item passes. Ordinary items report Quality and Training as round(Quality × 100), and zero for unsupported statistics; specialized item types can override the statistic calculation.

## Accountant

Accountant releases an item only when its currency comparison passes. It supports the same six comparison operators. It does not charge or reserve the tested currency, so the condition is a gate based on the player's current balance.

Gold balances are integer-divided by 10,000 before comparison. The threshold therefore uses groups of 10,000 Gold. With no selected currency, items pass freely.

## Inspector

Inspector passes the actual inventory item onward, stores a clone as LastItem for inspection, and keeps a LiveItem reference to the actual object. It does not modify the item's quality or equipment. All these tools use one-item buffers and require their relevant output to have space.

## Sources

- `Assets.Source.Flow.Elements/Filter.cs:55`
- `Assets.Source.Flow.Elements/Filter.cs:61`
- `Assets.Source.Flow.Elements/Appraiser.cs:57`
- `Assets.Source.Flow.Elements/Appraiser.cs:70`
- `Assets.Source.Items/ItemType.cs:297`
- `Assets.Source.Flow.Elements/Accountant.cs:55`
- `Assets.Source.Flow.Elements/Accountant.cs:63`
- `Assets.Source.Flow.Elements/Inspector.cs:42`
