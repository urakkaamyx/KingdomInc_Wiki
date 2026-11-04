# Amulet of Vigor

Energizes the wearer and anyone in their vicinity.

## In the game

Energizes the wearer and anyone in their vicinity.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | amulet_of_energy |
| Item type | Equipment |
| Slot | Amulet |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Energy | 25 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Amulet of Vigor](recipe-amulet_of_energy.md) | [Jeweler](building-Jeweler.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_166\"",
  "Slot": "EquipmentSlot.Amulet",
  "BaseStats": "new StatSet { (stat: EquipStat.Energy, amt: 25) }",
  "EquipTrait": "new AdventurerTrait\n\t\t\t{\n\t\t\t\tDisplayName = \"@amulet_of_energy_trait\",\n\t\t\t\tGetDescription = (ActiveTrait trait) => Translation.TranslateOnly(\"@amulet_of_energy_trait_desc\", 40f * trait.Quality),\n\t\t\t\tIconName = \"Icons2_55\",\n\t\t\t\tQuestTick = (ActiveTrait trait, QuestProgress quest) =>\n\t\t\t\t{\n\t\t\t\t\t_restoreEnergy(trait, quest.Parent.Contents);\n\t\t\t\t},\n\t\t\t\tDungeonHealingTick = (ActiveTrait trait, DungeonProgress dungeon) =>\n\t\t\t\t{\n\t\t\t\t\t_restoreEnergy(trait, dungeon.Party);\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier8.cs:169`
