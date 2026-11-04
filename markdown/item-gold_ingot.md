# Gold Ingot

A small bar of purified gold, ready to be turned into art.

## In the game

A small bar of purified gold, ready to be turned into art.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | gold_ingot |
| Item type | Item |
| Source Quest | true |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Transmute Metals](recipe-transmute_metals.md) | [Alchemist](building-Alchemist.md) | 3.0 |
| [Gold Ingot](recipe-gold_ingot.md) | [Forge](building-Forge.md) | 2.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Parade Armor](recipe-gold_armor.md) | 1 |
| [Sapphire Crown](recipe-gold_crown.md) | 2 |
| [Ceremonial Sword](recipe-gold_sword.md) | 3 |
| [Gold Wire](recipe-gold_wire.md) | 1 |
| [Gilded Coffin](recipe-gilded_coffin.md) | 1 |
| [Elegant Ring](recipe-simple_ring.md) | 1 |
| [Prayer Beads](recipe-prayer_beads.md) | 2 |
| [Relic of the Martyr](recipe-martyr_relic.md) | 1 |

## Adventure sources

| Source | Reward set | Base amount / rule |
| --- | --- | --- |
| [Bank "Heist"](quest-bank_heist.md) | First completion rewards | 150 · Base quality 1f |
| [Bank "Heist"](quest-bank_heist.md) | Repeat rewards | 50 · Base quality 1f |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_85\"",
  "SourceQuest": "true"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier3.cs:101`
