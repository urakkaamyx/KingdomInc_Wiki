# Elixir of Regeneration

The thick liquid burns on the way down, in a pleasant way. The drinker feels continuously reinvigorated, an effect that can last for days.

## In the game

The thick liquid burns on the way down, in a pleasant way. The drinker feels continuously reinvigorated, an effect that can last for days.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | regen_potion |
| Item type | Equipment |
| Slot | Potion |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Health | 24 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Elixir of Regeneration](recipe-regen_potion.md) | [Alchemist](building-Alchemist.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_159\"",
  "Slot": "EquipmentSlot.Potion",
  "BaseStats": "new StatSet { \n\t\t\t{\n\t\t\t\tEquipStat.Health,\n\t\t\t\t24\n\t\t\t} }",
  "EquipTrait": "new AdventurerTrait\n\t\t\t{\n\t\t\t\tDisplayName = \"@regen_potion_trait\",\n\t\t\t\tGetDescription = (ActiveTrait trait) => Translation.TranslateOnly(\"@regen_potion_trait_desc\", 6f * trait.Quality / 2f),\n\t\t\t\tIconName = \"Icons2_213\",\n\t\t\t\tArenaTick = (ActiveTrait trait, Arena arena) =>\n\t\t\t\t{\n\t\t\t\t\t_regenEffect(trait, arena);\n\t\t\t\t},\n\t\t\t\tQuestTick = (ActiveTrait trait, QuestProgress quest) =>\n\t\t\t\t{\n\t\t\t\t\t_regenEffect(trait, quest);\n\t\t\t\t},\n\t\t\t\tWarTick = (ActiveTrait trait, WarProgress war) =>\n\t\t\t\t{\n\t\t\t\t\t_regenEffect(trait, war);\n\t\t\t\t},\n\t\t\t\tDungeonHealingTick = (ActiveTrait trait, DungeonProgress dungeon) =>\n\t\t\t\t{\n\t\t\t\t\t_regenEffect(trait, dungeon);\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier9.cs:94`
