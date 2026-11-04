# Glass Vial

An empty sterilized vessel used in the creation of potions.

## In the game

An empty sterilized vessel used in the creation of potions.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | glass_vial |
| Item type | Resource |
| Resource Value | 800 |
| Resource Cost | new CurrencyCollection().Add(Currency.Gold, 800L) |
| Tag | Adventure Supplies |

## Gathering

| Building | Research | Quota step |
| --- | --- | --- |
| [Adventure Supplies](building-AdventureSupplies.md) | [Glass Vial](tech-glass_vial.md) | 1.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Healing Potion](recipe-healing_potion.md) | 1 |
| [Revitalizing Potion](recipe-energy_potion.md) | 1 |
| [Elixir of Fire Resistance](recipe-fire_resist_potion.md) | 1 |
| [Elixir of Shadow Resistance](recipe-shadow_resist_potion.md) | 1 |
| [Elixir of Poison Resistance](recipe-poison_resist_potion.md) | 1 |
| [Stoneskin Elixir](recipe-armor_potion.md) | 1 |
| [Greater Healing Potion](recipe-greater_healing_potion.md) | 1 |
| [Elixir of Mastery](recipe-stats_potion.md) | 1 |
| [Elixir of Alacrity](recipe-swiftness_potion.md) | 1 |
| [Elixir of Regeneration](recipe-regen_potion.md) | 1 |
| [Enchanted Ink](recipe-enchanted_ink.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_223\"",
  "ResourceValue": "800L",
  "ResourceCost": "new CurrencyCollection().Add(Currency.Gold, 800L)",
  "Tag": "ResourceTag.AdventureSupplies"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier9.cs:126`
