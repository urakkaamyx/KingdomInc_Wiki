# Necklace of Fireballs

The tiny beads on this necklace are, in fact, dangerous weapons: They spontaneously combust after being thrown.

## In the game

The tiny beads on this necklace are, in fact, dangerous weapons: They spontaneously combust after being thrown.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | fireball_amulet |
| Item type | Equipment |
| Slot | Amulet |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Combat Power | 30 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Necklace of Fireballs](recipe-fireball_amulet.md) | [Jeweler](building-Jeweler.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_215\"",
  "Slot": "EquipmentSlot.Amulet",
  "BaseStats": "new StatSet { (stat: EquipStat.CombatPower, amt: 30) }",
  "EquipTrait": "new AdventurerTrait\n\t\t\t{\n\t\t\t\tDisplayName = \"@fireball_amulet\",\n\t\t\t\tGetDescription = (ActiveTrait trait) => Translation.TranslateOnly(\"@fireball_amulet_trait\", fireballDamage * trait.Quality),\n\t\t\t\tIconName = \"Icons2_215\",\n\t\t\t\tWarTick = (ActiveTrait trait, WarProgress war) =>\n\t\t\t\t{\n\t\t\t\t\twar.PartialProgress += Mathf.RoundToInt(fireballDamage * trait.Quality * trait.Self.GetDamageMultiplier(war));\n\t\t\t\t},\n\t\t\t\tDungeonHealingTick = (ActiveTrait trait, DungeonProgress dungeon) =>\n\t\t\t\t{\n\t\t\t\t\tdungeon.StageProgress += fireballDamage * trait.Quality * trait.Self.GetDamageMultiplier(dungeon);\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier8.cs:266`
