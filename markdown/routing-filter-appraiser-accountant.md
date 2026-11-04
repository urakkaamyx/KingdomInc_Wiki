# Filters, Appraisers, and Accountants

Choose exact item filters, stat comparisons, and balance-based gates.

## Filter

Filter’s selector lists unlocked item types. Search matches all words against translated item names. Selecting an item changes its icon and closes the popup. Filter sends exact matching ItemType to output index 0 and other items to index 1. A full chosen output stalls the item instead of using the other output.

## Appraiser

Choose a stat, comparison operator, and integer amount. Operators are ==, !=, <, <=, >, and >=. Current Health, Current Energy, Quality, and Training are marked as percentages; other stats use their numeric units. No selected stat passes every item. True goes to output 0, false to output 1; routing waits when the selected output is full.

## Accountant

Choose a currency, operator and whole-number threshold to open/close a single output. It compares the kingdom balance, not the passing item value. No currency selected passes everything. Gold comparison uses balance/10000, i.e. whole displayed gold coins, whereas other currencies use whole currency units.

## Applying settings

Enter or numpad Enter submits Appraiser/Accountant edits. Empty amount text becomes zero. Applying updates model, icon and displayed threshold and closes the popup. Appraiser current-health/current-energy values are rounded percentages of combatant maximums.

## Sources

- `Assets.Behaviour.UI.ItemFilter/ItemFilterCell.cs:19`
- `Assets.Behaviour.UI.ItemFilter/ItemFilterPopup.cs:32`
- `Assets.Behaviour.UI.ItemAppraiser/ItemAppraiserPopup.cs:29`
- `Assets.Behaviour.UI.ItemAppraiser/ItemAppraiserStatOption.cs:12`
- `Assets.Behaviour.UI.ItemAppraiser/AccountantPopup.cs:28`
- `Assets.Behaviour.Flow.Elements/WorldFlowAppraiser.cs:18`
- `Assets.Behaviour.Flow.Elements/WorldFlowAccountant.cs:18`
- `Assets.Behaviour.Flow.Elements/WorldFlowFilter.cs:14`
- `Assets.Source.Items/AppraiserStatExtensions.cs:5`
- `Assets.Source.Items.Type/CombatantItemType.cs:11`
- `Assets.Source.Flow.Elements/Appraiser.cs:27`
- `Assets.Source.Flow.Elements/Accountant.cs:30`
- `Assets.Source.Flow.Elements/Filter.cs:25`
