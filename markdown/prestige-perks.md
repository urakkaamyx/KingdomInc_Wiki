# Prestige perks and refunds

All nine perks and their exact rank formulas.

## Ranks and refunds

A zero-point perk has zero effect. Rank n costs n nightmares: first rank 1, second 2, third 3. Total rank-n investment is n(n+1)/2. Unspent nightmares equal total NightmareCount minus all invested rank costs. Left click buys a rank when affordable; right click refunds a rank; Reset sets every perk to zero.

## Perk formulas

| Identifier | Value at n≥1 | Rank 1 | Rank 2 |
| --- | --- | --- | --- |
| tech_cost_reduce | 0.50+0.05(n−1) | 50% discount | 55% |
| resource_cost_reduce | 0.05+0.02(n−1) | 5% reduction | 7% |
| currency_tax_reduce | 0.25+0.05(n−1) | 25% tax reduction | 30% |
| equipment_quality | 0.02n | +2 percentage points | +4 points |
| human_quality | 0.02n | +2 percentage points | +4 points |
| handcrafting_productivity | 1+0.25(n−1) | +100% value | +125% |
| dark_essence_quality | 0.10+0.05(n−1) | +10 percentage points | +15 points |
| human_health | 0.05n | +5% | +10% |
| sell_value | 0.05n | +5% | +10% |

## Application

Research discount multiplies generated research currency collections. Resource discount is read by player resource upgrades, Forest crew upgrades, and Farm upgrades. Human quality is added during human resource generation; equipment and dark-essence quality are added in the relevant crafting-result creation. Human health is included in HumanItemData health calculation; sell value is read by Shop and LuxuryShop. Manual productivity is read by RecipeElement. Manual crafting adds the perk value to current Productivity before accumulating productivity progress; equipment manually receives a further ×0.5 factor.

The purchase handler has no explicit per-perk rank cap. The formulas above are literal source behavior; extrapolated extreme ranks are not balanced-design recommendations.

## Sources

- `Assets.Source.Player/PrestigeNode.cs:14`
- `Assets.Source.Player/PrestigeNode.cs:103`
- `Assets.Source.Player/PrestigeNode.cs:114`
- `Assets.Source.Player/GamePlayer.cs:107`
- `Assets.Behaviour.UI.Prestige/UIPrestigeNode.cs:111`
- `Assets.Behaviour.UI.Prestige/PrestigeUI.cs:95`
- `Assets.Source.Flow.Elements/RecipeElement.cs:399`
- `Assets.Source.Items/CraftingResult.cs:57`
- `Assets.Source.Items.Data/HumanItemData.cs:233`
