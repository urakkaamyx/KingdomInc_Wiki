# Annihilate Gemstone recipe

Destroys the physical structure of an ancient gem, releasing the latent magic within.

## In the game

Destroys the physical structure of an ancient gem, releasing the latent magic within.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Enchanter](building-Enchanter.md) |
| Base crafting time | 4 seconds |
| Research | [Annihilate Gemstone](tech-annihilate_gemstone.md) |
| Currency reward per batch | 460 Mana |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Ancient Gemstone](item-ancient_gem.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_195\"",
  "Tag": "tag",
  "CraftingTimeMultiplier": "2f",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"ancient_gem\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[0]",
  "CraftingReward": "new CurrencyCollection(Currency.Mana, 460L)"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Enchanter.cs:165`
- `Assets.Source.Items/CraftingRecipe.cs:1`
